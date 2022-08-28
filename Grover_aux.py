import matplotlib.pyplot as plt
import numpy as np
from numpy import sin,sqrt

seno = lambda w : sin(w*np.linspace(0,2*np.pi,1000))

senos = np.array([seno(w) for w in range(64)])
N = len(senos)
amplitudes = np.array([1]*N)/sqrt(N)

for it in range(1,int(sqrt(N))):
    
    
    senos = np.array([amplitudes[i]*senos[i] for i in range(N)])
    
    plt.figure(figsize=(12,10))
    plt.plot(np.linspace(0,2*np.pi,1000),senos.sum(axis = 0))
    plt.show()

    amplitudes = np.array([1]*(3) + [2*it*sqrt(N)] + [1]*(N - 4) )
    norm_factor = 1/((amplitudes**2).sum())

    amplitudes = norm_factor*amplitudes
    
