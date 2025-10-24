
import random
""" Imports the built-in Python "random" module, which provides functions for generating 
random numbers and performing random operations. In this class, in method organize, it is used to shuffle the list of names 
before assigning them to seats, ensuring a random seating arrangement.
"""

from .table import Table
"""Imports the "Table" class from a module named "table" in the same package/folder (indicated by the dot '.').
This allows the Openspace class to create Table objects for its tables.
"""
class Openspace:
    """
This class represents an open space with multiple tables (6 by default), where each table has seats (4 by default).

    Attributes:
        tables (list of Table): List, containing Table objects in the open space.
        number_of_tables (int): Total number of tables in the open space.

    Methods:
        organize(names=None): Randomly assigns names to available seats across all tables.
        display(): Prints a readable view of the seating arrangement in the openspace.
        store(filename): Saves the seating arrangement to a text file.
    
    """
    def __init__(self, number_of_tables: int = 6) -> None:
        """
        It initializes an Openspace object with a specified number of tables (6 by default, if None).

        Parameters:
            number_of_tables (int): Number of tables to create in the open space.
        """
        self.tables = [Table() for i in range(number_of_tables)] # Creates a new Table object with seats (4 by default) for s many tables are in number_of_tables
        self.number_of_tables= number_of_tables #Stores the total number of tables that the user passes, or the default

    def organize(self, names = None):
        """
        It assigns names to available seats randomly across all tables.

        Parameters:
            names (list of str, optional): List of names to assign to seats. If None, a default list of names will be used.

        """
        
        if names is None: # Default list of names if none provided
            names = ["Aleksei","Amine","Anna","Astha","Brigitta",
                 "Bryan","Ena","Esra","Faranges","Frédéric",
                 "Hamideh","Héloïse","Imran","Intan K.",
                 "Jens","Kristin","Michiel","Nancy","Pierrick",
                 "Sandrine","Tim","Viktor","Welederufeal","Živile"]
        
        random.shuffle(names) # Randomizes the order of names
        
        for name in names: # Assigns each name to a free seat
            for table in self.tables:
                if table.has_free_spot(): # Checks if table has free seats
                    table.assign_seat(name)  #Assigns name to first available seat 
                    break #Breaks the loop in self.tables and moves to the next name in names  

    def display(self):
        """
        It prints a readable string of the seating arrangement for all tables and seats lists, with either occupant name of "[Empty]" if not occupied. 
        In claases Seat and Table, method __str__ is the equivalent of this one.
        It prevents unreadable output such as <main.xxxx>, when using print(Openspace).
        """
        for i, table in enumerate(self.tables, start = 1): #Iterates through each table in the list, and give it a number
            print(f"\nTable {i}:") #Prints a table header with a number
            for seat in table.seats: #Iterates through all seats at the table
                if seat.free:
                    print("   [Empty]") #Prints "Empty" if free 
                else:
                    print(f"    {seat.occupant}") #Prints the name of the occupant, if occupied


    def store(self, filename):
        """
        It saves the seating arrangement to a .txt file, which is later converted into .csv in main.py.
        It is similar to the display method, with the only difference this one stores the output in a file.

        Parameters:
            filename (str): Name of the file to save the seating arrangement.

        Behavior:
            - Writes each table and its seats to the file.
            - Marks free seats as "[Empty]" and occupied seats with occupant names.
            - Adds a blank line between tables for readability.
        """
        with open(filename, "w") as file: #Opens a file for writitng; re-writes with each script run
            for i, table in enumerate(self.tables, start = 1): #Iterates through each table in the list, and give it a number
                file.write(f"Table{i}:\n") #Writes a table header with a number
                for seat in table.seats: #Iterates through all seats at the table
                    if seat.free:
                        file.write("       [Empty]\n") #Writes "Empty" if free 
                    else:
                        file.write(f"  {seat.occupant}\n") #Writes occupant name if not free
                file.write("\n") #Adds a blank line between tables

    