import io
from datetime import datetime
from Database import Database
from Console import Console

# Main class for our project.
# Created by Felix Tietjen on 09-Mar-2017
class Bank(Console):

    iban_bank = "DE 8937 0400 4405 3201 3000"
    iban_bank_stripped = iban_bank.replace(" ", "")
    fees = 15

    database = None
    c = None

    def __init__(self):
        super().__init__()
        self.log("Loading Bank class...")
        # Initialise database.
        self.database = Database()

    def viewFinances(self):
        pass # do stuff here

    def drawMembershipFees(self):
        users = self.database.execute_file(self.database.sql_folder + '//' + "get_users.sql")
        self.log(str(users))
        for user in users:
            id = user[1] # User ID
            job = user[10] # User Job
            conditions = user[11] # User Conditions
            iban_user = user[12] # User IBAN
            # It's easier to ask for forgiveness than for permission
            try:
                value = self.fees - ( self.fees * int(conditions) / 100 )
            except ValueError:
                self.log("User " + id + " has the wrong conditions. No discount applied.")
                # TODO fix data
                value = self.fees
            result = self.database._execute_file(
                self.database.sql_folder + '//' + 'add_transaction.sql',
                (id,
                value,
                "Membership fees for this user",
                iban_user,
                self.iban_bank_stripped,
                datetime.now(),
                datetime.now()))
            self.log("User " + str(id) + ": Fees of " + str(value) + " successfully withdrawn.")
        self.prompt() # Wait for user input