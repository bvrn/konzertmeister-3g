#!/usr/bin/env python

from __future__ import annotations

from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import List, Optional

import numpy as np
import pandas as pd
import pdfkit
import typer


class OutputFormats(str, Enum):
    csv = "csv"
    html = "html"
    latex = "latex"
    md = "md"
    pdf = "pdf"
    xlsx = "xlsx"

    @classmethod
    @property
    def entries(cls) -> List[OutputFormats]:
        return [e for e in cls]


app = typer.Typer()

def query_user_input():
    format = [
        e for e in OutputFormats.entries if typer.confirm(f"Export {e.value}?")
    ]
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
    if not format:
        typer.echo(
            typer.style(
                "No export format chosen. Exiting now.",
                fg=typer.colors.WHITE,
                bg=typer.colors.RED,
            ),
            err=True,
        )
        raise typer.Exit(code=1)
    
    return format, title, date, checkbox

@app.command()
def convert(
    file: typer.FileText = typer.Argument(..., help="Konzertmeister CSV"),
    format: Optional[List[OutputFormats]] = typer.Option(
        None,
        "-f",
        "--format",
        help="Output format(s). Repeat for multiple values.",
        case_sensitive=False,
        show_default=False,
    ),
    checkbox: bool = typer.Option(
        False,
        "-c",
        "--checkbox",
        help="Checkbox in HTML and Markdown?",
        show_default=False,
    ),
    title: Optional[str] = typer.Option(
        "Nachweiskontrolle 3G (Getestet, Genesen, Geimpft)"
    ),
    date: Optional[str] = datetime.now().strftime("%d.%m.%Y"),
    output: Path = typer.Option(
        Path(".").resolve(),
        "-o",
        "--output",
        exists=True,
        file_okay=False,
        dir_okay=True,
        writable=True,
        resolve_path=True,
    ),
):
    if not format:
        format, title, date, checkbox = query_user_input()

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
    if OutputFormats.html in format:
        with open(basename + ".html", "w", encoding="utf-8") as file:
            file.write(html_rendered)
    if OutputFormats.xlsx in format:
        df.style.set_caption(f"{title} – {date}").apply(rower, axis=None).apply(
            colorize, axis=0, subset=pd.IndexSlice[:, "Rückmeldung"]
        ).to_excel(basename + ".xlsx", index=False)
    if OutputFormats.csv in format:
        df.to_csv(basename + ".csv", index=False)
    if OutputFormats.latex in format:
        df.to_latex(basename + ".tex", index=False)
    if OutputFormats.md in format:
        df_checkboxes.to_markdown(basename + ".md", index=False)
    if OutputFormats.pdf in format:
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
