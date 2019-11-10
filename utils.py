import numpy as np
from numpy.random import random_sample
from scipy.integrate import quad
import scipy.stats


def choose(choices, weights):
    bins = np.add.accumulate(weights)
    return choices[np.digitize(random_sample(1), bins)][0]

def getP(mu, sigma, N):
    """
    Returns the probablities (p_i) as defined in the section III, they are used
    to generate the transition probability matrix.

    The values mu and sigma are used for obtaining the pdf.
    """
    x = np.linspace(0, 1, 100)
    y = scipy.stats.norm.pdf(x, mu, sigma)

    def normal_distribution_function(x):
        """
        Returns a pdf of a normal distribution function with defined mu and
        sigma
        """
        value = scipy.stats.norm.pdf(x, mu, sigma)
        return value

    def integral(x1, x2):
        """
        Integrates `normal_distribution_function` (defined above) between x1
        and x2. This is used tp generate the probabilities.
        """
        res, _ = quad(normal_distribution_function, x1, x2)
        return res

    p=[]
    for i in range(N):
        p.append(integral(i/N, (i+1)/N))

    p= np.array(p)
    p /= np.float64(p.sum())

    return p
