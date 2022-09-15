# Cookiecutter PyPackage

[![CI](https://github.com/rszamszur/cookiecutter-pypackage/actions/workflows/main.yml/badge.svg)](https://github.com/rszamszur/cookiecutter-pypackage/actions/workflows/main.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
![GitHub](https://img.shields.io/badge/license-MIT-blue)

---

**Example generated project**: [rszamszur/pypackage-example](https://github.com/rszamszur/pypackage-example)

---

Cookiecutter template for a Python package.

## Includes

* GitHub actions for CI
* Poetry package manager
* Makefile with targets for install, tests (unit, integration, metrics), image
* Root CLI implementation with tests (Click)
* Dockerfile
* Sphinx documentation
* Nix expressions for development environment, package and container image

## Quickstart

Install cookiecutter
```shell
pip install -U cookiecutter
```

Generate a Python project:
```shell
cookiecutter https://github.com/rszamszur/cookiecutter-pypackage.git
```

## Contributing
Questions, comments or improvements? Please create an issue on Github. I do my best to include every contribution proposed in any way that I can.

## License

[MIT](https://github.com/rszamszur/cookiecutter-pypackage/blob/master/LICENSE)
