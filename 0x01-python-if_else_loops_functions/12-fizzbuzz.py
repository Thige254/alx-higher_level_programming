#!/usr/bin/python3
def fizzbuzz():
    for numbers in range(1, 101):
        print("FizzBuzz" if numbers % 15 == 0 else "Fizz" if numbers
              % 3 == 0 else "Buzz" if numbers % 5 == 0 else number, end=" ")
    print()
