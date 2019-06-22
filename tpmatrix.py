import numpy as np
from getprob import *

def genMatrix(p_vector):
    N= len(p_vector)
    M=[]
    for j in range(N):
        M.append(p_vector)
    M= np.array(M)
    return M


print(genMatrix(getP(0.5, 0.3, 4)))
