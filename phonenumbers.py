import random


def irancell():
    codes = ["0930", "0939", "0933", "0936"]
    pn = f"{random.choice(codes)}"
    for i in range(7):
        pn += str(random.randint(0, 9))
    return pn


def hamrahaval():
    codes = ["0912", "0911", "0919", "0993"]
    pn = f"{random.choice(codes)}"
    for i in range(7):
        pn += str(random.randint(0, 9))
    return pn


def rightell():
    codes = ["0921", "0922", "0923"]
    pn = f"{random.choice(codes)}"
    for i in range(7):
        pn += str(random.randint(0, 9))
    return pn

