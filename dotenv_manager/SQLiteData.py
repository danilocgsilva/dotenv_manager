from sqlite3.dbapi2 import connect
from dotenv_manager.DataInterface import DataInterface
from pathlib import Path
import os
import sqlite3

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

    def createDatabaseTables(self):
        connection = sqlite3.connect(self.getDatabasePath())
        create_table_statement = """
CREATE TABLE variables (
    id integer PRIMARY KEY,
    name text NOT NULL,
    value text NOT NULL,
    variable_group INT,
    group_id INT
);
"""
        cursor = connection.cursor()
        cursor.execute(create_table_statement)



