<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!--
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  -->
</p>

<h3 align="center">Konzertmeister 3 "G"</h3>

<p align="center">
erstellt aus einer Anwesenheitsliste verschiedene Formate zum Abhaken der drei "G"s (Getestet, Genesen, Geimpft)
<br />
<br />
<a href="https://github.com/bvrn/konzertmeister-3g/issues">Report Bug</a>
·
<a href="https://github.com/bvrn/konzertmeister-3g/issues">Request Feature</a>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#problems">Problems</a></li>
    <li><a href="#Example">Example</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li>
      <a href="#contributing">Contributing</a>
      ul>
        <li><a href="#dependency-management">Dependency Management</a></li>
        <li><a href="#code-quality">Code quality</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

konzertmeister-3g ist ein Kommandozeilentool und erstellt aus einer Anwesenheitsliste verschiedene Formate zum Abhaken
der drei "G"s (Getestet, Genesen, Geimpft).

### Built With

* [Typer](https://typer.tiangolo.com/)
* [Poetry](https://python-poetry.org/)
* [Pyinstaller](https://www.pyinstaller.org/)

<!-- GETTING STARTED -->

## Getting Started

Grundvoraussetzung ist eine CSV Datei mit den Anwesenheiten aus Konzertmeister exportiert.
In [example/export_attendence.html](example/export_attendences.html) ist der Weg dazu beschrieben.

### Prerequisites

Vorausgesetzt wird eine [Python](https://www.python.org/downloads) Umgebung
mit [PIP](https://geekflare.com/de/python-pip-installation/).

### Installation

1. Wheel Datei (.whl) aus den [Releases](https://github.com/bvrn/konzertmeister-3g/releases) herunterladen.
2. konzertmeister-3g installieren
   ```sh
   pip install konzertmeister_3g*.whl
   ```
3. Completions installieren (optional)
   ```sh
   konzertmeister-3g --install-completion
   ```

<!-- USAGE EXAMPLES -->

## Usage

```console
$ konzertmeister-3g [OPTIONS] FILE
```

**Arguments**:

* `FILE`: Konzertmeister CSV  [required]

**Options**:

* `-i, --interactively`: ask for everything interactively
* `--pdf`: export PDF
* `--xlsx`: export XLSX
* `--html`: export HTML
* `--md`: export Markdown
* `--latex`: export LaTeX
* `--csv`: export CSV
* `--checkbox`: Checkbox in HTML and Markdown?
* `--title TEXT`: [default: Nachweiskontrolle 3G (Getestet, Genesen, Geimpft)]
* `--date TEXT`: [default: _aktuelles Datum_]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

## Problems

Es scheint, als gäbe es Probleme unter Windows (Mac nicht getestet). Auch gibt es bis jetzt nur fertige mit pyinstaller
gepackte ausführbare releases.

## Example

Hier ein Beispiel, welches auch in [example](example) zu finden ist.
[![asciicast](https://asciinema.org/a/lM3uytLF8ccRC3QwIG6J6XWmD.svg)](https://asciinema.org/a/lM3uytLF8ccRC3QwIG6J6XWmD)

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/bvrn/konzertmeister-3g/issues) for a list of proposed features (and known
issues).

<!-- CONTRIBUTING -->

## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Dependency management

Python dependencies are managed via [Poetry](https://python-poetry.org/).

### Code quality

Various `git` [pre-commit](https://pre-commit.com/) hooks are in place to ensure code quality:

* Generic formatting and consistency checking.
* Sort Python imports via [`isort`](https://pycqa.github.io/isort/).
* Format Python code via [`black`](https://black.readthedocs.io/en/stable/).

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/bvrn/konzertmeister-3g](https://github.com/bvrn/konzertmeister-3g)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/bvrn/konzertmeister-3g.svg?style=for-the-badge

[contributors-url]: https://github.com/bvrn/konzertmeister-3g/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/bvrn/konzertmeister-3g.svg?style=for-the-badge

[forks-url]: https://github.com/bvrn/konzertmeister-3g/network/members

[stars-shield]: https://img.shields.io/github/stars/bvrn/konzertmeister-3g.svg?style=for-the-badge

[stars-url]: https://github.com/bvrn/konzertmeister-3g/stargazers

[issues-shield]: https://img.shields.io/github/issues/bvrn/konzertmeister-3g.svg?style=for-the-badge

[issues-url]: https://github.com/bvrn/konzertmeister-3g/issues

[license-shield]: https://img.shields.io/github/license/bvrn/konzertmeister-3g.svg?style=for-the-badge

[license-url]: LICENSE.txt

[product-screenshot]: images/screenshot.png
