import csv


def read(file):
    with open(file) as file:
        reader = csv.reader(file)
        headers = next(reader)
        for student in reader:
            # if "computer" in student[1]:
            #     print(student)

            if float(student[2]) >= 17:
                print(student)


read("students.csv")
