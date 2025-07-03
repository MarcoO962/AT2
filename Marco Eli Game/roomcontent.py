import random
from character import Enemy
from item import Item
from gui import pen, screen, 

ENEMY_LIST = [
    ("Goblin", "A sneaky green creature", 8, 2),
    ("Orc", "A brutish warrior", 15, 4),
    ("Wumpus", "A mysterious beast", 12, 3),
    ("Skeleton", "A rattling pile of bones", 7, 2),
    ("Zombie", "A shambling corpse", 10, 2),
    ("Vampire", "A bloodthirsty fiend", 14, 5),
    ("Werewolf", "A savage beast", 16, 6),
    ("Bandit", "A greedy thief", 9, 3),
    ("Sorcerer", "A master of dark magic", 13, 5),
    ("Slime", "A sticky blob", 6, 1),
    ("Minotaur", "A bull-headed brute", 18, 7),
    ("Giant Spider", "A venomous arachnid", 11, 4),
    ("Troll", "A hulking monster", 20, 6),
    ("Ghost", "A spooky apparition", 8, 3),
    ("Imp", "A mischievous demon", 7, 2),
    ("Lich", "An undead sorcerer", 15, 6),
    ("Harpy", "A screeching bird-woman", 10, 3),
    ("Golem", "A creature of stone", 17, 5),
    ("Mimic", "A chest with teeth!", 12, 4),
    ("Dragonling", "A young but fierce dragon", 14, 7)
]

WEAPON_LIST = [
    ("Torch", 3),
    ("Vegemite", 5),
    ("Sword", 7),
    ("Dagger", 4),
    ("Potion", 0),
    ("Axe", 8),
    ("Mace", 6),
    ("Bow", 5),
    ("Crossbow", 6),
    ("Spear", 7),
    ("Magic Wand", 9),
    ("Fire Bomb", 10),
    ("Ice Staff", 8),
    ("Silver Knife", 6),
    ("Club", 4),
    ("Morning Star", 7),
    ("Halberd", 9),
    ("Scythe", 8),
    ("Whip", 5),
    ("Boomerang", 4)
]

def maybe_add_enemy(room):
    if random.random() < 0.5:
        name, desc, hp, dmg = random.choice(ENEMY_LIST)
        enemy = Enemy(name, desc, hp=hp, damage=dmg)
        room.set_character(enemy)

def maybe_add_item(room):
    if random.random() < 0.5:
        name, dmg = random.choice(WEAPON_LIST)
        item = Item(name, dmg)
        item.set_description(f"A {name.lower()} with {dmg} damage.")
        room.set_item(item)