class Node:
    """Node class for singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to next node (or None if end of list)

class LinkedList:
    """Singly Linked List with insert, delete, and traverse operations."""
    def __init__(self):
        self.head = None  # Points to the first node in the list (or None if empty)

    def insert_at_end(self, data):
        """Insert a new node with value 'data' at the end of the list."""
        new_node = Node(data)
        if not self.head:
            # If the list is empty, set head to new node
            self.head = new_node
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next
            # At the last node, set its next pointer to the new node
            current.next = new_node
        # AI: When inserting at end, only the last node's 'next' pointer is updated to point to the new node.

    def delete_value(self, value):
        """Deletes the first node found with the given value."""
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev is None:
                    # Deleting the head node; just move head pointer to next node.
                    self.head = current.next
                else:
                    # Bypass the current node by updating prev's next pointer
                    prev.next = current.next
                # AI: To delete a node, the previous node's 'next' pointer is updated to skip over the deleted node.
                return True  # Value found and deleted
            prev = current
            current = current.next
        return False  # Value not found

    def traverse(self):
        """Traverse the list and return elements as a list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

if __name__ == "__main__":
    # Example usage and basic manual tests
    ll = LinkedList()
    print("Insert 1, 2, 3 at end:")
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    print("Current list:", ll.traverse())

    print("Delete value 2:")
    ll.delete_value(2)
    print("Current list after deleting 2:", ll.traverse())

    print("Delete value 1 (head):")
    ll.delete_value(1)
    print("Current list after deleting 1:", ll.traverse())

    print("Try deleting value 99 (not present):")
    result = ll.delete_value(99)
    print("Delete successful?", result)
    print("Current list:", ll.traverse())

    print("Delete value 3 (remaining node):")
    ll.delete_value(3)
    print("Current list after deleting all nodes:", ll.traverse())

    # AI: Test cases to validate all operations
    print("\nSuggested Test Cases:")
    print("1. Insert multiple elements and traverse to check ordering.")
    print("2. Delete head, middle, and last node, check list after each.")
    print("3. Delete from an empty list (should do nothing or return False).")
    print("4. Insert after all deletions to ensure list resets correctly.")
    print("5. Try removing a value not present (should return False and not change the list).")

