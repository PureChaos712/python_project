from storage import movement_map, descriptions, inventory, detailed_descriptions, items

#czy w słowniku mogą być obiekty - jeśli tak, to tworzyć 2 klase - item i special item

def check_for_monster(direction, inventory):
    if movement_map[direction].get("monster", False): #zły klucz, nie działa back
        if "knife" in inventory:
            return True
        else: 
            print("Pobije cie")
            return False
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
    try:
        if current_location == items[item].get("location") and items[item].get("take"):
            items[item]["location"] = "inventory"
            inventory.append(item)
            print(f"You take <<{item}>> with yourself")
        else:
            print("Nie możesz wziąć takiego przedmiotu")
    except:
        print("There's no such thing in this room")

def handle_special(item, current_location, player_health):
    if item == "knife" and current_location == "middle right":#add locarion behind canvas
        print(items[item].get("use"))
        items["canvas"]["state"] = "cut"
        items["unindentified potion"]["take"] = True
        items["newspaper"]["take"] = True

    elif item == "pencil":
        if "pencil" in inventory and "new notebook" in inventory:
            items["new notebook"]["use"] = "Pod grafitem ołówka widać napis 'Nwm no coś widać I guess'"
            print(items["new notebook"]["use"])
        elif "pencil" not in inventory:
            print("Nie masz pencil w ekwipunku")
        else:
            print("Nie masz na czym użyć ołówka")
    elif item == "unindentified potion":
        if player_health < 100:
            inventory.pop(item)
            player_health += 20
            return (player_health)
    elif item == "diary":
        pass #po wpisaniu hasła - odblokuj i zmień wartość use

#def handle_code()

def use_item (item, current_location, player_health):
    if items[item].get("special"):
        handle_special(item, current_location, player_health)
    else:
        if items[item]["take"] and item in inventory:
            items[item].get("use")
        elif items[item].get("location") == current_location:
            items[item].get("use")
        else:
            print("WROOOONG Idk what tho")

    
# def use_item(item, current_location):
#     if item in inventory and not items[item]["state"]:
#         print(items[item].get("use"))
#             #canvas cut flag        
#     elif items[item]["use"] and item in inventory:
#         print(items[item].get("use", "You can't use this item"))
#     elif current_location == items[item].get("location"):
#         print(items[item].get("use", "You can't use this item v2"))
#     else:
#         print("Coś innego się stało")
