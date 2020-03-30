class HouseKim:
    lastname = "KIM"

    def __init__(self, name):
        self.fullname = name + " " + self.lastname

    def travel(self, where):
        print(self.fullname + " goes on trip to " + where)

    def __del__(self):
        print("Killing " + self.fullname)


pey = HouseKim("WOOSEOK")
pey.travel("Europe")  # WOOSEOK KIM goes on trip to Europe
del pey  # Killing WOOSEOK KIM


'''
Inheritance
'''


class HousePark(HouseKim):
    lastname = "PARK"

    def travel(self, where, day):
        print(self.fullname, " goes to ", where, " on", day)


julliet = HousePark("Julliet")
julliet.travel("Dokdo", 3)
