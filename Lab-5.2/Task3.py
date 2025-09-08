def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Base case: if n is 1, return 1
    elif n == 1:
        return 1
    # Recursive case: sum of previous two Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
# Calculate the 6th Fibonacci number
result = fibonacci(6)
print(f"The 6th Fibonacci number is: {result}")