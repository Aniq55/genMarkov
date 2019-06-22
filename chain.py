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


CHAIN={}
CHAIN['STATE']=[]
CHAIN['TIME']=[]

CHAIN['STATE'].append(0)
CHAIN['TIME'].append(0)

ITERATIONS= 100
for i in range(ITERATIONS):
    CHAIN['STATE'].append(mm.transition())
    CHAIN['TIME'].append(CHAIN['TIME'][-1] + pp.interval(CHAIN['TIME'][-1]))

import matplotlib.pyplot as plt

plt.plot(CHAIN['TIME'], CHAIN['STATE'])
plt.show()
