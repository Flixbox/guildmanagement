import os
import io
import sqlite3

sql_init_folder = 'sql_init'

# Database helper for our project.
# Created by Felix Tietjen on 09-Mar-2017
class Database:

    connection = None

    def __init__(self):
        print("Loading Database...")
        self.connection = sqlite3.connect('database.db')
        # Executes every single sql file in the folder.
        for file in os.listdir(sql_init_folder):
            self.execute_file(file)

    # Execute a single sql file.
    def execute_file(self, location):
        print("Executing file " + location)
        c = self.connection.cursor()
        with open(sql_init_folder + '//' + location, 'r') as myfile:
            data = myfile.read().replace('\n', ' ')
        c.execute(data)
        self.connection.commit()

    # Close the sql connection, when the object is deleted.
    def __del__(self):
        self.connection.close()
