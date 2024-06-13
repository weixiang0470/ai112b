import numpy as np

class Value:
    """ stores a single scalar value and its gradient """

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0
        # internal variables used for autograd graph construction
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op # the op that produced this node, for graphviz / debugging / etc

    @property
    def shape(self):
        return self.data.shape
    
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward

        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward

        return out

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only supporting int/float powers for now"
        out = Value(self.data**other, (self,), f'**{other}')

        def _backward():
            self.grad += (other * self.data**(other-1)) * out.grad

        out._backward = _backward

        return out
    
    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self,), 'ReLU')

        def _backward():
            self.grad += (out.data > 0) * out.grad
        out._backward = _backward
        return out
    
    def matmul(self,other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(np.matmul(self.data , other.data), (self, other), 'matmul')

        def _backward():
            self.grad += np.dot(out.grad,other.data.T)
            other.grad += np.dot(self.data.T,out.grad)            
            
        out._backward = _backward

        return out
    
    def log(self):
            out = Value(np.log(self.data),(self,),'log') #對目標取log並轉換為Value的版本
            def _backward():
                self.grad += out.grad/self.data #log_c(f(x))的偏微分為 f'(x)/(f(x)*lnC)
            out._backward = _backward
            return out 
    
    def sum(self,axis = None):
        out = Value(np.sum(self.data,axis = axis), (self,), 'SUM')
        def _backward():
            output_shape = np.array(self.data.shape)
            output_shape[axis] = 1
            tile_scaling = self.data.shape // output_shape
            grad = np.reshape(out.grad, output_shape)
            self.grad += np.tile(grad, tile_scaling)
        
        out._backward = _backward
        return out
    
    def softmax(self):
        out = Value(np.exp(self.data)/np.sum(np.exp(self.data),axis=1)[:,None],(self,),'softmax')
        softmax = out.data
        def _backward():
            s = np.sum(out.grad * softmax, 1)
            t = np.reshape(s, [-1,1])
            self.grad += (out.grad - t)*softmax
        out._backward = _backward
        return out

    def cross_entropy(self,yb):
        guess_p = self.log()
        true_p = yb
        Possibolity = true_p * guess_p
        All_batch_P = Possibolity.sum(axis=1)
        Cross_Entropy_Loss = -1 * All_batch_P.sum()
        return Cross_Entropy_Loss

    def backward(self):

        # topological order all of the children in the graph
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        # go one variable at a time and apply the chain rule to get its gradient
        self.grad = 1
        for v in reversed(topo):
            v._backward()
    
    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"
