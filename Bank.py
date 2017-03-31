import io
from datetime import datetime
from Database import Database
from Console import Console
from prettytable import PrettyTable

# Bank class for our project.
# Organizes our finances.
# Created by Felix Tietjen on 09-Mar-2017
class Bank(Console):

    iban_bank = "DE 8937 0400 4405 3201 3000"
    # Strips spaces.
    iban_bank_stripped = iban_bank.replace(" ", "")

    # Default fees for all users.
    fees = 15

    database = None
    c = None

    # Called when the class is first created.
    def __init__(self):
        super().__init__()
        self.log("Loading Bank class...")
        # Initialise database.
        self.database = Database()

    # Shows a complete financial overview of all transactions.
    # Loads a pretty table.
    # Also shows our current balance.
    # Uses our Database class.
    def viewFinances(self):
        table = PrettyTable([
            'Transaction ID',
            'User ID',
            'Name',
            'Amount',
            'Comment',
            'From IBAN',
            'To IBAN',
            'Time'
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
                t[3], # Comment
                t[4], # From IBAN
                t[5], # To IBAN
                t[6]]) # Datetime Created (Updated is unnecessary)
            try:
                cash = cash + float(fee)
            except:
                pass # If the fee is not a number, we'll just ignore it
        self.log(table)
        self.log("Balance: " + str(cash))
        self.prompt() # Wait for user input

    # Draws in all membership fees, regardless of time.
    # Every user loses money according to their conditions.
    # We don't care about jobs or age.
    # Uses our Database class.
    def drawMembershipFees(self):
        # Get all users.
        users = self.getUsers()
        # Check all the users.
        for user in users:
            id = user[0] # User ID
            job = user[9] # User Job
            conditions = user[10] # User Conditions
            iban_user = user[11] # User IBAN

            # It's easier to ask for forgiveness than for permission
            try:
                # Try to calculate how much the user has to pay.
                value = self.fees - ( self.fees * int(conditions) / 100 )
            except ValueError:
                # If we fail, we will just go with the standard.
                # This happens when someone fills in incorrect data like "Hi".
                self.log("User " + id + " has the wrong conditions. No discount applied.")
                # We won't fix that data, we'll just ignore it.
                value = self.fees

            # Execute the whole thing.
            # We don't catch this if it goes wrong.
            result = self.database._execute_file(
                self.database.sql_folder + '//' + 'add_transaction.sql',
                (id,
                value,
                "Fees",
                iban_user,
                self.iban_bank_stripped,
                datetime.now(),
                datetime.now()))
            self.log("User " + str(id) + ": Fees of " + str(value) + " successfully withdrawn.")
        self.prompt() # Wait for user input

    # Returns all user info.
    # Uses our Database class.
    def getUsers(self):
        return self.database.execute_file(
            self.database.sql_folder + '//' + "get_users.sql")