from copy import copy

a = 3
b = 3
print(a is b)  # True

a, b = 'python', 'life'
(c, d) = ('python', 'life')
[e, f] = ['python', 'life']
g = h = 'python'

a = 3
b = 5
a, b = b, a
print(a, b)  # 5 3

# Copy of LIst
a = [1, 2, 3]
b = a
a[1] = 4
print(a)  # [1, 4, 3]
print(b)  # [1, 4, 3]

# Solution 1
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)  # [1, 4, 3]
print(b)  # [1, 2, 3]


# Solution 2
a = [1, 2, 3]
b = copy(a)
a[1] = 4
print(a)  # [1, 4, 3]
print(b)  # [1, 2, 3]
