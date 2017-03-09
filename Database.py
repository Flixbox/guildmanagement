'''
Database helper for our project.
Created by Felix Tietjen on 09-Mar-2017
'''


import io
import sqlite3

class Database:
    def __init__(self):
        print("Loading Database...")
        connection = sqlite3.connect('database.db')
        

