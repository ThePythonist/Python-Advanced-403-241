import json


def read_data():
    f = open("states.json")
    data = json.load(f)
    states = data["states"]
    return states


def write_data():
    f = open("state_names.json", "w")
    states = read_data()
    selected_states = []

    for i in states:
        if i["name"].lower() in ["alaska", "florida", "new york"]:
            selected_states.append(i)

    json.dump(selected_states, f)
    print(f.name, "created successfully")


write_data()
