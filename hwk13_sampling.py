#by Kay Towner

import math
import random
import numpy as np
import matplotlib.pyplot as plt

#Function to intigrate over:
def integral(x=None):
    """The integral to create a value from"""
    return (x**(-1/2)) / (np.exp(x)+1)

def p(x=None):
    """Probibility distribution function"""
    return 1 / 2*np.exp(x)

def w(x=None):
    """The function of w(x)"""
    return x**(-1/2)

def importsamp(N=None):
    """Importance sampling formula:"""
    a=0
    b=1
    sumNum = 0
    for i in range(N):
        x = random.uniform(0,1)
        sumNum += integral(x=x)
    return (1/N) * (sumNum/w(x=x)) * (b - a)


if __name__ == "__main__":
    N = 1000000 #sample a million
    x = np.random.uniform(0,1) #random # generator, 0 and 1
    randoms = np.random.random(10000) 

    #Show probability distribution p(x):
    probDis = p(x=randoms)
    print("The Probability Func Values:" ,probDis)
    #Get a random number between 0 and 1:
    randNumGen = random.uniform(0,1)
    print("The Random Number Generated Is:", randNumGen)
    #importance sampling:
    importance = importsamp(N=N)
    print("The Importance Values",importance)


    #PLOTTING: (just for visualization)_____________________

    #the Probibily dist graph:
    plt.hist(probDis, bins=10,density=True)
    plt.hist(importance, bins=10,density=True)
    plt.title("Probibility Dist. Graph")
    plt.show()







