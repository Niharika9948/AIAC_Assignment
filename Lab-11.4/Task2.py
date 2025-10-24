
class QueueList:
    """Queue implementation using Python list."""
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._items) == 0

    def __str__(self):
        return f"Queue(front -> back): {self._items}"


# Testing QueueList
if __name__ == "__main__":
    print("=== Queue Implementation Using List ===")
    q1 = QueueList()
    print("Is queue empty?", q1.is_empty())
    print("Enqueue 10")
    q1.enqueue(10)
    print("Enqueue 20")
    q1.enqueue(20)
    print("Enqueue 30")
    q1.enqueue(30)
    print(q1)
    print("Dequeue:", q1.dequeue())
    print(q1)
    print("Is queue empty?", q1.is_empty())
    print("Dequeue:", q1.dequeue())
    print("Dequeue:", q1.dequeue())
    print("Is queue empty after all dequeues?", q1.is_empty())
    print()

    print("--- Performance Review ---")
    print(
        "This list-based queue is simple, but removing from the front (pop(0)) is O(n),\n"
        "making it inefficient for large queues. Let's ask an AI for optimization advice."
    )


    print("\n=== AI Performance Review and Suggestion ===")
    print("Q: How can I make queue operations more efficient in Python?\n")
    print(
        "AI:\n"
        "To optimize queue performance, consider using the 'collections.deque' class from Python's standard library.\n"
        "Deque (double-ended queue) allows O(1) append and pop operations from both ends, making enqueue and dequeue faster.\n"
        "Here's how you can implement an efficient queue using deque:"
    )

    # Deque implementation
    from collections import deque

    class QueueDeque:
        """Optimized queue using collections.deque."""
        def __init__(self):
            self._items = deque()

        def enqueue(self, item):
            """Add an item to the back of the queue."""
            self._items.append(item)

        def dequeue(self):
            """Remove and return the item from the front of the queue."""
            if self.is_empty():
                raise IndexError("dequeue from empty queue")
            return self._items.popleft()

        def is_empty(self):
            """Check if the queue is empty."""
            return len(self._items) == 0

        def __str__(self):
            return f"Queue(front -> back): {list(self._items)}"

    print("\n=== Queue Implementation Using deque ===")
    q2 = QueueDeque()
    print("Is queue empty?", q2.is_empty())
    print("Enqueue 'a'")
    q2.enqueue('a')
    print("Enqueue 'b'")
    q2.enqueue('b')
    print("Enqueue 'c'")
    q2.enqueue('c')
    print(q2)
    print("Dequeue:", q2.dequeue())
    print(q2)
    print("Is queue empty?", q2.is_empty())
    print("Dequeue:", q2.dequeue())
    print("Dequeue:", q2.dequeue())
    print("Is queue empty after all dequeues?", q2.is_empty())

    print("\nSummary:")
    print(
        "• List-based queue: Slow dequeue (O(n)), suitable for short queues or learning purposes.\n"
        "• deque-based queue: Fast dequeue (O(1)), recommended for production code and large data."
    )


