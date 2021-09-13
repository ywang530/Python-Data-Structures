import ctypes                                       # provides low-level arrays

class DynamicArray:
    '''A dynamic array class akin to a simplified Python list.'''

    def __init__(self):
        '''Create an empty array''' 
        self._n = 0                                 # count actual elements
        self._capacity = 1                          # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        '''Return number of elements stored in the array.'''
        return self._n

    def append(self, obj):
        '''Add object to end of the array.'''
        if self._n == self._capacity:               # not enough room
            self._resize(2 * self._capacity)        # double room
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        '''Insert value at index k, shifting subsequent values rightward.'''
        if self._n == self._capacity:               # not enough room
            self._resize(2 * self._capacity)        # double room
        # (for simplicity, assume 0 <= k <= n in this verion)
        for i in range(self._n, k, -1):             # shift rightmost first
            self._A[i] = self._A[i-1]               
        self._A[k] = value                          # store newest element
        self._n += 1

    def remove(self, value):
        '''Remove first occurrence of value (or raise ValueError).'''
        for i in range(self._n):
            if self._A[i] == value:                 # found a match!
                for j in range(i, self._n-1):       # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n-1] = None           # help garbage collection
                self._n -= 1                        # we have one less item
                return                              # exit immediately
            raise ValueError('value not found')     # only reached if no match

    def __getitem__(self, i):
        '''Return element at index i.'''
        if not 0 <= i < self._n:
            raise IndexError('invalid index')
        return self._A[i]                           # retrieve from array  

    def _resize(self, c):                           # nonpublic utitity
        B = self._make_array(c)                     # new (bigger) array
        for i in range(self._n):                    # for each existing value
            B[i] = self._A[i]
        self._A = B                                 # use the bigger array
        self._capacity = c

    def __str__(self):  # print
        return '[' + str(self._A)[1:-1] + ']' # adapt list representation

    def _make_array(self, c):                       # nonpublic utitity
        '''Return new array with capacity c.'''
        return (c * ctypes.py_object)()           # see ctypes documentation


if __name__ == '__main__':
    a = DynamicArray()
    a.append(1)
    print(a[0])
    print(a._n)
    a.insert(1,2)
    a.remove(1)
    for i in range (len(a)):
        print(a[i])