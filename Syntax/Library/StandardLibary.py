print(abs(3))  # 3
print(abs(-3))  # 3
print(abs(1+2j))  # 2.23606797749979


# ASCII
print(chr(97))  # a
print(ord('a'))  # 97

'''
Compare
x > y: 1
x < y: -1
x == y: 0
'''
# print(cmp(4, 3))  # 1
# print(cmp(3, 4))  # -1
# print(cmp(4, 4))  # 0

# 7/3 = 2
# 7%3 = 1
print(divmod(7, 3))  # (2,1)


for i, name in enumerate(['Alex', 'Mini', 'Tiffany']):
    print(i, name)
'''
0 Alex
1 Mini
2 Tiffany
'''


# Return String
print(eval('1+2'))  # 3
print(eval("'hi' + 'a'"))  # hia
print(eval('divmod(4,3)'))  # (1, 1)


# filter(function, list)
def positive(l):
    return l > 0


# lambda: Similar to def.
# It is used to make a line instead of def
l = [lambda a, b:a+b, lambda a, b:a*b]

print(l[0](3, 4))  # 7
print(l[1](2, 5))  # 10

print(len("python"))  # 6
print(len([1, 2, 3]))  # 3

# list: Return List from Input
print(list("python"))  # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3)))  # [1, 2, 3]

print(map(lambda a: a*2, [1, 2, 3, 4]))

print(range(5))  # [0,1,2,3,4]
print(range(5, 10))  # [5,6,7,8,9]
print(range(1, 10, 2))  # [1,3,5,7,9]
print(range(0, -10, -1))  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

print(sorted([3, 1, 2]))  # [1, 2, 3]
a = [3, 1, 2]
result = a.sort()
print(result)  # None
print(a)  # [1,2,3]

print(type("abc"))  # <class 'str'>
print(type([]))  # <class 'list'>
