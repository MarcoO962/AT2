class Item:
    def __init__(self, item_name, damage=0):
        self.name = item_name
        self.description = ""
        self.damage = damage

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, item_description):
        self.description = item_description

    def get_damage(self):
        return self.damage