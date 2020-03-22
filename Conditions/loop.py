# While

prompt = """
    1. Add
    2. Del
    3. List
    4. Quit

    Enter number:"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())


a = 0
while a < 10:
    a = a+1
    if a % 2 == 0:
        continue
    print(a)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("Student %d - PASS" % number)
    else:
        print("Student %d - Fail" % number)

"""
Student 1 - PASS
Student 2 - Fail
Student 3 - PASS
Student 4 - Fail
Student 5 - PASS
"""

a = range(10)
for n in a:
    print(n)
# [0,1,2,3,4,5,6,7,8,9]

a = range(1, 11)
for n in a:
    print(n)
# [1,2,3,4,5,6,7,8,9,10]

sum = 0
for i in range(1, 11):
    sum += i
print(sum)
