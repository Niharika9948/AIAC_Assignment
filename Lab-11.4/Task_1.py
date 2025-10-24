
class Stack:
    """A simple Stack implementation (LIFO) using a Python list.

    Methods:
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the item on the top of the stack.
        peek(): Return the item on the top of the stack without removing it.
        is_empty(): Return True if the stack is empty, False otherwise.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack.

        Args:
            item: The item to be added.
        """
        self._items.append(item)

    def pop(self):
        """Remove and return the item on the top of the stack.

        Returns:
            The item at the top.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the item on the top of the stack without removing it.

        Returns:
            The item at the top.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Check if the stack is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return len(self._items) == 0


if __name__ == "__main__":
    # Test stack operations with sample data
    stack = Stack()
    print("Is stack empty? ->", stack.is_empty())

    print("Pushing 1")
    stack.push(1)
    print("Pushing 2")
    stack.push(2)
    print("Pushing 3")
    stack.push(3)

    print("Peek top:", stack.peek())
    print("Popping:", stack.pop())
    print("Peek after pop:", stack.peek())
    print("Is stack empty?", stack.is_empty())
    print("Popping:", stack.pop())
    print("Popping:", stack.pop())
    print("Is stack empty after popping all?", stack.is_empty())

    # Uncomment below to see error handling in action
    # print("Attempting to pop from empty stack:")
    # stack.pop()

    print("\n--- Suggestions for Optimization ---")
    print(
        "Using collections.deque instead of list can offer faster appends/pops from either end (O(1)),\n"
        "whereas list pops from the end are O(1) but appends/pops from the start are O(n). For most stack use cases,\n"
        "Python's list suffices, but if you need thread-safety or frequent left pops, consider using deque."
    )


