class BankAccount:
    def __init__(self, id, owner):
        # Attributes
        self.id = id
        self.owner = owner
        self.balance = 0

    # Methods
    def withdraw(self, value):  # bardasht
        fee = value * (1 / 100)  # karmozd

        if self.balance >= value + 10 + fee:  # 10 dollar baghi bemanad
            self.balance -= value
            self.balance -= fee
            print(f"Decreased account balance : {value}$")
            self.show_balance()
        else:
            print("Not enough credit")
            self.show_balance()

    def deposit(self, value):  # variz
        self.balance += value
        print(f"Increased account balance : {value}$")
        self.show_balance()

    def show_balance(self):
        print("-" * 50)
        print(f"Current account balance : {self.balance}$")
        print("-" * 50)


# Objects (Instances)
acc1 = BankAccount("1100", "hamed")
acc2 = BankAccount("1200", "tina")
acc3 = BankAccount("1300", "shahab")

acc2.deposit(50)
acc2.withdraw(39)
