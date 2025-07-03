from room import Room
from character import Player
from roomcontent import maybe_add_enemy, maybe_add_item

player = Player()
current_room = Room("Start Room")
maybe_add_enemy(current_room)
maybe_add_item(current_room)
dead = False

def show_room():
    print("\n" + "="*40)
    print(f"Location: {current_room.get_name()}")
    print(current_room.get_description())
    item = current_room.get_item()
    if item:
        print(f"Item here: {item.get_name()} - {item.description} (Damage: {item.get_damage()})")
    enemy = current_room.get_character()
    if enemy:
        print(f"Enemy here: {enemy.name} - {enemy.description} (HP: {enemy.hp}, Damage: {enemy.damage})")
    directions = list(current_room.linked_rooms.keys())
    if directions:
        print("Exits:", ", ".join(directions).upper())
    else:
        print("No exits yet. Try moving in any direction (north/south/east/west).")
    print("="*40)

def main_loop():
    global current_room, dead
    print("Welcome to the Endless Dungeon Crawler!")
    while not dead:
        show_room()
        print(f"Your HP: {player.hp} | Score: {player.score} | High Score: {player.high_score}")
        command = input("Command (north/south/east/west/take/fight/inventory/quit): ").strip().lower()
        if command in ["north", "south", "east", "west"]:
            enemy = current_room.get_character()
            if enemy:
                print(f"As you try to leave, {enemy.name} attacks you!")
                enemy.attack(player)
                if player.hp <= 0:
                    dead = True
                    continue  # Don't move if dead
            if not dead:
                next_room = current_room.generate_next_room(command)
                maybe_add_enemy(next_room)
                maybe_add_item(next_room)
                current_room = next_room
                print(f"You move {command}.")
        elif command == "take":
            enemy = current_room.get_character()
            if enemy:
                print(f"As you try to take the item, {enemy.name} attacks you!")
                enemy.attack(player)
                if player.hp <= 0:
                    dead = True
                    continue  # Don't take the item if dead
            if not dead:
                item = current_room.get_item()
                if item:
                    player.bag.append(item)
                    current_room.set_item(None)
                    print(f"You put the {item.get_name()} in your bag.")
                else:
                    print("There is nothing to take.")
        elif command == "fight":
            enemy = current_room.get_character()
            if enemy:
                if not player.bag:
                    print("You have nothing to fight with!")
                    continue
                print("Your bag:", ", ".join([i.get_name() for i in player.bag]))
                weapon_name = input("What will you fight with? (type item name): ").strip().lower()
                weapon = next((i for i in player.bag if i.get_name().lower() == weapon_name), None)
                if weapon:
                    print(f"You attack {enemy.name} with {weapon.get_name()} for {weapon.get_damage()} damage!")
                    defeated = enemy.take_damage(weapon.get_damage())
                    if defeated:
                        current_room.set_character(None)
                        print("Bravo, hero! You won the fight!")
                        player.add_score(10)
                    else:
                        enemy.attack(player)
                        if player.hp <= 0:
                            dead = True
                else:
                    print("You don't have that item.")
            else:
                print("There is no one here to fight with.")
        elif command == "inventory":
            if player.bag:
                print("Your bag:")
                for i in player.bag:
                    print(f"- {i.get_name()} (Damage: {i.get_damage()})")
            else:
                print("Your bag is empty.")
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command.")

    print(f"Game Over! Final Score: {player.score} | High Score: {player.high_score}")

if __name__ == "__main__":
    main_loop()