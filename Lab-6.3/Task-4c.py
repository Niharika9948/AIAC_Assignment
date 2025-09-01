def sum_to_n(n):
    """
    Calculate the sum of the first n natural numbers using a for loop.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# 2. Using the built-in sum and range functions (no explicit loop):
def sum_to_n_builtin(n):
    return sum(range(1, n + 1))

# 3. Using the mathematical formula:
def sum_to_n_formula(n):
    return n * (n + 1) // 2

# Example usage:
if __name__ == "__main__":
    n = 10
    print("Sum using for loop:", sum_to_n(n))
    print("Sum using while loop:", sum_to_n_while(n))
    print("Sum using built-in sum:", sum_to_n_builtin(n))
    print("Sum using formula:", sum_to_n_formula(n))
