def rectangle_area(x, y):
    return x * y

def square_area(x):
    return x * x

def circle_area(x):
    return 3.14 * x * x

def calculate_area(shape, x, y=0):
    area_functions = {
        "rectangle": lambda x, y: rectangle_area(x, y),
        "square": lambda x, y: square_area(x),
        "circle": lambda x, y: circle_area(x)
    }
    if shape not in area_functions:
        raise ValueError(f"Unknown shape: {shape}")
    return area_functions[shape](x, y)

# Example usage and output
print(calculate_area("rectangle", 4, 5))  # Output: 20
print(calculate_area("square", 3))        # Output: 9
print(calculate_area("circle", 2))        # Output: 12.56

