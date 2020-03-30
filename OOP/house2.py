class HousePark:
    lastname = "PARK"

    def __init__(self, name):
        self.fullname = name + " " + self.lastname

    def travel(self, where):
        print(self.fullname, "goes to ", where)

    def love(self, other):
        print(self.fullname, "is falling in love with", other.fullname)

    def fight(self, other):
        print(self.fullname, "is fighting with", other.fullname)

    def __add__(self, other):
        print(self.fullname, "married", other.fullname)

    def __sub__(self, other):
        print(self.fullname, "and", other.fullname, "divorced")

    def __del__(self):
        print("Killing", self.fullname)


class HouseKim(HousePark):
    lastname = "KIM"

    def travel(self, where, day):
        print(self.fullname, "goes to", where, "for", day, "days")


pey = HousePark("John")
julliet = HouseKim("Julliet")
pey.love(julliet)
pey + julliet

'''
John PARK is falling in love with Julliet KIM
John PARK married Julliet KIM
Killing John PARK
Killing Julliet KIM
'''

pey = HousePark("John")
julliet = HouseKim("Julliet")
pey.travel("Dokdo")
julliet.travel("Dokdo", 3)
pey.love(julliet)
pey + julliet
pey.fight(julliet)
pey - julliet

'''
John PARK goes to  Dokdo
Julliet KIM goes to Dokdo for 3 days
John PARK is falling in love with Julliet KIM
John PARK married Julliet KIM
John PARK is fighting with Julliet KIM
John PARK and Julliet KIM divorced
Killing John PARK
Killing Julliet KIM
'''
