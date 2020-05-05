class Car():
    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 5
        self.seats = 5
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car has {self.wheels} wheels"


class Convertible(Car):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return "Car with no roof"


benz = Convertible(color="green", price="$40")
print(benz.take_off())  # taking off
print(benz.wheels)  # 4
print(benz)  # Car with no roof
print(benz.color)
