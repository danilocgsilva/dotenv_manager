import abc

class DataInterface(abc.ABC):

    @abc.abstractclassmethod
    def exists(self) -> bool:
        pass

    @abc.abstractclassmethod
    def save(self):
        pass

    @abc.abstractclassmethod
    def environmentGroup(self, environmentGroupName: str):
        pass
