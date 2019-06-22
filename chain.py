import numpy as np
from markov import *

class PoissonProcess():

    def __init__(self, L, B, W):
        self.Lambda= L
        self.beta= B
        self.omega= W

    def time_variance(self, t):
        return self.Lambda + self.beta*np.sin(self.omega*t)

    def interval(self, t):
        return np.random.poisson(self.time_variance(t))


pp= PoissonProcess(300, 100, 2*np.pi/1200)
mm= MarkovModel(0.5, 0.2, 4)


CHAIN=[]
CHAIN.append((0,0))

ITERATIONS= 10
for i in range(ITERATIONS):
    CHAIN.append( (mm.transition(), pp.interval(CHAIN[-1][1]) ) )

print(CHAIN)
