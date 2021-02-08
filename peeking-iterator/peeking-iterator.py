class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.next_el = self.iterator.next()
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_el

    def next(self):
        """
        :rtype: int
        """
        res = self.next_el
        self.next_el = self.iterator.next()
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_el != -100000