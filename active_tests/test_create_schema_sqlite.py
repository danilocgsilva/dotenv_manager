import sys
sys.path.insert(1, "..")
import sqlite3
from pathlib import Path
from dotenv_manager.SQLiteData import SQLiteData

sqliteData = SQLiteData()
try:
    sqliteData.createDatabaseTables()
    print("Database created successfully.")
except Exception as e:
    print("Error in creating database: " + str(e))
