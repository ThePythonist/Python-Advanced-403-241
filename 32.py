import json


def read_data():
    f = open("states.json")
    data = json.load(f)
    states = data["states"]
    names = [i["name"] for i in states]
    return names


def write_data():
    f = open("state_names.json", "w")
    states = read_data()
    json.dump(states, f)
    print(f.name, "created successfully")


write_data()
