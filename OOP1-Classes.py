import time


class SedanCar:  # PascalCase
    def __init__(self, esm, pelak, rang, delay):
        self.name = esm
        self.plate = pelak
        self.color = rang
        self.speed = 0
        self.delay = delay
        self.engine = False

    def start_engine(self):  # snake_case
        self.engine = True
        print("Started Engine")

    def accelerate(self, value):
        if self.engine == True:
            for i in range(value):
                time.sleep(self.delay)
                self.speed += 10
                print("Current Speed :", self.speed)
        else:
            print("Engine is off")

    def brake(self):
        pass

    def horn(self):
        print("Beeeeeeep")


# Creating instance/object
samand = SedanCar("samand", "86S325IR44", "white", 2)
dena = SedanCar("dena", "34A325IR68", "black", 1)
runna = SedanCar("runna", "70J225IR72", "red", 1.5)
charger = SedanCar("Charger", "NADARAD", "black", 0.3)

charger.start_engine()
charger.accelerate(3)

charger.horn()
