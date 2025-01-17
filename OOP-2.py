# class Parent:
#     def say_hello(self):
#         print("hello")
#
#
# class Child(Parent):
#     def say_goodbye(self):
#         print("bye")
#
#
# valed = Parent()
# farzand = Child()

# ====================================================

class Parent:
    def __init__(self, familyname, city, job):
        self.familyname = familyname
        self.city = city
        self.job = job

    def say_hello(self):
        print("hello")


class Child(Parent):
    def __init__(self, familyname, city, university, job=None):
        super().__init__(familyname, city, job)
        self.university = university

    def say_goodbye(self):
        print("bye")


valed = Parent("ahmadi", "tehran", "teacher")
farzand = Child("ahmadi", "karaj", "sharif")

print(farzand.job)
