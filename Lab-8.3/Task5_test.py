from Task5 import convert_date_format

def run_tests():
    test_cases = [
        # Normal cases
        ("2023-12-31", "31-12-2023"),
        ("2000-01-01", "01-01-2000"),
        ("1999-11-09", "09-11-1999"),
        ("2020-02-29", "29-02-2020"),  # Leap year

        # Edge cases
        ("0001-01-01", "01-01-0001"),  # Earliest possible date
        ("9999-12-31", "31-12-9999"),  # Latest possible date

        # Leading zeros
        ("2023-04-05", "05-04-2023"),
        ("2023-10-09", "09-10-2023"),

        # Invalid formats (should raise ValueError)
        ("2023/12/31", ValueError),
        ("31-12-2023", ValueError),
        ("2023-12", ValueError),
        ("2023-12-31-01", ValueError),
        ("", ValueError),
        ("2023-13-01", "01-13-2023"),  # Invalid month, but function doesn't validate month/day
        ("2023-00-00", "00-00-2023"),  # Invalid, but function doesn't validate
        ("abcd-ef-gh", "gh-ef-abcd"),  # Nonsense, but correct split
    ]

    for i, (input_val, expected) in enumerate(test_cases):
        try:
            result = convert_date_format(input_val)
            if isinstance(expected, type) and issubclass(expected, Exception):
                print(f"Test case {i+1}: convert_date_format({repr(input_val)}) => Expected exception {expected.__name__} | FAIL")
            else:
                print(f"Test case {i+1}: convert_date_format({repr(input_val)}) => {repr(result)} | Expected: {repr(expected)} | {'PASS' if result == expected else 'FAIL'}")
        except Exception as e:
            if isinstance(expected, type) and isinstance(e, expected):
                print(f"Test case {i+1}: convert_date_format({repr(input_val)}) => Raised {e.__class__.__name__} as expected | PASS")
            else:
                print(f"Test case {i+1}: convert_date_format({repr(input_val)}) => Raised {e.__class__.__name__} | Expected: {expected} | FAIL")

if __name__ == "__main__":
    run_tests()
