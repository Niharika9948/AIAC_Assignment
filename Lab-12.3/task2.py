def bubble_sort(arr):
    """
    Performs bubble sort on the given list arr.
    Returns the sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Take input from console
input_list = input("Enter a list of elements separated by spaces: ")
arr = input_list.strip().split()
arr = [int(x) for x in arr]

sorted_arr = bubble_sort(arr)

print("Sorted list:", sorted_arr)