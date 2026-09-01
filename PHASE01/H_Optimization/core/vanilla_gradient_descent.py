class GradientDescent:
    def __init__(self, lr=0.001):
        self.lr = lr

    def step(self, params, grads):
        """
        this is calculated using the general formula for gradeints
        we come to know here that how p effects the L(Loss)
        """
        L = [p - self.lr * g for p, g in zip(params, grads)]
        return L
