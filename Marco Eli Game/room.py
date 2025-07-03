import random

class Room:
    def __init__(self, room_name):  # Initializes a room with a name
        self.name = room_name
        self.description = ""
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def generate_next_room(self, direction):  # Generates and links a new room in a given direction
        if direction not in self.linked_rooms:
            new_room = Room(f"Room {random.randint(1000, 9999)}")
            self.link_room(new_room, direction)
            opposites = {"north": "south", "south": "north", "east": "west", "west": "east"}
            if direction in opposites:
                new_room.link_room(self, opposites[direction])
            return new_room
        return self.linked_rooms[direction]

    def get_item(self):  # Returns the item in the room
        return self.item

    def set_item(self, item):  # Sets an item in the room
        self.item = item

    def set_character(self, character):  # Sets a character in the room
        self.character = character

    def get_character(self):  # Returns the character in the room
        return self.character

    def set_description(self, room_description):  # Sets the description of the room
        self.description = room_description

    def get_description(self):  # Returns the description of the room
        return self.description

    def get_name(self):  # Returns the name of the room
        return self.name

    def link_room(self, room_to_link, direction):  # Links another room in a specified direction
        self.linked_rooms[direction] = room_to_link