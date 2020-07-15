# implements an item class
# attributes are name and description

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def on_take(self, player):
        print(f"{player.name} picked up the {self.name}\n\n")