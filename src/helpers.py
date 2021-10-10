import abc 
import numpy as np
import math

class DecayFunction(metaclass=abc.ABCMeta):
    """
    Base class for decay functions, implemented with a strategy design pattern
    """
    def __init__(self, init_value):
        self._value = init_value

    @property
    def value(self):
        return self._value
  
    @abc.abstractmethod
    def decay(self):
        pass



class LinearDecay(DecayFunction):
    """
    Decaying with a constant rate
    """
    def __init__(self, start_value, rate):
        self.rate = rate
        super().__init__(start_value)

    def decay(self):
        self._value -= self.rate


class ExponentialDecay(DecayFunction):
    """
    Decaying exponential.
    """
    def __init__(self, start_value, rate):
        self.rate = rate
        super().__init__(start_value)

    def decay(self):
        self._value *= self.rate 
        
        


def euclidean_distance_2d(x, y):
    return math.sqrt(pow(y[0]-x[0],2) + pow(y[1]-x[1],2))


def euclidean_distance_1d(x, y):
    return abs(x-y)


def euclidean_distance_1d_circular(n, i, j):
    """
    Calculates 1d distance of integers i and j in a circle of n elements.
    :param n: Circle length
    :param i: Start element
    :param j: Target element
    :return: Minimal distance
    """
    d = euclidean_distance_1d(i, j)
    return min(d, n-d)



def gaussian(d, sigma):
    p = sigma**2
    if p == 0:
        return 0
    return math.exp(-d**2/(2*p))


def bubble(d, sigma):
    if d <= sigma:
        return 1 
    return 0 