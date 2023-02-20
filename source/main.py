from calculations import calc
from filtering import filterEven
from hello import greetings

greetings()

print("Enter string to calculate(num operation num):")
try: 
    a, operation, b = input().split()
    print(calc(a, b, operation))
    print("Enter numbers separated by space to find even")
    numbers = input().split()
    print(filterEven(numbers))
except ValueError:
    print("Invalid string!")
