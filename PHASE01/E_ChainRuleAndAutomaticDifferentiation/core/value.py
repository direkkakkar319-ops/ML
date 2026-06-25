class Value:
    """
    Every Value stores its numeric data, its gradient (initially zero),
    a backward function, and pointers to child nodes that produced it.
    """
    def __init__(self, data, children=(), op=''):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(children)
    
    
    def __repr__(self):
        return f"Value(data={self.data:.4f}, grad={self.grad:.4f})"
    
    """
    Arithmetic operations with gradient tracking
        Each operation creates a closure that knows how to
        compute local gradients and multiply by the upstream
        gradient `(out.grad)`.
        
        The `+=` handles the case where a value is used in
        multiple operations.
    """
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        output = Value(self.data + other.data, (self, other), "+")
        
        def _backward():
            self.grad += output.grad
            other.grad += output.grad
        
        output._backward = _backward

        return output
    
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        output = Value(self.data * other.data, (self, other), "*")

        def _backward():
            self.grad += other.data * output.grad
            other.grad += self.data * output.grad
        
        output._backward = _backward

        return output
    

    def relu(self):
        output = Value(max(0, self.data), (self,), "relu")

        def _backward():
            self.grad += (1.0 if output.data > 0 else 0.0) * output.grad
        
        output._backward = _backward

        return output
    

    def backward(self):
        """
        Topological sort ensures every node's gradient is
        fully computed before it propagates to its children.
        The seed gradient is 1.0 (dy/dy = 1).
        """
        topo = []
        visited = set()

        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
            build_topo(self)
        
        self.grad = 1.0
        for v in reversed(topo):
            v._backward()