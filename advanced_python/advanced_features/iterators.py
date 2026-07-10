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
    
    def __next__(self):
        """
        The `__next__` method defines the iteration behaviour.
        It should return the next item in the sequence or raise a 
        StopIteration.
        """
        if self.current<self.end:
            value = self.current
            self.current+=1
            return value
        else:
            raise StopIteration
        

if __name__=="__main__":
    my_range = MyRange(1,5)

    for number in my_range:
        print(number)
