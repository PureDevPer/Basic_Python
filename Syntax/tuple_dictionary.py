t1 = (1, 2, 'a', 'b')
t2 = (3, 4)

print(t1 + t2)  # (1, 2, 'a', 'b', 3, 4)
print(t2 * 3)  # (3, 4, 3, 4, 3, 4)

dic = {
    'name': 'pey',
    'phone': '0119993323',
    'birth': '1118'
}
print(dic)
# {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])  # 10
print(grade['julliet'])  # 99

a = {1: 'a', 2: 'b'}
print(a[1])  # a
print(a[2])  # b

a[3] = 'c'
print(a)  # {1: 'a', 2: 'b', 3: 'c'}

a[4] = [1, 2, 3]
print(a)  # {1: 'a', 2: 'b', 3: 'c', 4: [1, 2, 3]}

del a[1]
print(a)  # {2: 'b', 3: 'c', 4: [1, 2, 3]}

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())  # ['birth', 'name', 'phone']
print(a.values())  # ['1118', 'pey', '0119993323']
# [('birth', '1118'), ('name', 'pey'), ('phone', '011993323')]
print(a.items())
print(a.get('name'))  # 'pey'
print('name' in a)  # True
print('email' in a)  # False
