from storage import movement_map, descriptions, inventory, items
import json

#jeśli w pokoju jest potwór, to jeśli nie masz noża - zablokuj wejście
def check_for_monster(direction, inventory):
    if direction in movement_map and movement_map[direction].get("monster"):
        if "knife" in inventory:
            print("U fight the monster\n")
            return True
        else: 
            print("To enter this room you need some sort of a weapon\n")
            return False
    else:
        return True

#obsługa zmiany pokoju
def handle_movement(current_location, direction, inventory):
    possible_movement = movement_map[current_location]

    if direction in possible_movement:
        if check_for_monster(direction, inventory) or direction == "back" or direction == "forward":
            current_location = possible_movement[direction]
            print(descriptions[current_location]+"\n")
    else:
        print("You can't go that way\n")
    return(current_location)
    
def user_help():
    print("Commands you can use include:\n'go' + direction - to move\n'look around' - to check your surroundings\n'examine' + item - to check an item\n'take' + item - to take an item into your inventory\n'use' + item - to use item\n'inventory' - to check inventory\n'help' to check commands\n'quit' - to quit the game [progress will be saved]\n'reset game' - resets the game (sets all the variables back to default)")
    print("Items and directions you can use will be displayed in these brackets: <<item>>")

def print_inventory():
    if inventory:
        print("In your inventory, there is: ")
        for thing in inventory:
            print(thing)
    else:
        print("Your inventory is empty")
    print("\n")

def examine_item(item, current_location):
    if item in items:

        if items[item].get("take"):
            print(f"You don't have {item} in your inventory\n")

        #osobna obsługa specjalnych itemów
        elif item == "bed" and current_location == "middle left":
            print(items[item]["description"]+"\n")
            items["knife"]["description"] = "And old knife. Seems like it's been though a lot"
            items["knife"]["take"] = True

        elif item == "closet" and current_location == "middle left":
            print(items[item]["description"]+"\n")
            items["death certificate"]["description"] = "It appears to be a death certificate of a patient. At the top of the page you can see a text written with a blue pen 'Petal program - final case 09'"
            items["death certificate"]["take"] = True
            items["death certificate"]["use"] = "'Petal program - final case 09'. Wypis death certificate"

        else:
            if current_location == items[item].get("location") or item in inventory:
                if items[item]["description"]:
                    print(items[item]["description"]+"\n")
                else: 
                    print("You don't see it anywhere\n")
            else:
                print("You don't see it anywhere\n")
    else:
        print("You can't see it anywhere around\n")

def take_item(item, current_location):
    if item in items:
        if current_location == items[item].get("location") and items[item].get("take"):
            items[item]["location"] = "inventory"
            items[item]["take"] = 0
            inventory.append(item)
            print(f"You take <<{item}>> with yourself\n")
        else:
            print("You can't take this item\n")
    else:
        print("There's no such thing in this room\n")

###########

def use_potion(player_health):
    if player_health < 100:
        inventory.remove("unindentified potion")
        player_health += 20
        return(player_health, inventory)
    else:
        print("You hp is full\n")
        return(player_health, inventory)

def handle_special(item, current_location):
    if item == "knife" and item in inventory:
        if current_location == "middle right":
            print(items[item].get("use")+"\n")
            # items["canvas"]["state"] = "cut"
            items["unindentified potion"]["take"] = True
            items["unindentified potion"]["description"] = "Napój, który kolorem przypomina whisky. Zdaje się mieć lecznicze właściwości [Podnosi hp o 20 punktów]"
            items["newspaper"]["take"] = True
            items["newspaper"]["description"] = "Tekst z gazety. Napisano na nim dziecięcym pismem 143"
        else:
            print("You can't do that\n")

    elif item == "pencil":
        if "pencil" in inventory and "new notebook" in inventory:
            items["new notebook"]["use"] = "Pod grafitem ołówka widać napis '0325 for safe'"
            print(items["new notebook"]["use"]+"\n")
        elif "pencil" not in inventory:
            print("Nie masz pencil w ekwipunku\n")
        else:
            print("Nie masz na czym użyć ołówka\n")
    
    else:
        print("You can't do that\n")

def use_item (item, current_location):
    if item in items: #use vigenere note dodać
        if "special" in items[item]:
            if items[item].get("special") == "special":
                handle_special(item, current_location)
            elif items[item].get("special") == "input_code":
                input_code(item, current_location)
            elif items[item].get("special") == False and items[item].get("location") == current_location:
                print(items[item].get("use")+"\n")
            elif items[item].get("special") == False and items[item].get("location") == "inventory":
                print(items[item].get("use")+"\n")
            else:
                print("You can't do that dummy\n")
        elif "take" in items[item]:
            if item in inventory and "use" in items[item]:
                print(items[item].get("use")+"\n")
            else:
                print("You can't do that\n")
        elif items[item].get("location") == current_location:
            if "use" in items[item]:
                print(items[item].get("use", None)+"\n")
            else:
                print("You can't use this item\n")
        else:
            print("WROOOONG Idk what tho\n")
    else:
        print("No such item\n")

def input_code(item, current_location):
    if items[item].get("location") == current_location or item in inventory:
        if items[item].get("take"):
            print("You don't have it in your inventory\n")
        else:
            user_code = input(f"Input password for <<{item}>>: ")
            if user_code != items[item].get("code"):
                print("Incorrect password\n")
            else:
                items[item]["special"] = False
                print("You input the right code\n")
                if items[item].get("use") == "endgame":
                    print("AAAAAAAAAAAAA\n")
                elif item == "safe":
                    items["vigenere note"]["take"] = True
                    items["vigenere note"]["use"] = "plik"
                    print("You see a <<vigenere note>>")
                    items["vigenere note"]["description"] = "Notatka z tablicą służącą do odczytu szyfru Vigenere'a. Nad nią widnieje napis 'Jej imię'"
                    print(items["vigenere note"]["description"]+"\n")
                elif item == "diary":
                    items[item]["description"] = "You opened the lock of the diary"
                    items[item]["use"] = "98 in red"
                    print(items[item]["use"])
                elif item == "laptop":
                    items[item]["use"] = "Green 63"
                    print(items[item]["use"])
    else:
        print("U can't do that, there's no such thing here\n")

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
