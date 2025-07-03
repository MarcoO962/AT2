from room import room
from character import Enemy, Friend
from item import Item

roomrn = room("roomrn")
roomrn.set_description("A dank and dirty room ")
room = room("room")
room.set_description("A large room with a rack")
grotto = room("Grotto")
grotto.set_description("A small room with ancient graffiti")
roomrn.link_room(room, "south")
grotto.link_room(room, "east")
room.link_room(grotto, "west")
room.link_room(roomrn, "north")

vegemite = Item("vegemite")
vegemite.set_description("A Wumpuses worst nightmare")
grotto.set_item(vegemite)
torch = Item("torch")
torch.set_description("A light for the end of the tunnel")
room.set_item(torch)
bag = []

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.set_weakness("vegemite")
room.set_character(harry)
josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)


dead = False
current_room = roomrn          
while dead == False:	
    print("\n")         
    current_room.get_details()         
    item = current_room.get_item()
    if item is not None:
        item.describe()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")     
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)  
    elif command == "talk":
    # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Bravo,hero you won the fight!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")
                        dead = True

                else:
                    print("Scurry home, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you…")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_room.set_item(None)


        



