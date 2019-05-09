import numpy as np
import matplotlib.pylab as plt
edificio=np.genfromtxt("edificio.txt",delimiter=",")
data1=edificio[0:,][0:1000]
W=[]
U1max=[]
U2max=[]
U3max=[]
for n in range(100):
    rango=edificio[0:,][1000*(n+1):1000*(n+2)]
    u1=max(abs(rango[:,4]))
    u2=max(abs(rango[:,5]))
    u3=max(abs(rango[:,6]))
    w=rango[:,7][0]
    W.append(w)
    U1max.append(u1)
    U2max.append(u2)
    U3max.append(u3)
    
plt.figure(figsize=(20,10))
plt.title("Amplitud en función de las frecuencias")
plt.plot(W,U1max,"r",label="primer piso")
plt.plot(W,U2max,"g",label="segundo piso")
plt.plot(W,U3max,"b",label="tercer piso")
plt.xlabel("$\omega$")
plt.ylabel("Amplitud")
plt.legend()
plt.savefig("U_vs_freq.pdf")