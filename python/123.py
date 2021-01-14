def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add())
print(add(1))
print(add(1, 2, 3))
print(add(1, 2, 4, 5))
print(add(1, 3, 4, 5, 67, 88))
