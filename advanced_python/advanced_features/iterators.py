class MyRange:
    """
    Iterators
    """
    def __init__(self, start, end):
        self.current = start 
        self.end = end
    
    def __iter__(self):
        """
        The `__iter__` makes this class an iterable
        It should return an iterator object .
        """
        return self
