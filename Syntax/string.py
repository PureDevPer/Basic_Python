a = "Life is too short, You need Python"
print(a[0:3])  # Lif
print(a[0:5])  # Life
print(a[19:])  # You need Python
print(a[:17])  # Life is too short
print(a[:])  # Life is too short, You need Python

'''
String Formatting
'''

print('I eat %d apples.' % 100)  # I eat 100 apples.
print('I eat %s apples.' % "five")  # I eat five apples.

number = 10
day = "three"
print("I eat %d apples. So I was sick for %s days." % (number, day))
# I eat 10 apples. So I was sick for three days.
print("Todays rate is %s" % 3.234)  # Todays rate is 3.234
print("Error is %d%%." % 98)  # Error is 98%.
print("%10s" % "hi")  # hi
print("%-10s jane." % 'hi')  # hi         jane.
print("%0.4f" % 3.42134234)  # 3.4213
print("%10.4f" % 3.42134234)  # 3.4213

'''
Useful Function
'''
a = "hi"
print(a.upper())  # HI

a = "HI"
print(a.lower())  # hi

'''
A number of 'b'
'''
a = "hobby"
print(a.count('b'))  # 2

a = "Python is best choice"
print(a.find('b'))  # 10
print(a.find('z'))  # -1

a = "Life is too short"
print(a.index('t'))  # 8
# print (a.index('z')) # error

a = ","
print(a.join("abcd"))  # "a,b,c,d"

a = "    hi"
print(a.lstrip())  # hi

a = "hi     "
print(a.rstrip())  # hi

a = "    hi    "
print(a.strip())  # hi

a = "Life is too short"
print(a.replace("Life", "Your leg"))  # Your leg is too short

a = "Life is too short"
print(a.split())  # ['Life', 'is', 'too', 'short']

a = "a:b:c:d"
print(a.split(":"))  # ['a', 'b', 'c', 'd']

a = "Hi man"
print(a.swapcase())  # hI MAN
