from functions import *
from storage import *

file = open("savefile.txt", "r")
first_time = int(file.readline())
player_health = int(file.readline())

current_location = file.readline()[0:-1]

save_inventory = file.readline()
print(save_inventory)

if save_inventory != 0 and inventory:
    for item in save_inventory.split(" "):
        inventory.append(item)
    print(inventory)
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
    action = input("What do you want to do? ").lower().split(" ")
    if (action[0] == "go"):
        direction = " ".join(action[1:])
        current_location = handle_movement(current_location, direction, inventory)
    elif (" ".join(action) == "help"):
        user_help()
    elif (" ".join(action) == "inventory"):
        print_inventory()
    elif (" ".join(action) == "look around"):
        print(detailed_descriptions[current_location])
    elif (action[0] == "examine"):
        item = " ".join(action[1:])
        examine_item(item, current_location)
    elif (action[0] == "take"):
        item = " ".join(action[1:])
        take_item(item, current_location)
    elif (action[0] == "use"):
        item = " ".join(action[1:])
        if item == "unindentified potion":
            player_health, inventory = use_potion(player_health)
        else:
            use_item(item, current_location, player_health)
    elif (" ".join(action) == "where am i"):
        print(f"You are currently in {current_location}")
    elif (" ".join(action) == "quit"):
        file = open("savefile.txt", "w")
        # if inventory:
        file.write("0\n"+str(player_health)+"\n"+str(current_location)+"\n"+" ".join(inventory))
        # else:
        #     file.write("0\n"+str(player_health)+"\n"+str(current_location)+"\n0")
        print("Darkness surrounds you as you lose consciousness")
        break
    else:
        print("Wrong command")