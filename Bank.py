import io
from Database import Database
from Console import Console
from User import User
from Bank import Bank

# Main class for our project.
# Created by Felix Tietjen on 09-Mar-2017
class Guild(Console):

    database = None
    c = None

    def __init__(self):
        super().__init__()
        self.log("Loading application...")
        # Initialise database.
        self.database = Database()
        self.mainLoop()