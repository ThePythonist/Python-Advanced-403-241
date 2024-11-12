import random
import time
import os


def password(length):
    password = [str(i) for i in random.sample(range(0, 10), length)]
    print("".join(password))


while True:
    print("Your password is ", end="")
    password(6)
    time.sleep(3)
    os.system("cls")
