import json
from colorama import Fore


def read_data():
    f = open("payments.json")
    data = json.load(f)
    employees = data["employees"]
    salaries = {}

    for i in employees:
        avg = sum(i["monthly_payment"].values()) / len(i["monthly_payment"].values())
        salaries.setdefault(i['name'], avg)

    max_salary = max(salaries.values())

    for k, v in salaries.items():
        if salaries[k] == max_salary:
            print(Fore.RED + f"{k} : {v}")
        else:
            print(Fore.LIGHTWHITE_EX + f"{k} : {v}")


read_data()
