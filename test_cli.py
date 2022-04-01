from mlib import load_df, get_closest
from cli import getclosestplayers
import pytest
from click.testing import CliRunner


@pytest.fixture(name="test_output")
def fixture_test_output():
    return "     NAME           TEAM      GP    PPG    RPG    APG\n---  -------------  ------  ----  -----  -----  -----\n452  Ja Morant      Mem       56   27.6    5.7    6.7\n141  Stephen Curry  Gol       64   25.5    5.2    6.3\n421  CJ McCollum    Nor       20   25.9    4.8    6.4\n217  Paul George    Lac       28   24.9    6.8    5.5\n174  Kevin Durant   Bro       50   29.6    7.3    6.2"


def test_load_df():
    assert load_df().shape == (703, 28)


def test_get_closest(test_output):
    assert get_closest(27, 7, 7) == test_output


def test_getclosestplayers(test_output):
    runner = CliRunner()
    result = runner.invoke(getclosestplayers, input="27\n7\n7\n")
    assert result.exit_code == 0
    assert len(result.output) == 431
