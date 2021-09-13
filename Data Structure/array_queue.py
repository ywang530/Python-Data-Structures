class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10       # moderate capacity for all new queues
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO)."""
        if self.is_empty():
            raise Empty('Queue is empty')
        data = self._data[self._front]
        self._data[self._front] = None      # help garbage collection
        self._front = (self._front + 1) % len(self._data)       # circularly
        self._size -= 1
        return data

    def enqueue(self, e):
        """Add an element to the back of queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))        # double the array when full
        idx = (self._front + self._size) % len(self._data)
        self._data[idx] = e
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old_data = self._data                           # keep track of existing list
        old_idx = self._front
        self._data = [None] * cap                       # allocate list with new capacity
        for i in range(self._size):                     # only consider existing elements
            self._data[i] = old_data[old_idx]           # intentionally shift indices
            old_idx = (old_idx + 1) % len(old_data)     # use old size as modulus
        self._front = 0                                 # front has been realigned