import json


def read_data():
    f = open("payments.json")
    data = json.load(f)
    employees = data["employees"]
    salaries = []

    for i in employees:
        for j in i["monthly_payment"].values():
            salaries.append(j)

    avg = sum(salaries) / len(salaries)
    print("Average salary for employees in the past year :", avg)


read_data()
