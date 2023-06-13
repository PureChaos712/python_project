from functions import *
from storage import *

file = open("savefile.txt", "r")
first_time = int(file.readline())
player_health = int(file.readline())
current_location = file.readline()[0:-1]
save_inventory = file.readline()
print(save_inventory)
if save_inventory != "":
    if save_inventory:
        for item in save_inventory.split(" "):
            inventory.append(item)
else:
    print("Puste")
file.close()

if first_time:
    print("Welcome to a text-based escape room")
    user_help()
    print("You find yourself standing in a dark corridor. From here you can go \n         <<forward>>\n<<far left>>     <<far right>>\n<<middle left>>  <<middle right>>\n<<close left>>   <<close right>>")
else:
    print("As you awaken you sth sth")
    print("You're currently in",current_location)

while player_health > 0:
    action = input("What do you want to do? ").lower()
    command = action.split(" ")[0]
    parameter = " ".join(action.split(" ")[1:])

    if (command == "go"):
        current_location = handle_movement(current_location, parameter, inventory)

    elif (action == "help"):
        user_help()

    elif (action == "inventory"):
        print_inventory()

    elif (action == "look around"):
        print(detailed_descriptions[current_location])

    elif (command == "examine"):
        examine_item(parameter, current_location)

    elif (command == "take"):
        take_item(parameter, current_location)

    elif (command == "use"):

        if parameter == "unindentified potion":
            player_health, inventory = use_potion(player_health)

        else:
            use_item(parameter, current_location)

    elif (action == "where am i"):
        print(f"You are currently in {current_location}")

    elif (action == "quit"):
        file = open("savefile.txt", "w")
        
        file.write("0\n"+str(player_health)+"\n"+str(current_location)+"\n"+" ".join(inventory))

        file = open("items.txt", "w")
        json.dump(items, file)
        file.close()

        file = open("movement_map.txt", "w")
        json.dump(movement_map, file)
        file.close()
        
        print("Darkness surrounds you as you lose consciousness")
        break
    else:
        print("Wrong command")