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
        sqliteData.createDatabaseTables()

        environmentGroupName = "my_environment"
        existsGroup = sqliteData.environmentGroup(environmentGroupName).exists()
        self.assertFalse(existsGroup)

    def test_save_environment_group(self):

        sqliteData = self.__getTemporarySqliteConnection()
        sqliteData.createDatabaseTables()

        environmentGroupName = "my_environment"
        sqliteData.environmentGroup(environmentGroupName).save()
        existsGroup = sqliteData.environmentGroup(environmentGroupName).exists()
        self.assertTrue(existsGroup)

    def test_not_existing_for_another_environment_group(self):
        sqliteData = self.__getTemporarySqliteConnection()
        sqliteData.createDatabaseTables()
        environmentGroupName = "my_environment"
        anotherEnvironmentGroup = "another_group"
        sqliteData.environmentGroup(environmentGroupName).save()
        existsGroup = sqliteData.environmentGroup(anotherEnvironmentGroup).exists()
        self.assertFalse(existsGroup)

    def test_save_already_existing_environment_group(self):
        environmentGroupNameTesting = "created_earlier"
        sqliteData = self.__getTemporarySqliteConnection()
        sqliteData.createDatabaseTables()
        sqliteData.environmentGroup(environmentGroupNameTesting).save()
        with self.assertRaises(Exception):
            sqliteData.environmentGroup(environmentGroupNameTesting).save()

    def test_return_string_creating_empty_database(self):
        sqliteData = self.__getTemporarySqliteConnection()
        responseCreated = sqliteData.createDatabaseTables()
        expectedResponse = "created"
        self.assertEqual(expectedResponse, responseCreated)

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
