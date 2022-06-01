#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_repr = repr(number)
lastNum = int(num_repr[-1])

if lastNum > 5:
    print(f"Last digit of {number} is {lastNum} and is greater than 5")
elif lastNum < 5 and lastNum != 0:
    print(f"Last digit of {number} is {lastNum} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lastNum} is 0")
