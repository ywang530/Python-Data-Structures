class MyQueue:
    # Implement a first in first out (FIFO) queue using only two stacks
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
 
        if not len(self.stack_out):
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
           
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        return not(self.stack_in or self.stack_out)

if __name__ == '__main__':

    myQueue = MyQueue()
    myQueue.push(1) # queue is: [1]
    myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
    print(myQueue.peek())  # return 1
    print(myQueue.pop())   # return 1, queue is [2]
    print(myQueue.peek())
    print(myQueue.empty()) # return false