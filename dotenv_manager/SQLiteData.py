from sqlite3.dbapi2 import connect
from dotenv_manager.DataInterface import DataInterface
from pathlib import Path
import os
import sqlite3

class SQLiteData(DataInterface):

    def __init__(self):
        self.currentEnvironmentGroup = None
        self.fileName = ".dotenv_manager"
        self.basePath = str(Path.home())

    def exists(self):
        return True

    def save(self):
        return True

    def environmentGroup(self, currentEnvironmentGroup):
        self.currentEnvironmentGroup = currentEnvironmentGroup

    def getFullDatabasePath(self):
        return os.path.join(self.basePath, self.fileName)

    def createDatabaseTables(self):
        connection = sqlite3.connect(self.getFullDatabasePath())

        create_variable_table_statement = """
CREATE TABLE variables (
    id integer PRIMARY KEY,
    name text NOT NULL,
    value text NOT NULL,
    variable_group INT,
    group_id INT,
    template_id INT
);"""
        create_variable_group_statements = """CREATE TABLE variable_group (
    id integer PRIMARY KEY
);"""
        create_group_environment_table_statements = """CREATE TABLE group_environment (
    id integer PRIMARY KEY,
    name text NOT NULL
);"""
        create_table_templates_statements = """CREATE TABLE templates (
    id integer PRIMARY KEY,
    project_name text NOT NULL
)
"""
        cursor = connection.cursor()
        cursor.execute(create_variable_table_statement)
        cursor.execute(create_variable_group_statements)
        cursor.execute(create_group_environment_table_statements)
        cursor.execute(create_table_templates_statements)
        return "created"



