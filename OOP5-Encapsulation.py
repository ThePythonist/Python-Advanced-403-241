class MyClass:
    def __init__(self):
        self.public_member = "I am a public member"
        self._protected_member = "I am a protected member"
        self.__private_member = "I am a private member"

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")
        print(self.__private_member)


# Creating an instance of the class
obj = MyClass()


# Accessing public members and calling public methods

# print(obj.public_member)
# obj.public_method()

# obj.public_member = "Im not a public member"
# print(obj.public_member)

# Accessing protected members and calling protected methods
# print(obj._protected_member)
# obj._protected_method()
# obj._protected_member = "Im not a protected member"
# print(obj._protected_member)

# Trying to access private members and calling private methods (will result in an error)

# print(obj.__private_member)
# obj.__private_method()

# obj.__private_member = "yechizi"
# print(obj.__private_member)

# --------------------------------------------------------------------------------------------


class User:
    def __init__(self):
        self.username = "hamed_99"  # public
        self.__password = "123456"  # private

    def change_password(self, new_password):
        self.__password = new_password

    def show_password(self):  # The getter method
        print(self.__password)


hamed = User()
hamed.change_password("aaabbb")
hamed.show_password()

# --------------------------------------------------------------------------------------------

# class Car:
#     def __init__(self):
#         self.color = "Black" # Public member
#         self.__mileage = 0  # Private member
#
#     def _drive(self, kilometers):
#         print("Driving the car")
#         for i in range(kilometers):
#             self.__increase_mileage()
#
#         print(f"Mileage : {self.__mileage}")
#
#     def __increase_mileage(self):  # The Getter method
#         self.__mileage += 1 # Accesing private member
#
#
# my_car = Car()
# my_car._drive(35)
