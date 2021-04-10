from sqlite3.dbapi2 import connect
from dotenv_manager.DataInterface import DataInterface
from pathlib import Path
import os
import sqlite3

class SQLiteData(DataInterface):

    def __init__(self):
        self.currentEnvironmentGroup = None
        self.cursor = None
        self.fileName = ".dotenv_manager"

    def setDatabaseFullPath(self, full_path: str):
        self.databaseFullPath = full_path
        self.connection = sqlite3.connect(self.getFullDatabasePath())
        self.cursor = self.connection.cursor()

    def exists(self):
        statement_search = "SELECT name FROM variable_group WHERE name = ?;"
        t = (self.currentEnvironmentGroup,)
        self.cursor.execute(statement_search, t)
        rows = self.cursor.fetchall()

        if len(rows) == 1:
            return True
        if len(rows) == 0:
            return False
        raise Exception("The result was unexpected.")

    def save(self):
        save_statement = "INSERT INTO "
        return True

    def environmentGroup(self, currentEnvironmentGroup):
        self.currentEnvironmentGroup = currentEnvironmentGroup
        return self

    def getFullDatabasePath(self):
        return self.databaseFullPath

    def getFileNameSuggestion(self):
        return ".dotenv_manager"

    def getFolderBaseSuggestion(self):
        return str(Path.home())

    def createDatabaseTables(self):
        
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
        self.cursor.execute(create_variable_table_statement)
        self.cursor.execute(create_variable_group_statements)
        self.cursor.execute(create_group_environment_table_statements)
        self.cursor.execute(create_table_templates_statements)
        return "created"



