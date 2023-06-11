import codecs

inventory = []

descriptions = {}
file = open("/home/weronika/Desktop/python_projekt/locations_descriptions.txt", "r")

for line in file:
    line = line.split(":")
    room = line[0]
    description = codecs.decode(line[-1], 'unicode_escape')
    descriptions[room] = description

file.close()

#
detailed_descriptions = {}
file = open("/home/weronika/Desktop/python_projekt/look_around.txt", "r")

for line in file:
    line = line.split(":")
    room = line[0]
    detailed_description = codecs.decode(line[-1], 'unicode_escape')
    detailed_descriptions[room] = detailed_description

file.close()


movement_map = {
    "spawn": {
        "close left": "close left",
        "middle left": "middle left",
        "far left": "far left",
        "close right": "close right",
        "middle right": "middle right",
        "far right": "far right",
        "forward": "door",
    },
    "close left": {
        "back": "spawn",
        "monster": "weak",
        "state": False,
    },
    "middle left": {
        "back": "spawn",
    },
    "far left": {
        "back": "spawn",
    },
    "close right": {
        "back": "spawn",
        "monster": "strong",
        "state": False
    },
    "middle right": {
        "back": "spawn",
    },
    "far right": {
        "back": "spawn",
    },
    "door": {
        "back": "spawn",
    },
    "mirror room": {
        "monster": "boss",
    },
}

items = {
    "bed": {
        "description": "Old bed. It's worn out and has yellow stains on it. The mattress reeks of alcohol. There's a <<knife>> under the pillow.",
        "location": "middle left",
        "take": False,
        "examined": False,
    },
    "knife": {
        "description": "Tępy nóż. Przeżył już swoje lata",
        "location": "middle left",
        "take": True,
        "use": "You use the knife on the canvas.",
        "special": True
    },
    "old notebook": {
        "description": "Zniszczony notatnik. Zdaje się, że za chwile rozpadnie się w twoich rękach",
        "location": "close left",
        "take": True,
        "use": "7 7 7 7 7"
    },
    "safe note": {
        "description": "Notatka, która wypadła z potwora w czerwonym lewym pokoju",
        "location": "close left",
        "take": True,
        "use": "2137",
    },
    "death certificate": {
        "description": "Notatka śmierci jednej z pacjentek. Widnieje na niej data 3.05. Rok został rozmazany",
        "location": "middle left",
        "take": True,
        "use": "Wypis death certificate",
        "state": False
    },
    "vigenere note": {
        "description": "Notatka z tablicą służącą do odczytu szyfru Vigenere'a. Nad nią widnieje napis 'Jej imię'",
        "location": "middle left",
        "take": True,
        "use": "pliczek",
        "state": False
    },
    "new notebook": {
        "description": "Notatnik, który zdaje się być prawie nieużywany. Została z niego wyrwana pierwsza kartka",
        "location": "close right",
        "take": True,
        "use": False,
    },
    "unindentified potion": {
        "description": "Napój, który kolorem przypomina whisky. Zdaje się mieć lecznicze właściwości [Podnosi hp o 20 punktów]",
        "location": "middle right",
        "take": False,
        "use": "Your hp is now 20 hp higher",
        "state": False
    },
    "pencil": {
        "description": "Mocno zużyty ołówek, a raczej jego reszta. Widnieją na nim ślady zębów",
        "location": "middle right",
        "take": True,
        "use": "specjalna rzecz",
        "special": True
    },
    "pinpad": {
        "description": "Czytnik pin na 6 cyfr, z czego pierwsze dwa miejsca świecą się czerwono, dwa następne na zielono, a ostatnie na niebiesko",
        "location": "door",
        "use": "Podanie kombinacji v2",
    },
    "safe": {
        "description": "No sejf jak sejf. Na 4 cyfry",
        "location": "middle left",
        "use": "Podanie kombinacji?",
        "examined": False
    },
    "canvas": {
        "description": "Płótno z dziewczyną trzymającą różę. Za nim wydaje się nie być ściany. Możesz spróbować ją przeciąć",
        "location": "middle right",
        "state": "cut"
    },
    "newspaper": {
        "description": "Jakiś tekst z gazety. Podkreślony jest wrzesień",
        "location": "middle right",
        "take": False,
        "use": "Treść gazety",
    },
    "closet": {
        "description": "Old lab coats. There's a <<death certificate>> inside it. ",
        "location": "middle left",
        "examined": False,
    },
    "laptop": {
        "description": "Old laptop. It's working but moving the cursor or even trying to power off the machine doesn't seem to work.\nIt's showing a single photo of a young girl with blonde hair, blue eyes and a big smile. The file says 'Amber.jpg'",
        "location": "middle left",
        "use": "Kod na lapku",
        "examined": False,
    },
    "window": {
        "description": "Pustka",
        "location": "middle left",
        "use": "Ani drgnie",
    },
    "wall": {
        "description": "It says 'Beware of ligma'. You wonder what that means.",
        "location": "far right",
    },
    "floor": {
        "description": "5 petals are down.",
        "location": "far right"
    },
    "diary": {
        "description": "Diary placeholder",
        "location": "far left",
        "take": True,
        "use": "Wpis w dzienniku",
        "examined": False,
    },
    #meble dziewczęce z pokoju
    "mirror": {
        "description": "You see yourself. You decide to touch it. \nIt shatters.\nNext thing you notice is your hands covered in blood.\nYou did this to yourself. All of it.\nYou deserve it.",
        "location": "mirror room",
        "use": "Walka",
        "examined": False,
    }
}