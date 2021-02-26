#!/usr/bin/python3
from math import sqrt
number = int(input(' please enter a number: '))
num = int(sqrt(number))
is_prime = True
for x in range(2,num+1):
    if number % x == 0:
        is_prime = False
        break
if is_prime and num !=1 :
    print('%d is prime' % number)
else:
    print('%d is not prime' % number)
