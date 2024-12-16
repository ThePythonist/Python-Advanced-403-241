def factorial(number):
    if number == 1:
        return 1  # or number
    else:
        return number * factorial(number - 1)


number = int(input("Enter any number to see factorial : "))
if number >= 1:
    print(factorial(number))
elif number == 0:
    print("Factorial of zero is one")
else:
    print("Factorial of negative number doesnt exists")
