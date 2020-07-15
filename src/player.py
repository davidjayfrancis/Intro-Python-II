# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    
    
    def __str__(self):
        return self.name

    def addItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)
    
    def listInventory(self):
        print(f"Number of items in inventory: {len(self.items)}")
        for i in self.items: 
            print(f"Name: {i.name} | Description: {i.description}\n\n")
            
