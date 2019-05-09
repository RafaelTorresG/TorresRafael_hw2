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

#Haga una grafica de las transformadas de Fourier de ambas seniales.
#Esta grafica debe ser en funcion de las frecuencias (bono si no usa el paquete fftfreq.
#Indique esto con un mensaje en la terminal.)

d=(t[1]-t[0])
freq=np.fft.fftfreq(len(sig),d)
plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.plot(freq,sigSum_trans,"r")
plt.title("Transformada Seniales sumadas")
plt.ylim(-1,10)
plt.xlabel("Tiempo")
plt.ylabel("Senial")

plt.subplot(1,2,2)
plt.plot(freq,sig_trans,"b")
plt.title("Transformada Seniales seguidas")
plt.xlabel("Tiempo")
plt.ylabel("Senial")

plt.savefig("PlotTransFourier2.pdf")

#Usando el paquete matplotlib.pyplot.specgram (ver: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.specgram.html) haga un espectrograma de las dos seniales.
plt.figure()
plt.specgram(senialSum, NFFT=256, Fs=100)
plt.title("Espectrograma senial sumada")
plt.xlabel("t")
plt.ylabel("Frecuencia")
plt.savefig("specgram1.pdf")

plt.figure()
plt.specgram(senial, NFFT=256, Fs=100)
plt.title("Espectrograma senial seguida")
plt.xlabel("t")
plt.ylabel("Frecuencia")
plt.savefig("specgram2.pdf")

#Almacene los datos de temblor.txt. Estos datos son datos reales de una senial sismica
temblor=np.genfromtxt("temblor.txt")
tTemb=np.linspace(0,900.01,len(temblor))

#Haga una grafica de la senial en funcion del tiempo.
plt.figure(figsize=(30,10))
plt.plot(tTemb,temblor,"r",label="Senial recibida")
plt.xlabel("tiempo")
plt.ylabel("Senial del temblor transformada")
plt.legend()
plt.savefig("PlotFourier3.pdf")

#Haga la transformada de Fourier de la senial usando paquetes de scipy y grafiquela
from scipy.fftpack import fft
from scipy.fftpack import ifft
TransTemblor=fft(temblor)
freqTemblor=np.fft.fftfreq(len(temblor),0.01)

plt.figure(figsize=(30,10))
plt.plot(freqTemblor,TransTemblor,"g",label="Senial transformada")
plt.xlabel("frecuencias")
plt.ylabel("Senial del temblor")
plt.legend()
plt.savefig("PlotFourier4.pdf")

#haga un espectrograma de la senial
plt.figure()
plt.specgram(temblor, NFFT=256, Fs=100)
plt.title("Espectrograma temblor")
plt.xlabel("t")
plt.ylabel("Frecuencia")
plt.savefig("specgramTemblor.pdf")