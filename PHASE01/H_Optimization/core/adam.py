class Adam:
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = None
        self.v = None
        self.t = 0

    def step(self, params, grads):
        """
        In adam optimizer we give steps to weights according to the frequency
        High frequecy/higher gradient - small steps
        Low frequency/smaller gradient - bigger steps
        """
        if self.m is None:
            self.m = [0.0] * len(params)
            self.v = [0.0] * len(params)

        self.t += 1

        self.m = [self.beta1 * m + (1 - self.beta1) * g for m, g in zip(self.m, grads)]
        self.v = [
            self.beta2 * v + (1 - self.beta2) * g**2 for v, g in zip(self.v, grads)
        ]

        m_hat = [m / (1 - self.beta1**self.t) for m in self.m]
        v_hat = [v / (1 - self.beta2**self.t) for v in self.v]

        return [
            p - self.lr * mh / (vh**0.5 + self.epsilon)
            for p, mh, vh in zip(params, m_hat, v_hat)
        ]
