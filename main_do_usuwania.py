items = {
    "new notebook": {
        "description": "Notatnik, który zdaje się być prawie nieużywany. Została z niego wyrwana pierwsza kartka",
        #po użyciu ołówka: "usage": "alone"
        "usage": False,
        "takeable": True
    },
    "unindentified potion": {
        "description": "Napój, który kolorem przypomina whisky. Zdaje się mieć lecznicze właściwości [Podnosi hp o 20 punktów]",
        "usage": True,
        "special": True,
        "takeable": True
    },
    "pencil": {
        "description": "Mocno zużyty ołówek, a raczej jego reszta. Widnieją na nim ślady zębów",
        "usage": True,
        "special": True,
        "takeable": True
    },
    "pinpad": {
        "description": "Czytnik pin na 6 cyfr, z czego pierwsze dwa miejsca świecą się czerwono, dwa następne na zielono, a ostatnie na niebiesko",
        "usage": True,
        "special": True,
        "takeable": False
    },
    "safe": {
        "description": "No sejf jak sejf. Na 4 cyfry",
        "usage": True,
        "special": True,
        "takeable": False
    },
    "canvas": {
        "description": "Płótno z dziewczyną trzymającą różę. Za nim wydaje się nie być ściany. Możesz spróbować ją przeciąć",
        "usage": False,
        "special": True,
        "takeable": False
    },
    "newspaper": {
        "description": "Jakiś tekst z gazety. Podkreślony jest wrzesień",
        "usage": True,
        "special": False,
        "takeable": True
    },
    "closet": {
        "description": "Old lab coats. There's a <<death certificate>> inside it. ",
        "usage": False,
        "special": False,
        "takeable": False
    },
    "laptop": {
        "description": "Old laptop. It's working but moving the cursor or even trying to power off the machine doesn't seem to work.\nIt's showing a single photo of a young girl with blonde hair, blue eyes and a big smile. The file says 'Amber.jpg'",
        "usage": False,
        "special": False,
        "takeable": False
    },
    "window": {
        "description": "Pustka",
        "usage": False,
        "special": False,
        "takeable": False
    },
    "wall": {
        "description": "It says 'Beware of ligma'. You wonder what that means.",
        "usage": False,
        "special": False,
        "takeable": False
    },
    "floor": {
        "description": "5 petals are down.",
        "usage": False,
        "special": False,
        "takeable": False
    },
    "mirror": {
        "description": "You see yourself. You decide to touch it. \nIt shatters.\nNext thing you notice is your hands covered in blood.\nYou did this to yourself. All of it.\nYou deserve it.",
        "usage": False,
        "special": False,
        "takeable": False   
    }
}

inventory = []
player_health = 100
enemy_health = 100
current_location = "spawn"
endgame = False
canvas_state = False
vigenere = open("vigenere.txt", "r")
bed_examined = False
closet_examined = False

def print_inventory():
    print("Twój ekwipunek zawiera: ")
    for thing in inventory:
        print(thing)

def wrong_command():
    print("Nie możesz tego zrobić.")

def print_description(current_location):
    print(locations[current_location]["description"])

def check_room():
    global current_location
    if (direction == "close left"):
        if(check_inventory()):
            current_location = locations[current_location][direction]
        else:
            print("Coś mówi ci, że za tymi drzwiami czai się coś na co nie jesteś jeszcze gotowy")
    elif(direction == "close right"):
        if(check_inventory() and "unindentified potion" in inventory):
            current_location = locations[current_location][direction]
        else:
            print("Za tymi drzwiami kryje się coś, co może cię nieźle poturbować. Poszukaj czegoś do leczenia")
    else: 
        current_location = locations[current_location][direction]#asd

def check_inventory():
    if "knife" in inventory:
        return True

def look_around(current_location):
    print(locations[current_location]["look around"])

def check_item():
    global bed_examined
    global closet_examined
    item_definition()
    if (item in locations[current_location]["examinable"] and item != "bed" and item != "closet"):
        print(items[item]["description"])
    elif (item in locations[current_location]["examinable"] and item == "bed"):
        print(items[item]["description"])
        bed_examined = True
    elif (item in locations[current_location]["examinable"] and item == "closet"):
        print(items[item]["description"])
        closet_examined = True
    else:
        wrong_command()

def examine(current_location):
    print("Obecna lokalizacja to",current_location)
    if locations[current_location]["examinable"]:
        check_item()
    else:
        wrong_command()

def add_inventory(item):
    inventory.append(item)
    print("Wziąłeś",item)

def remove_item(item):
    locations[current_location]["examinable"][item] = False

def item_definition():
    global item
    item = " ".join(action[1:])

def take():
    item_definition()
    if (items[item]["takeable"]):
        if (item == "unindentified potion" or item == "newspaper"):
            if (canvas_state and item in locations[current_location]["examinable"] and locations[current_location]["examinable"][item]):
                add_inventory(item)        
                remove_item(item)
            else:
                wrong_command()

        elif (item == "knife"):
            if (bed_examined and item in locations[current_location]["examinable"] and locations[current_location]["examinable"][item]):
                add_inventory(item)        
                remove_item(item)  
            else:
                wrong_command()

        elif (item == "death certificate"):
            if (closet_examined and item in locations[current_location]["examinable"] and locations[current_location]["examinable"][item]):
                add_inventory(item)        
                remove_item(item)  
            else:
                wrong_command()

        elif (item in locations[current_location]["examinable"] and locations[current_location]["examinable"][item]):
            add_inventory(item)        
            remove_item(item)

        else:
            wrong_command()

    else:
        print("Nie możesz wziąć", item)

def use_item():
    if (item != "pencil" and items[item]["usage"]):
        print(items[item]["usage"])
    else:
        print("Nie możesz użyć",item)

def cut_canvas():
    global canvas_state
    print("Rozcinasz canvas\nZa nim znajdujesz wycinek z gazety oraz fiolkę z napojem wyglądającym jak whisky")
    canvas_state = "cut"

def use_special_item():
    if (item == "pencil"):
        if ("new notebook" in inventory):
            print("używasz",item,"na new notebook. Pojawia się tekst 'She is the absolute 0'")
        else:
            print("Nie masz na czym użyć",item)
    elif (item == "knife"):
        if (current_location == "middle_right"):
            cut_canvas()
        else:
            print("Nie masz na czym użyć noża")
    elif (item == "pinpad"):
        if (current_location == "door"):
            input_code()
        else:
            wrong_command()
    elif (item == "safe"):
        if(current_location == "middle_left"):
            input_code()
        else:
            wrong_command()
    elif (item == "vigenere note"):
        print(vigenere.read())
    else:
        print("Jakiś błąd, idk")

def ending(endgame, current_location):
    current_location = "mirror_room"
    print_description(current_location)
    while endgame != True:
        last_action = input("Co chcesz zrobić? \n\n").lower().split(" ")
        if (last_action[0] == "go"):
            print("there's nowhere to go now.\n\n")
        elif (" ".join(last_action) == "look around"):
            look_around(current_location)
        elif (last_action[0] == "inventory"):
            print("There's nothing in your inventory. In fact - there's no inventory to begin with. You can see your body but can't feel it nor touch it.\n\n")
        elif (last_action[0] == "help"):
            print("There's no help\n\n")
        elif (last_action[0] == "examine"):
            examine(current_location)
            endgame = True
        else:
            wrong_command()

    return endgame, current_location

def input_code():
    pin = input("Wpisz kod: ")
    if (current_location == "door"):
        if (pin == "12345678"):
            print("Dobry kod")
            ending(endgame, current_location)
        else:
            print("Zły kod")
    elif (current_location == "middle_left"):
        if (pin == "2137"):
            print("Dobry kod")
            open_safe()
        else:
            print("Zły kod")
    else:
        print("Bebebebe")

def open_safe():
    print("Sejf został otwarty. Znajdowała się w nim notatka.\nJest to tablica z alfabetem używana do odczytywania szyfru Vigenere'a")
    inventory.append("vigenere note")
    print("<<vigenere note>> dodana do ekwipunku")

def use():
    item_definition()
    if (items[item]["special"]):
        use_special_item()
    else:
        if (item in inventory):
            use_item()
        else:
            print("Nie masz",item,"w ekwipunku")

def death():
    print("Umarłeś. Ale jesteś znowu w korytarzu. Możesz walczyć jeszcze raz")
    #dodanie do ekwipunku potionki jeśli jej nie ma

    elif (" ".join(action) == "look around"):
        look_around(current_location)
    elif (action[0] == "examine"):
        examine(current_location)
    elif (action[0] == "take"):
        take()
    elif (action[0] == "use"):
        use()
    elif (action[0] == "inventory"):
        print_inventory()
    elif (action[0] == "help"):
        help()
    else:
        wrong_command()

if (player_health <= 0):
    death()

# co dodać: żeby tekst look around zmieniał się jeśli nie ma itemów do zebrania/jest mniej niż było
# dodać walki z potworkami
# dodać sekcję po exitcie
# komenda where am i? 
# zmienić globalne na parametry
# czemu przy examine mirror pokazuje mi czytnik pin...