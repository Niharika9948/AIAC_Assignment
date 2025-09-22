def calculate_percentage(amount, percentage_rate):
    """
    Calculate the percentage of a given amount.

    Parameters:
        amount (float or int): The base amount.
        percentage_rate (float or int): The percentage rate to apply.

    Returns:
        float: The calculated percentage value.
    """
    return amount * percentage_rate / 100  # Calculate percentage

total_amount = 200
discount_rate = 15

# Calculate the discount value based on the total amount and discount rate
discount_value = calculate_percentage(total_amount, discount_rate)

print(discount_value)  # Output the calculated discount value
