class Car():
    wheels = 4
    doors = 4
    windows = 5
    seats = 5

    def __str__(self):
        return f"Car has {self.wheels} wheels"


porsche = Car()
porsche.color = "Red"

print(porsche.windows)  # 5
print(porsche.color)  # Red

ferrari = Car()
ferrari.color = "Blue"
print(ferrari.color)  # Blue

'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
    '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'doors', 'seats', 'start', 'wheels', 'windows']
'''
print(dir(Car))


print(porsche)  # Car has 4 wheels
print(porsche.__str__())  # Car has 4 wheels
