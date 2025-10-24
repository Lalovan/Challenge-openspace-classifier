
class Seat:
    """" 
    This class is representing a single seat that can be occupied or not. 

    Attributes: 
        free (bool): It indicates whether the seat is free (True) or occupied (False).
        occupant (str): It is the name of the person currently occupying the seat, and empty string if the seat is free.

    Methods:
        set_occupant(name): It assigns a person if the seat is free.
        remove_occupant(): Frees the seat and returns the name of the previous occupant.
        __str__: It helps getting readable output for print(table), instead of <__main__.....>:. Example: "The seat is free."
       """
    def __init__(self) -> None:
        """
        It initializes a Seat object as free with no occupant.
        """
        self.free = True # True if seat is available, False if occupied
        self.occupant = "" # Name of the occupant; empty string if seat is free


    def set_occupant(self,name: str) -> None:
       """
       It allows the program to assign someone a seat if it is free.
        Parameters:
            name (str): Name of the person to occupy the seat.
        Prints a message indicating if the seat was successfully occupied
        or already taken.
       """
       if self.free:
            self.occupant = name # Sets the occupant object
            self.free = False # Marks the seat as occupied
            print(f"{name} is now occupying the seat.") #Indicates who is assigned to the seat
       else:
            print(f"The seat is occupied by {self.occupant}") # If already occupied, it indicates by whom
                
    
    def remove_occupant(self) -> str:
        """
        This method removes the current occupant from the seat and free it.
        Returns:
            str: Name of the person who was occupying the seat.
        Prints a message indicating, if the seat was freed or already free.
        """
        if not self.free:
            prev_occupant = self.occupant # Stores current occupant
            self.occupant = "" # Clears the seat
            self.free = True #Marks the seat as free
            print (f"{prev_occupant} just left and the seat is free.")
            return prev_occupant # Storing the name of the previous occupant #Returns previous occupants name
        else: 
            print("The seat is already free.") #It indicates, if the seat is already free


    def __str__(self):
         """
        It returns a readable string representation of the seat's current status (free or occupied). It prevents unreadable output such as <main.xxxx>, when using print(Seat).

        """
         result = "" # Generates the result string
         if self.free: # Checks if the seat is free or occupied and set the message accordingly
             result += "The seat is free."
         else:
            result += "The seat is occupied."
         return result # Returns the final status message       



class Table:

    """ 
    This class is representing a table with a fixed number of seats.

    Attributes:
        capacity(int): This is the total number of seats at the table. 
        seats(list of Seat): This is a list containing Seat objects, representing each seat.It is an instance attribute (
        each Table object has its own list of Seat objects) and not a parameter, and therefore, not included in the __init__parameter list below.
    Methods:
        has_free_spot(): Checks if at least one seat is free (once it finds a spot the loop breaks).
        assign_seat(name): Assigns a person to the first available seat.
        left_capacity(): Prints the number of free seats left.
        __str__ method helps getting readable output for print(table), instead of <__main__.....>:
        Example:

        Seat 1: Anna
        Seat 2: Zivile
        Seat 3: Nancy
        Seat 4: Victor
    """

    def __init__(self, capacity: int = 4): 
        """
        This method initializea a Table with a given number of seats, with a default option 4 seats per table.

        Parameters:
            capacity (int): The total number of seats to create for the table
        """
        self.capacity = capacity # Stores the total seats at the table
        self.seats = [Seat() for i in range(self.capacity)] # Create Seat objects

    def has_free_spot(self):
        """
        It checks if the table has at least one free seat. Once it finds it, the loop breaks.

        Returns:
            bool: True if there is a free seat, False otherwise.
        """
        for seat in self.seats: # Goes through the seats at the table
            if seat.free: 
                return True # Found at least one free seat
        return False # No free seat found 
            
    def assign_seat(self, name):
        """
        It assigns a person to the first available seat at the table.

        Parameters:
            name (str): Name of the person to assign to a seat.

        Prints a message if no more free seats are available. 
        """
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name) # Assign the person to this seat
                break
        else: 
            print("No more free seats.")

    def left_capacity(self):
        """
        It prints the number of free seats remaining at the table.
        """
        capacity = 0 #Creates an empty int, in order to store the number of free seats found by the loop
        for seat in self.seats: #Checking for free seats at the table
            if seat.free:
                capacity +=1 #Records the free seats it found.
        print(f"There are {capacity} free spots.")

    def __str__(self):
        """
        It returns a readable string representation of the table's current status (seats and occupants). 
        It prevents unreadable output such as <main.xxxx>, when using print(Table).

        Returns:
            str: A formatted string showing seat numbers and occupants.
        """
        result = "Table:\n" # Initializes the result string with a header
        for i, seat in enumerate(self.seats, start = 1): # Iterates over the seats with index starting from 1
            if seat.free:
                result += f"    Seat {i}: [Empty]\n" #If the seat is free, it displays as "[Empty]]
            else:
                result += f"    Seat {i}: {seat.occupant}\n" #If the seat is occupied, it displays the occupant's name
        return result
    