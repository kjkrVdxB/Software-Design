from bash.interpreter.builtins.cd import Cd
from .executable_factory import ExecutableFactory


class CdFactory(ExecutableFactory):
    """
    Creates a cd command by the tokenized string.
    Checks that no arguments are passed except the command name.
    """
    def create_executable(self, tokenized):
        args = [token.get_string_with_normalized_quotes() for token in tokenized.to_list()]
        self.__check_args(args)

        command = Cd()
        command.set_args(args)
        return command

    def __check_args(self, args):
        if len(args) < 1 or args[0] != "cd":
            raise Exception("Invalid command format: cd.")
