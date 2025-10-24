def linear_search(arr, target):
    """
    Performs a linear search on the given list arr to find the index of target.
    Returns the index if found, else returns -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Take input from console
input_list = input("Enter a list of elements separated by spaces: ")
arr = input_list.strip().split()
# Convert all elements to integers for the search (adjust if strings are valid)
arr = [int(x) for x in arr]

target = int(input("Enter the value to search for: "))

result = linear_search(arr, target)

if result != -1:
    print(f"Value {target} found at index {result}.")
else:
    print(f"Value {target} not found in the list.")