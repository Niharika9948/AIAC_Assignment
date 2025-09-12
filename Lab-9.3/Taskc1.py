def sum_even_odd(numbers):
    """
    Calculates the sum of even and odd numbers in a given list.

    Args:
        numbers (list of int): The list of integers to process.

    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers.
            - The sum of odd numbers.

    Raises:
        TypeError: If any element in the list is not an integer.

    Example:
        >>> sum_even_odd([1, 2, 3, 4])
        (6, 4)
    """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers.")
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")
    return even_sum, odd_sum

# AI-generated docstring (using Copilot):
# """
# Returns the sum of even and odd numbers in the given list.
#
# Args:
#     numbers (list): List of integers.
#
# Returns:
#     tuple: (sum of even numbers, sum of odd numbers)
# """

# Comparison:
# Manual docstring is more detailed, includes type checking, raises, and example.
# AI-generated docstring is concise, covers basic usage but lacks details and examples.

# Example usage:
if __name__ == "__main__":
    nums = [10, 15, 20, 25, 30]
    sum_even_odd(nums)
    