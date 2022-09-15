from click.testing import CliRunner
from {{cookiecutter.package_name}}.cli import cli


def test_dummy():
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0
