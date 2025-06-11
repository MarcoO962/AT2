class Cave:
    def __init__(self,  cave_name):
        self.name = cave_name
        self.description = ""
        self.linked_caves = {}
    def set_description(self, cave_description):
        self.description = cave_description
    def get_description(self):
        return self.description
    def set_name(self, cave_name):
        self.name = cave_name
    def get_name(self):
        return self.name
    def describe(self):
        print(self.description)
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link
    def get_details(self):
        print("The " + self.name)
        self.describe()
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print( "The " + cave.get_name() + " is " + direction)
        print("______________")
    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self


