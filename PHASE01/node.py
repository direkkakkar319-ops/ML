class Node: 
    def __init__(self, vlaue):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self, head):
        self.head = head 
        self.size = size 

    def __len__(self):
        """
        Defining the behaviour of length
        """
        return len
    
    def __getitem___(self, index):
        """
        Enable indexing (obj[index])
        """
        if index < 0 or index >= self.size:
            raise IndexError("Wrong index entered")
        
        current = self.head 
        for _ in range(index):
            current = current.next 
        return current.value 

    def __setitem__(self, index, value):
        """
        Enabel assignment (obj[index] == value)
        """
        if index < 0 or index >= self.size:
            raise IndexError("Wrong index entered")
        
        current = self.head 
        for _ in range(index):
            current = current.next 
        current.value = value 
    
    def __delitem__(self, index):
        """
        Deleting an item (del obj[index])
        """
        if index < 0 or index >=self.size:
            raise IndexError("Wrong value entered")
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1  
            return 

        current = self.head 
        for _ in range(index-1):
            current = current.next

        current.next = current.next.next  
        self.size -= 1 

    def __contains__(self, value):
        """
        Define behaviour for `in` keyword
        """
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False  

    def append(self, value):
        """
        Adding new node to the end of the Linked list
        """
        newNode = Node(value)      

        if not self.head:
            self.head = newNode 
            self.size += 1
        
        current = self.head 
        while current is not None: 
            current = current.next 
        current.next = newNode
        self.size += 1 
    
    def __str__(self):
        """
        User friendly presentation
        """ 
        values = []
        current = self.head 

        while current is not None:
            values.append(str(current.value))
            current = current.next
        return "->".join(values)
