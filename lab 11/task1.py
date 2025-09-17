class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0
if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.is_empty())  
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Peek:", stack.peek()) 
    print("Pop:", stack.pop())  
    print("Pop:", stack.pop())    
    print("Is stack empty?", stack.is_empty())  
    print("Pop:", stack.pop()) 
    print("Is stack empty?", stack.is_empty()) 
    print("\nSuggestion: For better performance on large stacks, consider using collections.deque instead of list, as deque provides O(1) time complexity for append and pop operations from both ends. The interface would remain similar, but replace self._items = [] with self._items = deque(), and use append() and pop() as before.")
