import codecs, json

inventory = []

descriptions = {}
file = open("/home/weronika/Desktop/python_projekt/locations_descriptions.txt", "r")

for line in file:
    line = line.split(":")
    room = line[0]
    description = codecs.decode(line[-1], 'unicode_escape')
    descriptions[room] = description

file.close()

detailed_descriptions = {}
file = open("/home/weronika/Desktop/python_projekt/look_around.txt", "r")

for line in file:
    line = line.split(":")
    room = line[0]
    detailed_description = codecs.decode(line[-1], 'unicode_escape')
    detailed_descriptions[room] = detailed_description
file.close()

file = open("movement_map.txt", "r")
data = file.read()
movement_map = json.loads(data)
file.close()

file = open("items.txt", "r")
data = file.read()
items = json.loads(data)
file.close()