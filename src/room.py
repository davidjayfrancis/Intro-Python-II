# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = False
        self.s_to = False
        self.w_to = False
        self.e_to = False
        self.items = []
        
    def __str__(self):
        return f"Room Name: {self.name} \nDescription: {self.description}"

    def addItem(self, name, description):
        self.items.append(Item(name, description))

    