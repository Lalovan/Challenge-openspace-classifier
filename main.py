
import csv
"""Imports the built-in csv module to read CSV files in a structured way.
It allows us to read rows as dictionaries, lists, etc.
"""
from utils.openspace import Openspace
"""Imports the Openspace class from the "utils.openspace" module ("utils." indicates the folder where openspace.py is saved). 
This class manages the seating arrangement, tables, storing and displaying results.
"""
def load_names(new_colleagues):
    """
    Loads names of new colleagues from a CSV file.
    Parameters:
        new_colleagues (str): Path to a CSV file containing a 'name' column.
    Returns:
        list of str: A list of names read from the CSV file.
    
    Behavior:
        - Reads the CSV file using DictReader.
        - Extracts the value from the "name" column for each row.
        - Handles UTF-8 encoding to support special characters in names.
    """
    names = [] # Creates an empty list to store the names from the .csv file
    with open(new_colleagues, newline = "", encoding = "utf-8") as csvfile:  # Open the CSV file safely using a context manager; preventing line endings to convert as empty rows
        reader = csv.DictReader(csvfile) # Reads CSV rows as dictionaries
        for row in reader:
            names.append(row["name"]) # Extracts the 'name' column and add to the list
    return names

names = load_names("new_colleagues.csv") # Loads the names of new colleagues from a CSV file

openspace1 = Openspace() # Creates an Openspace object with 6 tables (by default)
openspace1.organize(names) # Randomly assigns the loaded names to seats in the open space
openspace1.display() # Prints the seating arrangement to the console
openspace1.store("output.csv") # Saves the seating arrangement to a file named "output.csv"
