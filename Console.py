import time
from datetime import datetime
import codecs
import os
import io
import sys
import locale
from Database import Database
import logging


class Console:
    f = None
    database = None

    def __init__(self):
        logging.basicConfig(filename='log.log',level=logging.INFO)
        self.clearConsole()
        self.log("Initializing console application...")
        # must always be unicode = utf-8
        self.log("Encoding is " + sys.stdin.encoding)

    def clearConsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(message)
        self.logToFile(str(message))

    def prompt(self):
        command = input(' > ')
        self.log(' > ' + command)
        return command

    def promptNonEmpty(self):
        command = ""
        while not bool(command.strip()): # Checks for empty string
            command = self.prompt()
        return command

    def logToFile(self, message):
        logging.info(self.getTime() + ': ' + message.rstrip())

    def getTime(self):
        return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def promptToContinue(self):
        self.log("Press any key to continue...")
        command = self.prompt()
