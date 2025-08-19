def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

number = 6  # You can change this value to calculate factorial of another number
fact = factorial(number)
print(f"The factorial of {number} is {fact}")
