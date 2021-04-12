from dotenv_manager.SQLiteData import SQLiteData
import os

class TaskManage:

    def __init__(self, manageCommand: str):
        if manageCommand == ":":
            self.__manageDoubleDot()

    def __manageDoubleDot(self):
        sqliteData = SQLiteData()

        databaseFullPath = os.path.join(
            sqliteData.getFolderBaseSuggestion(),
            sqliteData.getFileNameSuggestion()
        )

        sqliteData.setDatabaseFullPath(databaseFullPath)
        
        if sqliteData.countEnvironmentGroups() == 0:
            print("There still no environment groups registered.")
        else:
            print("Implement real data.")
