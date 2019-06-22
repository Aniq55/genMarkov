import numpy as np


class PoissonProcess():

    def __init__(self, L, B, W):
        self.Lambda= L
        self.beta= B
        self.omega= W

    def time_variance(t):
        return self.Lambda + self.beta*np.sin(self.omega*t)

    def interval(self, t):
        return np.random.poisson(self.time_variance(t))
