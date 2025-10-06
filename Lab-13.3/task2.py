def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# Example usage and output
# Assuming 'example.txt' exists and 'missing.txt' does not
print(read_file("example.txt"))  # Output: (contents of example.txt)
print(read_file("missing.txt"))  # Output: Error: The file 'missing.txt' was not found.
