import numpy as np
import matplotlib.pyplot as plt

from markov import *

class PoissonProcess():
    """
    Initiates a Poisson Process object with given Lambda, beta and omega
    (mean interval, swing parameter and fluctuation frequency respectively).
    """
    def __init__(self, L, B, W):
        self.Lambda= L
        self.beta= B
        self.omega= W

    def time_variance(self, t):
        """
        Returns the time variance Lambda + beta * sin(omega * t)
        """
        return self.Lambda + self.beta*np.sin(self.omega*t)

    def interval(self, t):
        """
        Return samples from the Possion distribution as defined by
        time_variance(t). Essentially this gives
        Poisson(Lambda + beta * sin(omega * t)), the state transition intervals.
        """
        return np.random.poisson(self.time_variance(t))


# Poisson process with Lambda = 300, beta = 100, omega = 2pi/1200
pp= PoissonProcess(300, 100, 2*np.pi/1200)
# Markov model with mu = 0.5, sigma = 0.2 and N = 4
mm= MarkovModel(0.5, 0.2, 4)

# Generate the markov chain
CHAIN={}
CHAIN['STATE']=[]
CHAIN['TIME']=[]

# Initiate the State and Time with 0
CHAIN['STATE'].append(0)
CHAIN['TIME'].append(0)

ITERATIONS= 100
for i in range(ITERATIONS):
    CHAIN['STATE'].append(mm.transition())
    CHAIN['TIME'].append(CHAIN['TIME'][-1] + pp.interval(CHAIN['TIME'][-1]))

plt.plot(CHAIN['TIME'], CHAIN['STATE'])
plt.show()
