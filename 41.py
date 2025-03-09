import csv

data = [
    ["name", "major", "grade"],
    ["mahla", "computer", "17"],
    ["taha", "computer", "15.67"],
    ["kiana", "electronic", "18.6"],
    ["mohammad", "literature", "16.89"],
]


def write(data):
    with open('students.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        print("File created successfully")


write(data)
