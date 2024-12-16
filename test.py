class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def talk(self):
        print(f"""
Hi Im {self.name} and I am a {self.job}
and I am {self.age} years old.
""")


hamed = Person("hamed", 30, "python developer")
hamed.talk()
