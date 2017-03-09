import io
from Database import Database
from Console import Console

# Main class for our project.
# Created by Felix Tietjen on 09-Mar-2017
class Guild:

    database = None
    c = None
    
    def __init__(self):
        print("Loading application...")
        self.c = Console()
        # Initialise database.
        self.database = Database()
        
        
# Execute main application.
Guild()
