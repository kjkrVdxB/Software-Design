from os import listdir

from ..command import Command


class Ls(Command):
    """
    A command to list directory's contents. If no parameter is passed, lists
    contents of current working directory.
    """
    def execute(self):
        if len(self._args) > 2:
            raise Exception("Invalid argument number in ls. Found: " +
                            str(len(self._args)))

        path = '.' if len(self._args) == 1 else self._args[1]
        self._output_channel.write(' '.join(listdir(path)) + '\n')