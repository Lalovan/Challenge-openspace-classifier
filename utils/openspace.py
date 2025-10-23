# CLASS OPENSPACE:
from table import Table
import random

class Openspace:
    def __init__(self, number_of_tables: int) -> None:
        self.tables = [Table(4) for i in range(number_of_tables)]
        self.number_of_tables= 6

    def organize(self, names = None):
        import random
        
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

    def display(self):
        for i, table in enumerate(self.tables, start = 1):
            print(f"Table {i}:")
            for seat in table.seats:
                print("  ", seat.occupant or "Empty")
            print()


    def store(self,filename):
        with open(filename, "w") as file:
            for i, table in enumerate(self.tables, start = 1):
                file.write(f"Table{i}:\n")
                for seat in table.seats:
                    file.write(f"  {seat.occupant or "Empty"}\n")
                file.write("\n")

    