def validate_indian_mobile_number(mobile_number: str) -> bool:
    
    if len(mobile_number) != 10:
        return False
    if not mobile_number.isdigit():
        return False
    if mobile_number[0] not in {'6', '7', '8', '9'}:
        return False
    return True

if __name__ == "__main__":
    number = input("Enter an Indian mobile number: ")
    if validate_indian_mobile_number(number):
        print("Valid Indian mobile number.")
    else:
        print("Invalid Indian mobile number.")
