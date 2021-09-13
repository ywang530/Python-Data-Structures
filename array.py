class Array:
    """Represent a array"""

    def __init__(self,d):
        """create an array with length d"""
        self._array = [0] * d

    def __setitem__(self,j,val): # a[j] = val
        self._array[j] = val

    def __getitem__(self,j):    # return a[j]
        return self._array[j]

    def __len__(self):
        return len(self._array)

    def __add__(self,other):
        if len(self) != len(other): # relies on __len__ method
            raise ValueError('size must be the same')
        result = Array(len(self))
        for i in range (len(self)):
            result[i] = self[i] + other[i]
        return result

    def __sub__(self,other):
        if len(self) != len(other): # relies on __len__ method
            raise ValueError('size must be the same')
        result = Array(len(self))
        for i in range (len(self)):
            result[i] = self[i] - other[i]
        return result

    def __eq__(self,other):
        return self._array == other._array

    def __ne__(self,other): # rely on existing __eq__ definition
        return not self._array == other._array

    def __str__(self):  # print
        return '[' + str(self._array)[1:-1] + ']' # adapt list representation


if __name__ == '__main__':
    # unit test
    a = Array(5)
    b = Array(5)
    a[3] = 6 
    b[1] = 4
    print(a[3])
    print(len(a))
    print(a+b)
    print(a-b)
    print(a!=b)