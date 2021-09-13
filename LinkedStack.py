class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    #-------------------------- nested Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage
    
        def __init__(self, element, next):      # initialize node’s fields
            self._element = element             # reference to user’s element
            self._next = next                   # reference to next node

    #------------------------------- stack methods -------------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None                       # reference to the head node
        self._size = 0                          # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""    
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element              # top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO)."""
        if self.is_empty():
            raise Empty('Stack is empty')
        data = self._head._element
        old = self._head
        self._head = self._head._next           # bypass the former top node
        old = None
        self._size -= 1
        return data


if __name__ == '__main__':
    stack = LinkedStack()
    # print(stack._head._element)
    # print(stack._head._next)
    stack.push(10)
    stack.push(4)
    stack.push(9)
    stack.push(1)
    print(stack._head._element)
    print(stack._head._next._element)
    print(stack.top())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    # print(stack.pop())
