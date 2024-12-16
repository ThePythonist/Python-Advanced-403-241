class Calculator:
    def __init__(self, n1, op, n2):
        self.n1 = n1
        self.n2 = n2
        self.operator = op

    def add(self):
        print(self.n1 + self.n2)

    def subtract(self):
        print(self.n1 - self.n2)

    def multiply(self):
        print(self.n1 * self.n2)

    def divide(self):
        print(self.n1 / self.n2)


while True:
    n1 = int(input("Enter number 1 : "))
    op = input("Enter operator : ")
    n2 = int(input("Enter number 2 : "))

    mashinhesab = Calculator(n1, op, n2)

    if op == "+":
        mashinhesab.add()
    elif op == "-":
        mashinhesab.subtract()
    elif op == "*":
        mashinhesab.multiply()
    elif op == "/":
        mashinhesab.divide()
    else:
        print("Invalid operator")
