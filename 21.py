class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price


class Basket:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.total_price = sum([i.price for i in self.items])
        self.count = len(self.items)

    def add_to_basket(self, product):
        self.items.append(product)
        print(f"Added {product.name} to basket")
        self.total_price = sum([i.price for i in self.items])

    def remove_from_basket(self, product):
        self.items.remove(product)
        print(f"Removed {product.name} from basket")
        self.total_price = sum([i.price for i in self.items])

    def show_factor(self):
        print(f"Your basket items : {[i.name for i in self.items]}")
        print(f"Final factor : {self.total_price}")
        print("-" * 100)


kala1 = Product(17676195, "shark 9", 12800000)
kala2 = Product(16835001, "Redmi Watch 5 Active", 1700000)
kala3 = Product(4786906, "SAJTH underwear", 130000)

mamad = Basket(1001)
arian = Basket(1002)

mamad.add_to_basket(kala3)
mamad.add_to_basket(kala1)

print('-' * 100)
mamad.show_factor()

mamad.remove_from_basket(kala2)
print('-' * 100)
mamad.show_factor()
