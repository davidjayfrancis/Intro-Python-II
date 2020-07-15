from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'ballroom': Room("Grand Ballroom", """You enter what was once a grand and glorious 
ballroom. You can only imagine the dances that were held here. Unfortunately, the room 
has been ransacked, and only rats crawl the musty expanse. You gaze around, but 
unfortunately do not see any doors except that from which you entered, to the East."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['ballroom']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add some items 
room['foyer'].addItem("Rusty sword", "It has not seen use in ages but will get the job done.")

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("What is your character's name? \n")
player = Player(player_name, room['outside'])
print(player)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def displayRoomItemsText(obj):
    for i in obj.items:
        print(f"You spy a {i.name}. {i.description}")

gameloop = True

while gameloop: 
    print(f"You enter the '{player.current_room.name}'. {player.current_room.description}")
    displayRoomItemsText(player.current_room)
    direction = input("Where would you like to go? (enter 'n', 'w', 's', 'e' to travel, or enter 'q' for quit)\n")

    if direction == 'n':
        if player.current_room.n_to:
            player.current_room = player.current_room.n_to
        else: 
            input("There's no room in that direction!!! Please try again or press 'q' for quit.\n")
    
    elif direction == 'w':
        if player.current_room.w_to:
            print("You leave the '{player.current_room}.'\n")
            player.current_room = player.current_room.w_to
        else: 
            input("There's no room in that direction!!! Please try again or press 'q' for quit.\n")

    elif direction == 'e':
        if player.current_room.e_to:
            player.current_room = player.current_room.e_to
        else: 
            input("There's no room in that direction!!! Please try again or press 'q' for quit.\n")

    elif direction == 's':
        if player.current_room.s_to:
            player.current_room = player.current_room.s_to
        else: 
            input("There's no room in that direction!!! Please try again ('n', 'e', 's', 'w') or press 'q' for quit.")

    elif direction == 'q':
        print(f"Thank you for playing, {name}, it's been a mighty quest!")
        gameloop = False




