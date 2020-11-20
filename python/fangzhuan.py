#/usr/bin/python3

x = int(input('number = '))
fz = 0
while x > 0:
    fz = fz * 10 + x % 10
    x //= 10
print(fz)
