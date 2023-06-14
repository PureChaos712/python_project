from functions import *
from storage import *

#wczytaj dane z pliku
endgame = False
file = open("savefile.txt", "r")
first_time = int(file.readline())
player_health = int(file.readline())
current_location = file.readline()[0:-1]#-1 bo zawierało \n
save_inventory = file.readline()

if save_inventory != "":
    if save_inventory:
        for item in save_inventory.split(" "):
            inventory.append(item)

file.close()

#Komunikat wyświetlający się na początku gry, jeśli nie była wcześniej zapisywana
if first_time:
    print("Welcome to a text-based escape room")
    user_help()
    print("You find yourself standing in a dark corridor. From here you can go \n         <<forward>>\n<<far left>>     <<far right>>\n<<middle left>>  <<middle right>>\n<<close left>>   <<close right>>")
else:
    print("You wake up. After a moment of confusion, you remember where you are. But you still don't know where 'here' even is.")
    print(f"You're currently in {current_location}\n")


while player_health > 0 and endgame == False:
    action = input("What do you want to do? ").lower()
    command = action.split(" ")[0] #akcja
    parameter = " ".join(action.split(" ")[1:]) #item

    if (command == "go"):
        current_location = handle_movement(current_location, parameter, inventory)

    elif (action == "help"):
        user_help()

    elif (action == "inventory"):
        print_inventory()

    elif (action == "look around"):
        print(detailed_descriptions[current_location]+"\n")

    elif (command == "examine"):
        examine_item(parameter, current_location)

    elif (command == "take"):
        take_item(parameter, current_location)




    elif (command == "use"):
        if parameter == "unindentified potion":
            player_health, inventory = use_potion(player_health)

        elif parameter == "pinpad":
            if current_location == "door":
                user_code = input(f"Input password for <<{parameter}>>: ")
                if user_code != "112233":
                    print("Incorrect password\n")
                else:
                    endgame = True
            else:
                print("U can't do that, there's no such thing here\n")
        else:
            use_item(parameter, current_location)






    elif (action == "where am i"):
        print(f"You are currently in {current_location}\n")

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

    elif (action == "reset game"):
        choice = input("Your whole progress will be reset. This may help you if you feel like the game files got corrupted. Are you sure you want to continue? y/n: ")
        if choice == "y":

            restart_game()
            break

        else:
            print("Progress won't be reset\n")

    else:
        print("Wrong command\n")

else:
    if endgame != False:
        print("Endgameee")
        
        current_location = "mirror room"
        print(descriptions[current_location]+"\n")
        
        while True:
            choice = input("What do you want to do?: ")

            if choice == "use mirror":
                print("enter final battle")
                break
            elif choice == "look around":
                print(detailed_descriptions[current_location]+"\n")
            elif choice == "inventory":
                print_inventory()
            elif choice == "help":
                print("\nThere's no help coming for you :)\n")
            elif choice == "go back":
                print("\nThere's no going back :)\n")
            elif choice == "examine mirror":
                examine_item("mirror", current_location)
            else:
                print("\nYou can't do that\n")

    elif player_health <= 0:
        print("U ded")
        
    else:
        print("Jakiś błąd")