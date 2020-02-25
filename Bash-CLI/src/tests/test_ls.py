import os

from bash.interpreter.builtins.ls import Ls
from bash.interpreter.channels.io_channel import IOChannel


def test_ls_from_argument():
    command = Ls()
    output = IOChannel()
    command.set_args(["ls", "Bash-CLI/src/tests/data/"])
    command.set_output_channel(output)
    command.execute()

    expected = ["example.txt", "numbers.txt"]
    assert sorted(output.read().split()) == expected


def test_ls_current():
    command = Ls()
    output = IOChannel()
    prev = os.getcwd()
    os.chdir("Bash-CLI/src/tests/data/")
    command.set_args(["ls"])
    command.set_output_channel(output)
    command.execute()
    os.chdir(prev)

    expected = ["example.txt", "numbers.txt"]
    assert sorted(output.read().split()) == expected


def test_ls_to_stdout(capsys):
    command = Ls()
    command.set_args(["ls", "Bash-CLI/src/tests/data/"])
    command.execute()

    expected = ["example.txt", "numbers.txt"]
    captured = capsys.readouterr()
    assert sorted(captured.out.split()) == expected
