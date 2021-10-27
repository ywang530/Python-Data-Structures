from collections import deque

class MyStack:
    # Implement a last-in-first-out (LIFO) queue using only one queue
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        size = len(self.queue)
        size -= 1
        while size:
            self.queue.append(self.queue.popleft())
            size -= 1
        
        return self.queue.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[-1]
    
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue


if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.top()
    param_3 = obj.pop()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)