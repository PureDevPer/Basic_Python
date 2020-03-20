a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])  # [3, ['a', 'b', 'c'], 4]

a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)  # [1, 2, 3, 4, 5, 6]
print(a*3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

a[1:2] = ['a', 'b', 'c']
print(a)  # [1, 'a', 'b', 'c', 3]

a[1:3] = []
print(a)  # [1, 'c', 3]

del a[1]
print(a)  # [1, 3]

a.append(2)
print(a)  # [1, 3, 2]

a.sort()
print(a)  # [1, 2, 3]

a.reverse()
print(a)  # [3, 2, 1]

print(a.index(3))  # 0
print(a.index(1))  # 2

a.insert(0, 4)
print(a)  # [4, 3, 2, 1]
a.insert(3, 5)
print(a)  # [4, 3, 2, 5, 1]

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)  # [1, 2, 1, 2, 3]
a.remove(3)
print(a)  # [1, 2, 1, 2]

a.pop()
print(a)  # [1, 2, 1]
a.pop(1)
print(a)  # [1, 1]

a = [1, 2, 3, 1]
print(a.count(1))  # 2
print(a.count(2))  # 1

a.extend([4, 5])
print(a)  # [1, 2, 3, 1, 4, 5]
