class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  
class LinkedList:
    def __init__(self):
        self.head = None  
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node  

    def delete_value(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev is None:
                    self.head = current.next  
                else:
                    prev.next = current.next  
                return True  
            prev = current
            current = current.next
        return False  

    def traverse(self):
        """Return a list of all elements in the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
if __name__ == "__main__":
    ll = LinkedList()
    # Test insertion
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("After insertions:", ll.traverse())  # [10, 20, 30]
    ll.delete_value(10)
    print("After deleting head (10):", ll.traverse())  # [20, 30]
    ll.insert_at_end(40)
    ll.delete_value(30)
    print("After deleting middle node (30):", ll.traverse())  # [20, 40]
    ll.delete_value(40)
    print("After deleting last node (40):", ll.traverse())  # [20]
    result = ll.delete_value(100)
    print("Attempt to delete non-existent value (100):", result, ll.traverse())  # False, [20]
    ll.delete_value(20)
    print("After deleting last remaining node (20):", ll.traverse())  # []
    ll.insert_at_end(50)
    print("After inserting into empty list:", ll.traverse())  # [50]
