def sort_list(data):
    numbers = sorted([item for item in data if isinstance(item, int)])
    strings = sorted([item for item in data if isinstance(item, str)])
    return numbers + strings

items = [3, "apple", 1, "banana", 2]
print(sort_list(items))
