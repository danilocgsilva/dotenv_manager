from dotenv_manager.DataInterface import DataInterface
from pathlib import Path
import os

class SQLiteData(DataInterface):

    def __init__(self):
        self.currentEnvironmentGroup = None

    def exists(self):
        return True

    def save(self):
        return True

    def environmentGroup(self, currentEnvironmentGroup):
        self.currentEnvironmentGroup = currentEnvironmentGroup

    def getDatabasePath(self):
        return os.path.join(str(Path.home()),  ".dotenv_manager")

