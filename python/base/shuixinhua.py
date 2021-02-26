#!/usr/bin/python3

for number in range(100,1000):
    a = number % 10
    b = number // 10 % 10
    c = number // 100
    if number == a ** 3 + b ** 3 + c ** 3:
        print(number)
