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

    def showMenu(self):
        self.log("Loading Menu...")
        self.clearConsole()
        self.log(" 1: New User")
        self.log(" 2: Draw membership fees")
        self.log(" 3: View finances")
        self.log(" 4: Exit")
        choice = self.prompt()
        return choice

    def mainLoop(self):
        choice = 0
        while choice != 4: # 4 = Exit
            choice = self.getMenuSelection()
            self.clearConsole()
            if choice == 1:
                # New Member
                self.createNewUser()
            if choice == 2:
                # Draw membership fees
                self.drawMembershipFees()
            if choice == 3:
                # View finances
                self.viewFinances()

    def getMenuSelection(self):
        choicestring = ""
        while True:
            try:
                choice = int(choicestring)
                if choice < 1:
                    raise TypeError()
                if choice > 4:
                    raise TypeError()
                break
            except TypeError:
                choicestring = self.showMenu()
            except ValueError:
                choicestring = self.showMenu()
        self.log("Selected Item " + str(choice))
        return choice

    def createNewUser(self):
        User()

    def drawMembershipFees(self):
        Bank.drawMembershipFees()

    def viewFinances(self):
        Bank.viewFinances()

# Execute main application.
Guild()
