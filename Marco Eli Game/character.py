class Character:
    def __init__(self, char_name, char_description, hp=10):  # Initializes a character
        self.name = char_name
        self.description = char_description
        self.hp = hp


class Enemy(Character):
    def __init__(self, char_name, char_description, hp=10, damage=2):  # Initializes an enemy
        super().__init__(char_name, char_description, hp)
        self.damage = damage

    def attack(self, player):  # Enemy attacks the player and deals damage
        print(f"{self.name} attacks you for {self.damage} damage!")
        player.take_damage(self.damage)

    def take_damage(self, amount):  # Reduces enemy HP and checks for defeat
        self.hp -= amount
        print(f"{self.name} takes {amount} damage! ({self.hp} HP left)")
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")
            return True
        return False


class Player(Character):
    def __init__(self, name="Hero", hp=30):  # Initializes the player
        super().__init__(name, "The brave adventurer", hp)
        self.bag = []
        self.score = 0
        self.high_score = 0

    def take_damage(self, amount):  # Reduces player HP and checks for death
        self.hp -= amount
        print(f"You take {amount} damage! ({self.hp} HP left)")
        if self.hp <= 0:
            print("You have died!")
            return True
        return False

    def heal(self, amount):  # Increases player HP
        self.hp += amount
        print(f"You heal {amount} HP! ({self.hp} HP now)")

    def add_score(self, points):  # Adds points and updates high score
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score