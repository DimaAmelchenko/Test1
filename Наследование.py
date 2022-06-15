class Transport:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour
        print('Transport')

    def price(self):
        pass

class Motorbike(Transport):
    def __init__(self, brand, colour, engine_capacity):
        super().__init__(brand, colour)
        self.engine_capacity = engine_capacity
        print(f"Motorbike = Brand: {self.brand}, Colour: {self.colour}, Engine capacity: {self.engine_capacity}")

    def price(self):
        print('Price: 5000')

class Bike(Transport):
    def __init__(self, brand, colour):
        super().__init__(brand, colour)
        print(f"Bike = Brand: {self.brand}, Colour: {self.colour}")

    def price(self):
        print('Price: 1000')

m1 = Motorbike('Ducati', 'Red', 1.0)
m1.price()
b1 = Bike('Stels', 'Grey')
b1.price()


