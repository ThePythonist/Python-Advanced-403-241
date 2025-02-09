import json

f = open("states.json")
data = json.load(f)
states = data["states"]

for i in states:
    print(i["name"])
