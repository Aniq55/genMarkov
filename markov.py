import numpy as np
from utils import *


class MarkovModel():
    """
    Produces a Markov model with mu, sigma and N states
    """

    def __init__(self, mu, sigma, N):
        self.prob= getP(mu, sigma, N)
        self.N_states= N
        self.current_state= 0
        self.states= np.array(list(range(self.N_states)))

    def transition(self):
        self.current_state =  choose(self.states , self.prob)
        return self.current_state

    def draw(self):
        """
        Drawing from a uniform probability distribution in the range of
        x_i, i.e., r ∼ U(x_i). r denotes the reward.
        Note the definition of x_i here, x_i ∈[(i − 1) / N , i / N). However,
        we have used 0-based indexing in the code.
        """
        return np.random.uniform(self.current_state/ self.N_states, (self.current_state+1)/ self.N_states)


# import matplotlib.pyplot as plt
# import numpy as np
# plt.hist(X, bins=mm.N_states, normed= True)
# plt.show()
