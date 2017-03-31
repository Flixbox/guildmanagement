import io
from Database import Database
from Console import Console
from User import User
from Bank import Bank

# Main class for our project.
# Main menu that calls all of our methods and classes.
# Created by Felix Tietjen on 09-Mar-2017
class Guild(Console):

    database = None
    c = None

    # Called when the class is first created.
    # Starts the main loop.
    def __init__(self):
        super().__init__()
        self.log("Loading application...")
        # Initialise database.
        self.database = Database()
        self.mainLoop()

    # Shows the menu and returns the user's choice.
    def showMenu(self):
        self.log("Loading Menu...")
        self.clearConsole()
        self.log(" 1: New User")
        self.log(" 2: Draw membership fees")
        self.log(" 3: View finances")
        self.log(" 4: Exit")
        choice = self.prompt()
        return choice

    # The main loop of the program.
    # From here, all of the other methods and classes are launched.
    # This can be left by selecting Exit.
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

    # Checks for the user's selection in the menu.
    # If the user enters something invalid, the menu is displayed again.
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

    # Starts the agent that helps creating a new user.
    # Creates the class User.
    def createNewUser(self):
        User()

    # Starts the agent that helps drawing in membership fees.
    # Creates the class Bank and starts its method.
    def drawMembershipFees(self):
        Bank().drawMembershipFees()

    # Starts the agent that helps viewing our Finances.
    # Creates the class Bank and starts its method.
    def viewFinances(self):
        Bank().viewFinances()

# Execute main application.
Guild()
