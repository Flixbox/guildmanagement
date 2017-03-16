import io
from Database import Database
from Console import Console
from Bank import Bank

# Class for our project.
# Created by Felix Tietjen on 16-Mar-2017
class User(Console):

    database = None
    c = None

    def __init__(self):
        super().__init__()
        self.log("Loading User class...")
        # Initialise database.
        self.database = Database()
        # Start new user creation
        self.createNewUser()

    def createNewUser(self):
        pass # do stuff here