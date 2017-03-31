import io
from datetime import datetime
from Database import Database
from Console import Console

# Class for our project.
# Created by Felix Tietjen on 16-Mar-2017
class User(Console):

    database = None
    c = None

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

    def __init__(self):
        super().__init__()
        self.log("Loading User class...")
        # Initialise database.
        self.database = Database()
        # Start new user creation
        self.createNewUser()

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