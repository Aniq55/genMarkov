import numpy as np
from tpmatrix import *
from numpy.random import random_sample

def choose(choices, weights):
    bins = np.add.accumulate(weights)
    return choices[np.digitize(random_sample(1), bins)]


class MarkovModel():

    def __init__(self, mu, sigma, N):
        self.prob= getP(mu, sigma, N)
        self.N_states= N
        self.current_state= 0
        self.states= np.array(list(range(self.N_states)))

    def transition(self):
        self.current_state =  choose(self.states , self.prob)


mm= MarkovModel(0.5, 0.5, 4)

for i in range(10):
    mm.transition()
    print(mm.current_state)
