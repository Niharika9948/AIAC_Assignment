age = int(input("Enter your age: "))

if age >= 0:
    if age <= 12:
        print("Age group: Child")
    elif age <= 19:
        print("Age group: Teen")
    elif age <= 59:
        print("Age group: Adult")
    else:
        print("Age group: Senior")
else:
    print("Invalid age entered.")