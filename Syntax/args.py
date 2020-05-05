def plus(a, b, *args):
    print(args)
    return a+b


# **kwargs: keyword argument
def minus(a, b, *args, **kwargs):
    print(args, kwargs)
    return a+b


def plus_all(*args):
    result = 0
    for number in args:
        result += number
    print(result)


# (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
plus(1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

# (1, 1, 1, 1, 1, 1, 1, 1, 1, 1) {'d': True, 'e': True, 'c': True, 'f': True}
minus(1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, d=True, e=True, c=True, f=True)


plus_all(1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # 13
