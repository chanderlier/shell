#!/usr/bin/python3
import math

for i in range(2,101):
    is_prime = True
    for factor in range(2, int(math.sqrt(i)+1)):
            if i % factor == 0:
                is_prime = False
                break
    if is_prime:
        print(i,end='\n')

