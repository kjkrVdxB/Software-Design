import os

from ..command import Command


class Cd(Command):
    """
    A command to change current working directory. If no parameter is passed
    changes to user's home directory.
    """
    def execute(self):
        if len(self._args) > 2:
            raise Exception("Invalid argument number in cd. Found: " +
                            str(len(self._args)))

        os.chdir(os.path.expanduser('~') if len(self._args) == 1 else self._args[1])