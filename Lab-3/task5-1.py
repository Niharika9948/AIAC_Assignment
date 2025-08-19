def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Example usage:
if __name__ == "__main__":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = fahrenheit_to_celsius(f)
    print(f"{f} Fahrenheit is {c:.2f} Celsius.")
