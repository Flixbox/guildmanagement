import io
import sqlite3


# Database helper for our project.
# Created by Felix Tietjen on 09-Mar-2017
class Database:
    
    connection = None
    
    def __init__(self):
        print("Loading Database...")
        self.connection = sqlite3.connect('database.db')
        self.execute_file("sql//initialise_database.sql")

    def execute_file(self, location):
        print("Executing file " + location)
        c = self.connection.cursor()
        with open(location, 'r') as myfile:
            data = myfile.read().replace('\n', ' ')
        c.execute(data)
        self.connection.commit()

