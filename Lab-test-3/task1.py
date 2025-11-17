# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")
        self.display()

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        print(f"Inserted {data} at the end.")
        self.display()

    # Delete a node by value
    def delete_node(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            print(f"Deleted node with value {key}.")
            self.display()
            return

        # Search for the key
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # Key not found
        if temp is None:
            print(f"Node with value {key} not found.")
            self.display()
            return

        # Unlink the node
        prev.next = temp.next
        temp = None
        print(f"Deleted node with value {key}.")
        self.display()

    # Display the linked list
    def display(self):
        temp = self.head
        if temp is None:
            print("Linked list is empty.\n")
            return
        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None\n")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    
    # Insert at beginning
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    
    # Insert at end
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    
    # Delete nodes
    ll.delete_node(20)
    ll.delete_node(50)  # Node not in the list

