from storage import movement_map, descriptions, inventory, items

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
    if direction in movement_map[current_location] and direction == "back":
        current_location = movement_map[current_location][direction]
        print(descriptions[current_location])
    elif direction in movement_map[current_location]:
        if check_for_monster(direction, inventory):
            current_location = movement_map[current_location][direction]
            print(descriptions[current_location])
    else:
        print("Wrong location")#zmienić komunikat
    return(current_location)
    
def user_help():
    print("Commands you can use include:\n'go' + direction - to move\n'look around' - to check your surroundings\n'examine' + item - to check an item\n'take' + item - to take an item into your inventory\n'use' + item - to use item\n'inventory' - to check inventory\n'help' to check commands\n'quit' - to quit the game [progress will be saved]")
    print("Items and directions you can use will be displayed in these brackets: <<item>>")

#go - uwzględnienie potwora i noża
#use - te co są w inventory i te co są specjalne
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
    try:
        if current_location == items[item].get("location"):
            print(items[item]["description"])
            items[item]["examined"] = True
        else:
            print("Pomyliłeś pokoje")
    except:
        print("There's no such thing in this room")

def take_item(item, current_location):
    if item in items:
        if current_location == items[item].get("location") and items[item].get("take"):
            items[item]["location"] = "inventory"
            inventory.append(item)
            print(f"You take <<{item}>> with yourself")
        else:
            print("Nie możesz wziąć takiego przedmiotu")
    else:
        print("There's no such thing in this room")
    # try:
    #     if current_location == items[item].get("location") and items[item].get("take"):
    #         items[item]["location"] = "inventory"
    #         inventory.append(item)
    #         print(f"You take <<{item}>> with yourself")
    #     else:
    #         print("Nie możesz wziąć takiego przedmiotu")
    # except:
    #     print("There's no such thing in this room")

def handle_special(item, current_location):
    if item == "knife":
        if current_location == "middle right":#add locarion behind canvas
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

    elif item == "diary":
        pass #po wpisaniu hasła - odblokuj i zmień wartość use

def use_potion(player_health):
    if player_health < 100:
        inventory.remove("unindentified potion")
        player_health += 20
        return (player_health, inventory)

#def handle_code()

def use_item (item, current_location):
    if "special" in items[item]:
        if items[item].get("special") == "special":
            handle_special(item, current_location)
        elif items[item].get("special") == "input_code":
            input_code(item)
    elif "take" in items[item]:
        if items[item]["take"] and item in inventory:
            items[item].get("use")
    elif items[item].get("location") == current_location:
        items[item].get("use")
    else:
        print("WROOOONG Idk what tho")

def input_code(item):
    user_code = input(f"Input password for <<{item}>>: ")
    if user_code != items[item].get("code"):
        print("Incorrect password")
    else:
        items[item]["examined"] = True
        print("You input the right code")