class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        return f"The price of {self.model} is ${self.price}"


car1 = Car("Toyota Camry", 2020, 24000)
car2 = Car("Honda Accord", 2021, 26000)

print(car1.cost())
print(car2.cost())