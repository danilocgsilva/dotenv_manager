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
        self.columnNames = {
            "variables": "variables",
            "variable_group": "variable_group",
            "environment_group": "environment_group",
            "templates": "templates"
        }

    def setDatabaseFullPath(self, full_path: str):
        self.databaseFullPath = full_path
        self.connection = sqlite3.connect(self.getFullDatabasePath())
        self.cursor = self.connection.cursor()

    def exists(self):
        statement_search = "SELECT name FROM " + self.columnNames["environment_group"]  + " WHERE name = ?;"
        t = (self.currentEnvironmentGroup,)
        self.cursor.execute(statement_search, t)
        rows = self.cursor.fetchall()

        if len(rows) == 1:
            return True
        if len(rows) == 0:
            return False

        raise Exception("The result was unexpected.")

    def save(self):

        if self.__environmentGroupAlreadyExists(self.currentEnvironmentGroup):
            raise Exception("The environemnt group " + self.currentEnvironmentGroup + " already exists.")

        save_statement = "INSERT INTO " + self.columnNames["environment_group"] + " (name) VALUES ('" + self.currentEnvironmentGroup + "')"

        self.cursor.execute(save_statement)

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

    def countEnvironmentGroups(self):
        counting_query = "SELECT COUNT(name) as countingEnvironmentGroups FROM {environment_group};".format(environment_group = self.columnNames["environment_group"])
        self.cursor.execute(counting_query)
        resultsRows = self.cursor.fetchall()
        return resultsRows[0][0]

    def createDatabaseTables(self):
        
        create_variable_table_statement = """
CREATE TABLE {table_name} (
    id integer PRIMARY KEY,
    name text NOT NULL,
    value text NOT NULL,
    variable_group INT,
    group_id INT,
    template_id INT
);"""
        create_variable_group_statements = """CREATE TABLE {table_name} (
    id integer PRIMARY KEY
);"""
        create_environment_group_table_statements = """CREATE TABLE {table_name} (
    id integer PRIMARY KEY,
    name text NOT NULL
);"""
        create_table_templates_statements = """CREATE TABLE {table_name} (
    id integer PRIMARY KEY,
    project_name text NOT NULL
)
"""
        self.cursor.execute(create_variable_table_statement.format(table_name = self.columnNames["variables"]))
        self.cursor.execute(create_variable_group_statements.format(table_name = self.columnNames["variable_group"]))
        self.cursor.execute(create_environment_group_table_statements.format(table_name = self.columnNames["environment_group"]))
        self.cursor.execute(create_table_templates_statements.format(table_name = self.columnNames["templates"]))
        return "created"

    def __environmentGroupAlreadyExists(self, environmentGroupName):

        select_term = "SELECT name FROM {environment_group_name} WHERE name = ?;".format(environment_group_name = self.columnNames["environment_group"])
        filter_query = (environmentGroupName,)
        self.cursor.execute(select_term, filter_query)
        resultsRows = self.cursor.fetchall()
        if len(resultsRows) > 0:
            return True
        return False

