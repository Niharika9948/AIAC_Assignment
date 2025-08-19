def calculate_power_bill(customer_type, units_consumed):
    """
    Calculate the power bill based on customer type and units consumed.

    Args:
        customer_type (str): Type of customer - 'residential', 'commercial', or 'industrial'
        units_consumed (float): Number of units consumed

    Returns:
        float: Total bill amount
    """
    customer_type = customer_type.lower()
    if customer_type == 'residential':
        # Example: First 100 units at $0.12/unit, next 200 at $0.15, rest at $0.20
        if units_consumed <= 100:
            bill = units_consumed * 0.12
        elif units_consumed <= 300:
            bill = 100 * 0.12 + (units_consumed - 100) * 0.15
        else:
            bill = 100 * 0.12 + 200 * 0.15 + (units_consumed - 300) * 0.20
    elif customer_type == 'commercial':
        # Example: First 200 units at $0.16/unit, rest at $0.22
        if units_consumed <= 200:
            bill = units_consumed * 0.16
        else:
            bill = 200 * 0.16 + (units_consumed - 200) * 0.22
    elif customer_type == 'industrial':
        # Example: Flat rate $0.25/unit, minimum bill $500
        bill = units_consumed * 0.25
        if bill < 500:
            bill = 500
    else:
        raise ValueError("Invalid customer type. Choose 'residential', 'commercial', or 'industrial'.")
    return bill

# Example usage:
if __name__ == "__main__":
    print("Power Bill Calculator")
    ctype = input("Enter customer type (residential/commercial/industrial): ").strip()
    try:
        units = float(input("Enter units consumed: "))
        total_bill = calculate_power_bill(ctype, units)
        print(f"Total bill for {ctype} customer consuming {units} units: ${total_bill:.2f}")
    except ValueError as e:
        print("Error:", e)
