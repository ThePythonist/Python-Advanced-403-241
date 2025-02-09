import json


def read_data():
    f = open("payments.json")
    data = json.load(f)
    employees = data["employees"]

    for i in employees:
        print(i["name"], ":", i["job_title"])


read_data()
