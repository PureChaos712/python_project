from storage import movement_map, descriptions, inventory, items
import json

def check_for_monster(direction, inventory):
    if direction in movement_map and movement_map[direction].get("monster", False):
        if "knife" in inventory:
            return True
        else: 
            print("To enter this room you need some sort of a weapon")
            return False
    elif direction == "forward":
        return True
    else:
        return True

def handle_movement(current_location, direction, inventory):
    possible_movement = movement_map[current_location]

    if direction in possible_movement and direction == "back":
        current_location = possible_movement[direction]
        print(descriptions[current_location])
    elif direction in possible_movement:
        if check_for_monster(direction, inventory):
            current_location = possible_movement[direction]
            print(descriptions[current_location])
    else:
        print("Wrong location")#zmienić komunikat
    return(current_location)
    
def user_help():
    print("Commands you can use include:\n'go' + direction - to move\n'look around' - to check your surroundings\n'examine' + item - to check an item\n'take' + item - to take an item into your inventory\n'use' + item - to use item\n'inventory' - to check inventory\n'help' to check commands\n'quit' - to quit the game [progress will be saved]\n'reset game' - resets the game (sets all the variables back to default)")
    print("Items and directions you can use will be displayed in these brackets: <<item>>")

#system walki
#handler etapu w mirror room

def print_inventory():
    if inventory:
        print("In your inventory, there is: ")
        for thing in inventory:
            print(thing)
    else:
        print("Your inventory is empty")

def examine_item(item, current_location):
    if item in items:
        if items[item].get("take"):
            print("Nie masz w inventory tego czegos")
        else:
            if current_location == items[item].get("location") or item in inventory:
                print(items[item]["description"])
                items[item]["examined"] = True
            else:
                print("Pomyliłeś pokoje")


def take_item(item, current_location):
    if item in items:
        if current_location == items[item].get("location") and items[item].get("take"):
            items[item]["location"] = "inventory"
            items[item]["take"] = 0
            inventory.append(item)
            print(f"You take <<{item}>> with yourself")
        else:
            print("Nie możesz wziąć takiego przedmiotu")
    else:
        print("There's no such thing in this room")

def handle_special(item, current_location):
    if item == "knife":
        if current_location == "middle right":
            print(items[item].get("use"))
            items["canvas"]["state"] = "cut"
            items["unindentified potion"]["take"] = True
            items["newspaper"]["take"] = True
        else:
            print("You can't use it here")

    elif item == "pencil":
        if "pencil" in inventory and "new notebook" in inventory:
            items["new notebook"]["use"] = "Pod grafitem ołówka widać napis 'Nwm no coś widać I guess'"
            print(items["new notebook"]["use"])
        elif "pencil" not in inventory:
            print("Nie masz pencil w ekwipunku")
        else:
            print("Nie masz na czym użyć ołówka")

def use_potion(player_health):
    if player_health < 100:
        inventory.remove("unindentified potion")
        player_health += 20
        return (player_health, inventory)

#def handle_code()

def use_item (item, current_location):
    if item in items:
        if "special" in items[item]:
            if items[item].get("special") == "special":
                handle_special(item, current_location)
            elif items[item].get("special") == "input_code":
                input_code(item, current_location)
            elif items[item].get("special") == False and items[item].get("location") == current_location:
                print(items[item].get("use"))
            elif items[item].get("special") == False and items[item].get("location") == "inventory":
                print(items[item].get("use"))
            else:
                print("You can't do that dummy")
        elif "take" in items[item]:
            if items[item]["take"] and item in inventory:
                items[item].get("use")
        elif items[item].get("location") == current_location:
            items[item].get("use")
        else:
            print("WROOOONG Idk what tho")
    else:
        print("No such item")

def input_code(item, current_location):
    if items[item].get("location") == current_location or item in inventory:
        if items[item].get("take"):
            print("You should take it first")
        else:
            user_code = input(f"Input password for <<{item}>>: ")
            if user_code != items[item].get("code"):
                print("Incorrect password")
            else:
                items[item]["special"] = False
                print("You input the right code")
                if items[item]["use"] == "endgame":
                    print("AAAAAAAAAAAAA")
                else:
                    print(items[item]["use"])
    else:
        print("U can't do that, there's no such thing here")

def restart_game():
    file = open("savefile.txt", "w")
    file.write("1\n100\nspawn\n")

    save_file = open("items.txt", "w")
    load_file = open("backup_items.txt", "r")

    backup = json.load(load_file)
    json.dump(backup, save_file)
    save_file.close()
    load_file.close()

    save_file = open("movement_map.txt", "w")
    load_file = open("backup_movement_map.txt", "r")

    backup = json.load(load_file)
    json.dump(backup, save_file)
    save_file.close()
    load_file.close()
    print("Progress got reset. Start the game again")
