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

plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.plot(tSum,senialSum,"r")
plt.title("Seniales sumadas")
plt.xlabel("Tiempo")
plt.ylabel("Senial")

plt.subplot(1,2,2)
plt.plot(t,senial,"b")
plt.title("Seniales seguidas")
plt.xlabel("Tiempo")
plt.ylabel("Senial")

plt.savefig("PlotFourier1.pdf")


#Haga la transformada de Fourier de ambas seniales usando su implementacion propia de la transformada discreta de fourier
def fourier(M):
    F=[]
    n=len(M)
    for i in range(n):
        s=0
        for k in range(n):
            s+=M[k]*np.exp((-1j)*2*np.pi*k*((i*1.0)/n))
        F.append(s)
    return (F)
###Transformadas
sigSum_trans=fourier(sigSum)
sig_trans=fourier(sig)