class Dungeon:
    def __init__(self,  dungeon_name):
        self.name = dungeon_name
        self.description = ""
        self.linked_dungeons = {}
        self.character = None
        self.item = None
    
    def get_item(self):
        return self.item
    def set_item(self, item_name):
        self.item = item_name
    
    def set_character(self, dungeon_character):
        self.character = dungeon_character
    def get_character(self):
        return self.character
    
    def set_name(self, dungeon_name):
        self.name = dungeon_name
    def set_description(self, dungeon_description):
        self.description = dungeon_description
    def get_description(self):
        return self.description
    def get_name(self):
        return self.name
    
    def describe(self):
        print(self.description) 
    def link_dungeon(self, dungeon_to_link, direction):
        self.linked_dungeons[direction] = dungeon_to_link
    def get_details(self):
        print("The " + self.name)
        self.describe()
        for direction in self.linked_dungeons:
            dungeon = self.linked_dungeons[direction]
            print( "The " + dungeon.get_name() + " is " + direction)
        print("______________")
    def move(self, direction):
        if direction in self.linked_dungeons:
            return self.linked_dungeons[direction]
        else:
            print("You can't go that way")
            return self


