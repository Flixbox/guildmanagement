import io
from datetime import datetime
from Database import Database
from Console import Console
from prettytable import PrettyTable

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
        table = PrettyTable([
            'Transaction ID',
            'User ID',
            'Name',
            'Amount',
            'Comment'
        ])
        transaction_history = self.database.execute_file(
            self.database.sql_folder +
            '//' +
            "get_transaction_history.sql")
        users = self.getUsers()
        self.clearConsole()
        cash = 0
        for t in transaction_history:
            user_id = t[1]
            fee = t[2]
            salutation = "Mr."
            first_name = "John"
            last_name = "Doe"
            # Search for user's name (Salutation + First name + Last name)
            for user in users:
                try:
                    if (int(user[0]) == user_id):
                        salutation = user[1]
                        first_name = user[2]
                        last_name = user[3]
                except:
                    pass # Something is up with the user ID > ignore
            table.add_row([
                t[0],
                user_id,
                salutation +
                ' ' +
                first_name +
                ' ' +
                last_name,
                str(fee),
                t[3]])
            try:
                cash = cash + float(fee)
            except:
                pass # If the fee is not a number, we'll just ignore it
        self.log(table)
        self.log("Balance: " + str(cash))
        self.prompt() # Wait for user input

    def drawMembershipFees(self):
        users = self.getUsers()
        for user in users:
            id = user[0] # User ID
            job = user[9] # User Job
            conditions = user[10] # User Conditions
            iban_user = user[11] # User IBAN
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

    def getUsers(self):
        return self.database.execute_file(
            self.database.sql_folder + '//' + "get_users.sql")