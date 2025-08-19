def calculate_power_bill(units):
    """
    Calculates the power bill based on the number of units consumed.
    Example slab:
        - First 100 units: $0.5 per unit
        - Next 100 units (101-200): $0.75 per unit
        - Next 100 units (201-300): $1.20 per unit
        - Above 300 units: $1.50 per unit
    """
    bill = 0
    if units <= 100:
        bill = units * 0.5
    elif units <= 200:
        bill = 100 * 0.5 + (units - 100) * 0.75
    elif units <= 300:
        bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.20
    else:
        bill = 100 * 0.5 + 100 * 0.75 + 100 * 1.20 + (units - 300) * 1.50
    return bill

# Example usage:
units_consumed = 350  # You can change this value to test with different units
bill_amount = calculate_power_bill(units_consumed)
print(f"Units Consumed: {units_consumed}")
print(f"Power Bill: ${bill_amount:.2f}")
