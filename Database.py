import os
import io
import sqlite3

sql_init_folder = 'sql_init'
sql_edit_folder = 'sql_edit'

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

    # Execute a single sql file with arguments.
    def _execute_file(self, location, args):
        print("Executing file " + location + " with arguments " + str(args))
        with open(sql_edit_folder + '//' + location, 'r') as myfile:
            data = myfile.read().replace('\n', ' ')
        return self._execute(data, args)

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
