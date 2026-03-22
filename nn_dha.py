import random
from nn_engine import Value


class Module:
    def parameters(self):
        return []
    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0

class Neuron(Module):
    def __init__(self, nin, non_lin=True):
        self.w = [Value(random.uniform(-1, 1)) for _ in range(nin)]
        self.b = Value(0)
        self.non_lin = non_lin

