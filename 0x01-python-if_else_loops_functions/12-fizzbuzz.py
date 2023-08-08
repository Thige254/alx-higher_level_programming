#!/usr/bin/python3
def fizzbuzz():
    print(" ".join("FizzBuzz" if numbers % 15 == 0 else "Fizz" if numbers
                   % 3 == 0 else "Buzz" if numbers % 5 == 0 else str(numbers) for
                   numbers in range(1, 101)))
