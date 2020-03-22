def sum(a, b):
    return a+b


print(sum(3, 4))  # 7


# When we don't know how many arguments need
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(sum_many(1, 2, 3))  # 6
print(sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55


def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result


print(sum_mul('sum', 1, 2, 3, 4, 5))  # 15
print(sum_mul('mul', 1, 2, 3, 4, 5))  # 120


def sum_and_mul(a, b):
    return a+b, a*b


print(sum_and_mul(3, 4))  # (7, 12)
sum, mul = sum_and_mul(3, 4)
print(sum, mul)
