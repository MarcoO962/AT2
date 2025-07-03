chest_no = 0

class Chest():
    def __init__(self):
        self.id = "chest"+str(chest_no+1)
        self.description = ""
    def set_name(self, item_name):
        self.name = item_name
    def get_name(self):
        return self.name
    def set_description(self, item_description):
        self.description = item_description
    def get_character(self):
        return self.description
    def describe(self):
        print ("The [" + self.name + "] is here - " + self.description)

