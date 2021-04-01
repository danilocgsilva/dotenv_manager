import unittest 
from dotenv_manager.SQLiteData import SQLiteData
from pathlib import Path
import os

class test_SQLiteData(unittest.TestCase):

    def test_not_exists_environment_group(self):

        sqliteData = SQLiteData()

        environmentGroupName = "my_environment"
        existsGroup = sqliteData.environmentGroup(environmentGroupName).exists()
        self.assertFalse(existsGroup)

    def test_save_environment_group(self):

        sqliteData = SQLiteData()

        environmentGroupName = "my_environment"
        sqliteData.environmentGroup(environmentGroupName).save()
        existsGroup = sqliteData.environmentGroup(environmentGroupName).exists()
        self.assertTrue(existsGroup)

    def test_correct_path_for_sqlite(self):

        sqliteData = SQLiteData()

        databaseName = ".dotenv_manager"

        expected_path = os.path.join(str(Path.home()), databaseName)
        object_path = sqliteData.getDatabasePath()
        self.assertEqual(expected_path, object_path)
