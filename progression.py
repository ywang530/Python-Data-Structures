class Progression:
    def __init__(self,start=0):
        self._current = start

    def _advance(self):
        """Update self. current to a new value.
        This should be overridden by a subclass to customize progression."""
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def print_progression(self,n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    def __init__(self,increment=1,start=0):
        """Create a new arithmetic progression.
        increment the fixed constant to add to each term (default 1)
        start the first term of the progression (default 0)"""
        self._increment = increment
        super().__init__(start) # initialize base class

    def _advance(self):
        self._current += self._increment


class FibonacciProgression(Progression):
    def __init__(self,first=0,second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':
    seq =  Progression()
    seq.print_progression(3)
    ari_seq = ArithmeticProgression(3)
    ari_seq.print_progression(3)
    fib = FibonacciProgression(4,6)
    fib.print_progression(10)