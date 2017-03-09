'''
Database helper for our project.
Created by Felix Tietjen on 09-Mar-2017
'''


import io
import sqlite3

class Database:
    connection = None
    
    def __init__(self):
        print("Loading Database...")
        self.connection = sqlite3.connect('database.db')
        self.execute_file("sql//initialise_database.sql")

    def execute_file(self, location):
        print("Executing file " + location)
        

