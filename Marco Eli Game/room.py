import random

class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = ""
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def generate_next_room(self, direction):
        if direction not in self.linked_rooms:
            new_room = Room(f"Room {random.randint(1000, 9999)}")
            new_room.set_description("A mysterious, newly discovered chamber.")
            self.link_room(new_room, direction)
            opposites = {"north": "south", "south": "north", "east": "west", "west": "east"}
            if direction in opposites:
                new_room.link_room(self, opposites[direction])
            return new_room
        return self.linked_rooms[direction]

    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def set_name(self, room_name):
        self.name = room_name

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link