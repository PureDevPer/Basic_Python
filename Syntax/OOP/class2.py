class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first+self.second
        return result

    def mul(self):
        result = self.first*self.second
        return result

    def sub(self):
        result = self.first-self.second
        return result

    def div(self):
        result = self.first/self.second
        return result


a = FourCal()
a.setdata(4, 2)
print(a.sum())  # 6
print(a.mul())  # 8
print(a.sub())  # 2
print(a.div())  # 2.0
