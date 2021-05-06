#by Kay Towner

import math
import random
import numpy as np
import matplotlib.pyplot as plt

#Values:
N = 10000
x = np.random.random(10000) #generated random samples
gamma = 1

def CDF(x, x0=None, gamma=None):
    """Function is the CDF of random_couchy
    gamma = width-dist
    orig: (1/np.pi)*math.atan(((x-x0)/gamma)+(1/2))"""
    return (gamma*np.tan(np.pi*(x-(1/2))))+x0


def random_cauchy(N, x0=None, gamma=None):
    """Function of the random distribution, x0=mean"""
    randomNums = []
    inversList = []
    for i in range(N):
        x = np.random.random(0,1)
        randomNums.append(x)
        invers = CDF(x=x, x0=0,gamma=gamma)
        inversList.append(invers)
    return randomNums, inversList


if __name__ == "__main__":
    xs = np.arange(-40, 40, 0.1)
    ys = CDF(x=xs, x0=0, gamma=gamma)
      
    randomNums = random_cauchy(N=x, x0=0, gamma=gamma)   
    inversList = random_cauchy(N=x, x0=0, gamma=gamma)
    

#PLOTTING______________________________________________
    
    #graphing the CDF
    plt.plot(xs, ys)#pdf plotted
    plt.hist(randomNums, bins=100, alpha=0.5, density=True)
    plt.hist(inversList, bins=100, alpha=0.5, density=True)
    
    plt.ylabel('distribution density')
    plt.xlabel('points(x)')
    plt.title("CDF: True vs Calculated")
    plt.show()
