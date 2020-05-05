class Car():
    def __init__(self, *args, **kwargs):
        print(kwargs)
        self.wheels = 4
        self.doors = 4
        self.windows = 5
        self.seats = 5
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car has {self.wheels} wheels"


porsche = Car(color="green", price="$40")
#{'color': 'green', 'price': '$40'}
# Car has 4 wheels
print(porsche)
print(porsche.color, porsche.price)  # green $40

bmw = Car()
print(bmw.color, bmw.price)  # black $20
