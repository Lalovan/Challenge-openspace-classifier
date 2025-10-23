
import csv
from utils.openspace import Openspace

def load_names(new_colleagues):
    names = []
    with open(new_colleagues, newline = "", encoding = "utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names.append(row["name"])
    return names

names = load_names("new_colleagues.csv")

office = Openspace(6)
office.organize(names)
office.display()
office.store("output.csv")
