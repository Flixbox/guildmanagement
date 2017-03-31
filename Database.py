import os
import io
import sqlite3

# Database helper for our project.
# Created by Felix Tietjen on 09-Mar-2017
class Database:

    sql_init_folder = 'sql_init'
    sql_folder = 'sql'

    connection = None

    def __init__(self):
        print("Loading Database...")
        self.connection = sqlite3.connect('database.db')
        # Executes every single sql file in the folder.
        for file in os.listdir(self.sql_init_folder):
            self.execute_file(self.sql_init_folder + '//' + file)

    # Execute a single sql file without arguments.
    def execute_file(self, location):
        print("Executing file " + location)
        c = self.connection.cursor()
        with open(location, 'r') as myfile:
            data = myfile.read().replace('\n', ' ')
        c.execute(data)
        data = c.fetchall()
        self.connection.commit()
        return data

    # Execute a single sql file with arguments.
    def _execute_file(self, location, args):
        print("Executing file " + location + " with arguments " + str(args))
        with open(location, 'r') as myfile:
            data = myfile.read().replace('\n', ' ')
        data = self._execute(data, args)
        self.connection.commit()
        return data

    # Executes a command with arguments.
    def _execute(self, command, args):
        # Executes an SQL command.
        c = self.connection.cursor()
        c.execute(command, args)
        data = c.fetchall()
        self.connection.commit()
        return data

    # Close the sql connection when the object is deleted.
    def __del__(self):
        self.connection.close()
