import numpy as np
import matplotlib.pylab as plt

#Almacene los datos de signalSuma.dat y de signal.dat. Estas dos seniales estan conformadas por dos ondas sinusoidales. En el primer caso la #senial es la suma de las dos ondas,
#en el segundo la senial esta conformada por, primero una de las ondas y luego la siguiente.
sigSum=np.genfromtxt('signalSuma.dat')
sig=np.genfromtxt('signal.dat')

#Haga una grafica con dos subplots uno con los datos de signal.dat y otro con los de signalSuma.dat.
#Desagregar tiempo y senial
tSum=sigSum[:,0]
senialSum=sigSum[:,1]

t=sig[:,0]
senial=sig[:,1]

plt.figure()
plt.subplot(1,2,1)
plt.plot(tSum,senialSum)

plt.figure()
plt.subplot(1,2,2)
plt.plot(t,senial)

plt.savefig("PlotFourier1.pdf")