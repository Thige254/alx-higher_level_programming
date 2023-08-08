#This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.
#The variable number will store a different value every time you will run this program
#The output of the program should be:
#The string Last digit of, followed by
#the number, followed by
#the string is, followed by the last digit of number, followed by
#if the last digit is greater than 5: the string and is greater than 5
#if the last digit is 0: the string and is 0
#if the last digit is less than 6 and not 0: the string and is less than 6 and not 0

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

