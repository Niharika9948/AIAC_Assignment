def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
try:
    fact = factorial(number)
    print(f"The factorial of {number} is {fact}")
except ValueError as e:
    print(e)

