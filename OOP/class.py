class Service:
    secrect = "SECRET"

    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s" % (a, b, result))


# Pay is an INSTANCE, which is made by class
pay = Service()
print(pay.secrect)
# SECRET
print(pay.sum(1, 1))
# 1 + 1 = 2
# None


class Service2:
    secrect = "SECRET"

    def setname(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        #print("%s: %s + %s = %s" % (self.name, a, b, result))
        print(self.name, ": ", a, "+", b, "=", result)


pay2 = Service2()
pay2.setname("KIM")
print(pay2.sum(1, 1))
# KIM: 1 + 1 = 2
# None


class Service3:
    secrect = "SECRET"

    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print(self.name, ": ", a, "+", b, "=", result)


pay3 = Service3("KIM")
print(pay3.sum(1, 1))
# KIM :  1 + 1 = 2
# None
