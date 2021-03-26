import sys
from dotenv_manager.InteractorException import InteractorException

class Interactor:

    def __init__(self):
        self.argument = self.__get_argument_force()

    def __get_argument_force(self):
        try:
            return self.__get_argument()
        except InteractorException:
            return None

    def __get_argument(self):
        try:
            return sys.argv[1]
        except IndexError:
            raise InteractorException("You should provides the first argument as a command.")
