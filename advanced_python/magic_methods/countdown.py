"""Iterators"""
class CountDown: 
    """Simple iterator that countdowns from a simple number"""

    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        """Return the iteratos object"""
        return self 
    
    def __next__(self):
        """return the next value in the countdown"""
        if self.current>0:
            value = self.current
            self.current -= 1
            return value 
        raise StopIteration
for number in CountDown(5):
    print(number)         
