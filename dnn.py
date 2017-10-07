import numpy as np

#softmax function
#input array of integers
#returns an array of P(class i) = e^zi/(e^z1 + e^z2 + ... + e^zn)

def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result