from Task3 import is_sentence_palindrome

def run_tests():
    test_cases = [
        # Palindromic sentences
        ("A man, a plan, a canal: Panama", True),
        ("No lemon, no melon", True),
        ("Was it a car or a cat I saw?", True),
        ("Madam In Eden, I'm Adam", True),
        ("Able was I ere I saw Elba", True),
        ("", True),  # Empty string is a palindrome
        ("   ", True),  # Only spaces
        ("!!!", True),  # Only punctuation

        # Not palindromic sentences
        ("Hello, world!", False),
        ("Python is fun", False),
        ("Palindrome", False),
        ("This is not a palindrome", False),

        # Edge cases
        ("A", True),  # Single character
        ("1", True),  # Single digit
        ("12 21", True),  # Numeric palindrome with space
        ("123abccba321", True),  # Alphanumeric palindrome
        ("123abc321", False),  # Not a palindrome
    ]

    for i, (input_val, expected) in enumerate(test_cases):
        result = is_sentence_palindrome(input_val)
        print(f"Test case {i+1}: is_sentence_palindrome({repr(input_val)}) => {repr(result)} | Expected: {repr(expected)} | {'PASS' if result == expected else 'FAIL'}")

if __name__ == "__main__":
    run_tests()
