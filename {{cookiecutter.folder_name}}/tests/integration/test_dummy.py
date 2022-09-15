from click.testing import CliRunner


def test_dummy():
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0
