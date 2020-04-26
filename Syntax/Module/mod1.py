def sum(a, b):
    return a+b


def safe_sum(a, b):
    if type(a) != type(b):
        print("We can't add them")
        return
    else:
        result = sum(a, b)
        return result


if __name__ == "__main__":
    print(safe_sum("a", 1))
    print(safe_sum(1, 4))
