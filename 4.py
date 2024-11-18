from faker import Faker
from pprint import pprint

fake = Faker()
people = []

for i in range(4):
    person = {
        "name": fake.name(),
        "email": fake.email(),
        "country": fake.country(),
        "birth": str(fake.date_of_birth()),
    }

    people.append(person)

pprint(people)
