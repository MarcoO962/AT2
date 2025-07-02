from character import Enemy
harry = Enemy("Harry", "A smelly Wumpus")

harry.describe()
harry.set_weakness("vegemite")

print("What will you fight with?")
fight_with = input()
harry.fight(fight_with)





