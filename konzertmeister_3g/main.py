from datetime import datetime
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
import pdfkit
import typer

app = typer.Typer()


@app.command()
def convert(
    file: typer.FileText = typer.Argument(..., help="Konzertmeister CSV"),
    interactively: bool = typer.Option(
        False,
        "--interactively",
        "-i",
        help="ask for everything interactively",
        show_default=False,
    ),
    pdf: bool = typer.Option(False, "--pdf", help="export PDF", show_default=False),
    xlsx: bool = typer.Option(False, "--xlsx", help="export XLSX", show_default=False),
    html: bool = typer.Option(False, "--html", help="export HTML", show_default=False),
    markdown: bool = typer.Option(
        False, "--md", help="export Markdown", show_default=False
    ),
    latex: bool = typer.Option(
        False, "--latex", help="export LaTeX", show_default=False
    ),
    csv: bool = typer.Option(False, "--csv", help="export CSV", show_default=False),
    checkbox: bool = typer.Option(
        False, "--checkbox", help="Checkbox in HTML and Markdown?", show_default=False
    ),
    title: Optional[str] = typer.Option(
        "Nachweiskontrolle 3G (Getestet, Genesen, Geimpft)"
    ),
    date: Optional[str] = datetime.now().strftime("%d.%m.%Y"),
):
    if not (pdf or xlsx or html or markdown or latex or csv) or interactively:
        pdf = typer.prompt(
            "Export PDF [y/N]", default=False, type=bool, show_default=False
        )
        xlsx = typer.prompt(
            "Export XLSX [y/N]", default=False, type=bool, show_default=False
        )
        html = typer.prompt(
            "Export HTML [y/N]", default=False, type=bool, show_default=False
        )
        markdown = typer.prompt(
            "Export Markdown [y/N]", default=False, type=bool, show_default=False
        )
        latex = typer.prompt(
            "Export LaTeX [y/N]", default=False, type=bool, show_default=False
        )
        csv = typer.prompt(
            "Export CSV [y/N]", default=False, type=bool, show_default=False
        )
        if not (pdf or xlsx or html or markdown or latex or csv):
            typer.echo(
                typer.style(
                    "No export format chosen. Exiting now.",
                    fg=typer.colors.WHITE,
                    bg=typer.colors.RED,
                ),
                err=True,
            )
            raise typer.Exit(code=1)

    if interactively:
        title = typer.prompt(
            "Title",
            default="Nachweiskontrolle 3G (Getestet, Genesen, Geimpft)",
            type=str,
            show_default=True,
        )
        date = typer.prompt(
            "Date",
            default=datetime.now().strftime("%d.%m.%Y"),
            type=str,
            show_default=True,
        )
        checkbox = typer.prompt(
            "Export with Checkboxes? [y/N]",
            default=False,
            type=bool,
            show_default=False,
        )

    basename = Path(file.name).resolve().stem

    df = pd.read_csv(file, sep=";", encoding="utf-8")

    df.drop(df.columns[[1, 2, 4]], axis=1, inplace=True)
    dropped_rows = df[
        df.iloc[:, 1].str.isnumeric()
    ].index  # only records without Numbers (dropping sections)
    df.drop(dropped_rows, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.sort_values(
        by=[df.columns[1], df.columns[0]], ascending=[False, True], inplace=True
    )
    df.reset_index(drop=True, inplace=True)

    df["Getestet"] = ""
    df["Genesen"] = ""
    df["Geimpft"] = ""

    df_checkboxes = df.copy()
    if checkbox:
        df_checkboxes["Getestet"] = "<input type='checkbox'>"
        df_checkboxes["Genesen"] = "<input type='checkbox'>"
        df_checkboxes["Geimpft"] = "<input type='checkbox'>"

    html_rendered = (
        df_checkboxes.style.set_caption(f"{title} – {date}")
        .apply(rower, axis=None)
        .apply(colorize, axis=0, subset=pd.IndexSlice[:, "Rückmeldung"])
        .hide_index()
        .render()
    )
    html_rendered = f"<meta charset='UTF-8'>\n{html_rendered}"
    if html:
        with open(basename + ".html", "w", encoding="utf-8") as file:
            file.write(html_rendered)
    if xlsx:
        df.style.set_caption(f"{title} – {date}").apply(rower, axis=None).apply(
            colorize, axis=0, subset=pd.IndexSlice[:, "Rückmeldung"]
        ).to_excel(basename + ".xlsx", index=False)
    if csv:
        df.to_csv(basename + ".csv", index=False)
    if latex:
        df.to_latex(basename + ".tex", index=False)
    if markdown:
        df_checkboxes.to_markdown(basename + ".md", index=False)
    if pdf:
        pdfkit.from_string(html_rendered, basename + ".pdf", options={"quiet": ""})


def colorize(series):
    return [
        "color: red"
        if element == "Absage"
        else "color: blue"
        if element == "Zusage"
        else "color: orange"
        for element in series
    ]


def rower(data):
    """
    https://stackoverflow.com/a/61009688
    """
    s = data.index % 2 != 0
    s = pd.concat([pd.Series(s)] * data.shape[1], axis=1)  # 6 or the n of cols u have
    z = pd.DataFrame(
        np.where(s, "background-color:#f2f2f2", ""),
        index=data.index,
        columns=data.columns,
    )
    return z


if __name__ == "__main__":
    app()
