import os
import sys
sys.path.insert(1, "..")
import unittest 
import tempfile
from dotenv_manager.SQLiteData import SQLiteData
from pathlib import Path
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers

class test_SQLiteData(unittest.TestCase):

    def test_not_exists_environment_group(self):

        sqliteData = self.__getTemporarySqliteConnection()

        environmentGroupName = "my_environment"
        existsGroup = sqliteData.environmentGroup(environmentGroupName).exists()
        self.assertFalse(existsGroup)

    def test_save_environment_group(self):

        sqliteData = self.__getTemporarySqliteConnection()

        environmentGroupName = "my_environment"
        sqliteData.environmentGroup(environmentGroupName).save()
        existsGroup = sqliteData.environmentGroup(environmentGroupName).exists()
        self.assertTrue(existsGroup)

    def test_not_existing_for_another_environment_group(self):
        sqliteData = self.__getTemporarySqliteConnection()
        environmentGroupName = "my_environment"
        anotherEnvironmentGroup = "another_group"
        sqliteData.environmentGroup(environmentGroupName).save()
        existsGroup = sqliteData.environmentGroup(anotherEnvironmentGroup).exists()
        self.assertFalse(existsGroup)

    def test_save_already_existing_environment_group(self):
        environmentGroupNameTesting = "created_earlier"
        sqliteData = self.__getTemporarySqliteConnection()
        sqliteData.environmentGroup(environmentGroupNameTesting).save()
        with self.assertRaises(Exception):
            sqliteData.environmentGroup(environmentGroupNameTesting).save()

    def test_getFileNameSuggestion(self):
        sqliteData = SQLiteData()
        self.assertEqual(".dotenv_manager", sqliteData.getFileNameSuggestion())

    def test_getFolderBaseSuggestion(self):
        sqlLiteData = SQLiteData()
        self.assertEqual(str(Path.home()), sqlLiteData.getFolderBaseSuggestion())

    def test_correct_path_for_sqlite(self):

        sqliteData = SQLiteData()

        databaseName = ".dotenv_manager"

        fullDatabasePath = os.path.join(
            sqliteData.getFolderBaseSuggestion(),
            databaseName
        )

        sqliteData.setDatabaseFullPath(fullDatabasePath)

        expected_path = os.path.join(str(Path.home()), databaseName)

        object_path = sqliteData.getFullDatabasePath()
        self.assertEqual(expected_path, object_path)

    def test_countEnvironmentGroups(self):
        sqliteData = self.__prepareEmptySqliteObject()
        sqliteData.environmentGroup("EnvsFromProjectOne").save()
        sqliteData.environmentGroup("EnvsFromAnotherProject").save()
        sqliteData.environmentGroup("ThirdContainerVariables").save()
        self.assertEqual(3, sqliteData.countEnvironmentGroups())

    # def test_countEnvironmentGroups_exception_empty(self):
    #     sqliteData = SQLiteData()
    #     databaseFullPath = os.path.join(
    #         self.__makeTemporaryTestDir(),
    #         sqliteData.getFileNameSuggestion()
    #     )
    #     sqliteData.setDatabaseFullPath(databaseFullPath)

    #     environemnt_group = "my_working_vars"
    #     with self.assertRaises(Exception):
    #         sqliteData.countEnvironmentGroups()

    def test_countEnvironmentGroups_empty(self):
        sqliteData = SQLiteData()
        databaseFullPath = os.path.join(
            self.__makeTemporaryTestDir(),
            sqliteData.getFileNameSuggestion()
        )
        sqliteData.setDatabaseFullPath(databaseFullPath)

        environemnt_group = "my_working_vars"
        self.assertEqual(0, sqliteData.countEnvironmentGroups())
            

    def test_is_tables_created_true(self):
        sqliteData = SQLiteData()
        databaseFullPath = os.path.join(
            self.__makeTemporaryTestDir(),
            sqliteData.getFileNameSuggestion()
        )
        sqliteData.setDatabaseFullPath(databaseFullPath)

        self.assertTrue(sqliteData.is_tables_created())

    def test_tuple_columnNames(self):
        sqliteData = self.__getTemporarySqliteConnection()
        self.assertTrue(isinstance(sqliteData.columnNames, dict))

    def test_database_created_after_setting_path(self):
        sqliteData = SQLiteData()
        databaseFullPath = os.path.join(
            self.__makeTemporaryTestDir(),
            sqliteData.getFileNameSuggestion()
        )
        sqliteData.setDatabaseFullPath(databaseFullPath)
        self.assertTrue(sqliteData.is_tables_created())

    def __prepareEmptySqliteObject(self) -> SQLiteData:
        sqliteData = self.__getTemporarySqliteConnection()
        return sqliteData
    
    def __getTemporaryTestDir(self):
        dateHash = DcgsPythonHelpers().getHashDateFromDate()
        systemTemporaryLocation = tempfile.gettempdir()
        fullPath = os.path.join(systemTemporaryLocation, "dotenv_manager_unit_test-" + dateHash)
        
        loopCurrent = 1
        while os.path.exists(fullPath):
            fullPath = fullPath + "-" + str(loopCurrent)
            loopCurrent += 1
        return fullPath

    def __makeTemporaryTestDir(self):
        temporaryDir = self.__getTemporaryTestDir()
        os.makedirs(temporaryDir)
        return temporaryDir

    def __getTemporarySqliteConnection(self):
        temporary_directory = self.__makeTemporaryTestDir()
        sqliteData = SQLiteData()   
        temporary_full_path_sqlite_file = os.path.join(
            temporary_directory,
            sqliteData.getFileNameSuggestion()
        )
        sqliteData.setDatabaseFullPath(temporary_full_path_sqlite_file)
        return sqliteData

if __name__ == '__main__':
    unittest.main()
