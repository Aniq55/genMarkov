import numpy as np
from numpy.random import random_sample
from scipy.integrate import quad
import scipy.stats


def choose(choices, weights):
    bins = np.add.accumulate(weights)
    return choices[np.digitize(random_sample(1), bins)][0]

def getP(mu, sigma, N):
    x = np.linspace(0, 1, 100)
    y = scipy.stats.norm.pdf(x, mu, sigma)

    def normal_distribution_function(x):
        value = scipy.stats.norm.pdf(x, mu, sigma)
        return value

    def integral(x1, x2):
        res, _ = quad(normal_distribution_function, x1, x2)
        return res

    p=[]
    for i in range(N):
        p.append(integral(i/N, (i+1)/N))

    p= np.array(p)
    p /= np.float64(p.sum())

    return p
