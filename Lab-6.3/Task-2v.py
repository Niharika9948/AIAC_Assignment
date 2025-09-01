def print_multiples_for(num):
    print("Using for loop:")
    for i in range(1, 11):
        print(num * i)

def print_multiples_while(num):
    print("Using while loop:")
    i = 1
    while i <= 10:
        print(num * i)
        i += 1

# Example usage:
number = 5
print_multiples_for(number)
print_multiples_while(number)