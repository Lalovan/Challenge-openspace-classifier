# CLASS OPENSPACE:
import random

from .table import Table

class Openspace:
    def __init__(self, number_of_tables: int) -> None:
        self.tables = [Table(4) for i in range(number_of_tables)]
        self.number_of_tables= 6

    def organize(self, names = None):
        
        if names is None:
            names = ["Aleksei","Amine","Anna","Astha","Brigitta",
                 "Bryan","Ena","Esra","Faranges","Frédéric",
                 "Hamideh","Héloïse","Imran","Intan K.",
                 "Jens","Kristin","Michiel","Nancy","Pierrick",
                 "Sandrine","Tim","Viktor","Welederufeal","Živile"]
        
        random.shuffle(names)
        
        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break

# this method has integrated the __str__ method, which is a separate method in Classes Seat and Table
    def display(self):
        for i, table in enumerate(self.tables, start = 1):
            print(f"\nTable {i}:")
            for seat in table.seats:
                if seat.free:
                    print("   [Empty]")
                else:
                    print(f"    {seat.occupant}")


    def store(self, filename):
        with open(filename, "w") as file: #Open a gile to write to
            for i, table in enumerate(self.tables, start = 1): #Go through each table and give it a number
                file.write(f"Table{i}:\n") #Write a header for the table
                for seat in table.seats: #Go through all seats at the table
                    if seat.free:
                        file.write("       [Empty]\n") #Writes "Empty" if free 
                    else:
                        file.write(f"  {seat.occupant}\n") #Writes occupant name if not free
                file.write("\n") #Adds a blank line between tables

    