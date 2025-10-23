
# CLASS SEAT:
class Seat:
    """" 
    Attributes:
    Methods:
       """
    def __init__(self) -> None:
        self.free = True
        self.occupant = ""

#Function that allows the program to assign someone a seat if it is free.  

    def set_occupant(self,name: str) -> None:
        if self.free == True:
            self.occupant = name
            self.free = False
            print(f"{name} is occupying the seat.")
        else:
            print(f"The seat is occupied by {self.occupant}")
                
#Function that removes someone from a seat and return the name of the person occupying the seat before
    
    def remove_occupant(self) -> str:
        if self.free == False:
            prev_occupant = self.occupant
            self.occupant = "" 
            self.free = True
            print (f"{prev_occupant} just left and the seat is free.")
            return prev_occupant # storing the name of the previous occupant
        else: 
            print("The seat is already free.")
        

# CLASS TABLE:

class Table:

    """ DESCRIPTION"""

    def __init__(self, capacity: int): 
       self.capacity = 4
       self.seats = [Seat() for i in range(capacity)]

    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
        return False
            
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break
        #random shuffle?
        else: 
            print("No more free seats.")


    def left_capacity(self):
        capacity = 0
        for seat in self.seats:
            if seat.free:
                capacity +=1
        print(f"There are {capacity} free spots.")