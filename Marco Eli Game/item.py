class Item:
    def __init__(self, item_name, damage=0):  # Initializes an item
        self.name = item_name
        self.description = ""
        self.damage = damage

    def get_name(self): # Returns the name of an item
        return self.name

    def set_description(self, item_description): # Sets the description of an item
        self.description = item_description 

    def get_damage(self): # Returns the name of an item
        return self.damage