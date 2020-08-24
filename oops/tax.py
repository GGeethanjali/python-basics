class Product:
    def __init__(self, id_no, name, price, category):
        self.id_no = id_no
        self.name = name
        self.price = price
        self.category = category
        self.tax = 0

    def calculate_tax(self):
        if self.price > 500:
            self.tax = self.price * 0.05
        else:
            self.tax = self.price * 0.02

    def calculate_additional_tax(self):
        if self.price > 500:
            self.tax = self.price * 0.05
        else:
            self.tax = self.price * 0.02

item1 = Product("1", "apple", 30, "produce")
item2 = Product("2", "milk", 400, "dairy")
item3 = Product("3", "towel", 1150, "textile")
item4 = Product("4", "soap", 100, "home needs")

print(item1.calculate_tax())
