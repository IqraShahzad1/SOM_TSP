import matplotlib.pyplot as plt
import os 



def plot_map(directory, cities, neurons, iteration):
    """
    Generates the required map of cities and neurons at a given moment and
    stores the result in a png image. The map contains all the cities
    represented as red dots and all the neurons as green, crossed by a line
    dots. The method plots the iteration in which the snapshot was taken.
    :param cities: the cities to be plotted, passed as a list of (x, y)
    coordinates
    :param neurons: the cities to be plotted, passed as a list of (x, y)
    coordinates
    :param iteration: the iterations when the snapshot is taken
    :return: returns nothing
    """
    plt.scatter(*zip(*cities), color='red', s=3)
    plt.scatter(*zip(*neurons), color='green', s=2)

    plt.plot(*zip(*(neurons+[neurons[0]])), color='darkgreen')

    # Invert x axis to match representation at
    # http://www.math.uwaterloo.ca/tsp/world/countries.html
    plt.gca().invert_xaxis()
    plt.gca().set_aspect('equal', adjustable='datalim')

    plt.title('Iteration #{:06d}'.format(iteration))
    plt.axis('off') 
    plt.savefig('{}/{}.png'.format(directory, iteration))
    plt.clf() 