import os

from bash.interpreter.builtins.cd import Cd
from bash.interpreter.channels.io_channel import IOChannel


def test_cd_from_argument():
    command = Cd()
    output = IOChannel()
    prev = os.getcwd()
    command.set_args(["cd", "Bash-CLI/src/tests/data/"])
    command.set_output_channel(output)
    command.execute()

    assert os.getcwd() == os.path.normpath(prev + "/Bash-CLI/src/tests/data")

    os.chdir(prev)


def test_cd_home():
    command = Cd()
    output = IOChannel()
    prev = os.getcwd()
    command.set_args(["cd"])
    command.set_output_channel(output)
    command.execute()

    assert os.getcwd() == os.path.expanduser('~')

    os.chdir(prev)
