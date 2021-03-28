import abc

class CommandInterface(abc.ABC):
    @abc.abstractmethod
    def help(self):
        pass
