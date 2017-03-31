import io
from datetime import datetime
from Database import Database
from Console import Console

# User class for our project.
# Used for creating new users for the guild management system.
# Created by Felix Tietjen on 16-Mar-2017
class User(Console):

    database = None
    c = None

    # SQL variables.
    salutation = None
    firstname = None
    lastname = None
    street = None
    zipcode = None
    city = None
    country = None
    birthday = None
    job = None
    conditions = None
    iban = None
    created_at = None
    updated_at = None

    # Called when the class is first created.
    # Starts the new user creation method.
    def __init__(self):
        super().__init__()
        self.log("Loading User class...")
        # Initialise database.
        self.database = Database()
        # Launches the new user thing.
        self.createNewUser()

    # Asks the user to enter all relevant and irrelevant data.
    # The most important part are the conditions.
    # This has to be a number like 20.12 or 15.
    # Afterwards, everything is stored safely.
    # Uses our Database class.
    def createNewUser(self):
        self.clearConsole()
        self.log("Salutation: ")
        self.salutation = self.promptNonEmpty()
        self.log("First name: ")
        self.firstname = self.promptNonEmpty()
        self.log("Last name: ")
        self.lastname = self.promptNonEmpty()
        self.log("Street: ")
        self.street = self.promptNonEmpty()
        self.log("Zipcode: ")
        self.zipcode = self.promptNonEmpty()
        self.log("City: ")
        self.city = self.promptNonEmpty()
        self.log("Country: ")
        self.country = self.promptNonEmpty()
        self.log("Birthday: ")
        self.birthday = self.promptNonEmpty()
        self.log("Job: ")
        self.job = self.promptNonEmpty()
        self.log("Conditions (% off): ")
        self.conditions = self.promptNonEmpty()
        self.log("IBAN: ")
        self.iban = self.promptNonEmpty()

        # All the info is there, let's launch an SQL operation!
        # (We don't catch any exceptions.)
        result = self.database._execute_file(
            self.database.sql_folder + '//' + 'add_user.sql',
            (self.salutation,
            self.firstname,
            self.lastname,
            self.street,
            self.zipcode,
            self.city,
            self.country,
            self.birthday,
            self.job,
            self.conditions,
            self.iban,
            datetime.now(),
            datetime.now()))
        self.log(result)