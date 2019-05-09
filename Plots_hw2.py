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

t=edificio[0:,][:,0][0:1000]/100
AU_w9=edificio[0:,][10000:11000]
AU11=AU_w9[:,4]
AU12=AU_w9[:,5]
AU13=AU_w9[:,6]
plt.figure()
plt.title("Amplitudes con $\omega=0.639225$")
plt.plot(t,AU11,"r",label="Primer piso")
plt.plot(t,AU12,"g",label="Segundo piso")
plt.plot(t,AU13,"b",label="Tercer piso")
plt.ylabel("Amplitud")
plt.xlabel("t")
plt.legend()
plt.savefig("w9.pdf")

AU_w37=edificio[0:,][38000:39000]
AU21=AU_w37[:,4]
AU22=AU_w37[:,5]
AU23=AU_w37[:,6]
plt.figure()
plt.title("Amplitudes con $\omega=1.74797$")
plt.plot(t,AU21,"r",label="Primer piso")
plt.plot(t,AU22,"g",label="Segundo piso")
plt.plot(t,AU23,"b",label="Tercer piso")
plt.ylabel("Amplitud")
plt.xlabel("t")
plt.legend()
plt.savefig("w37.pdf")

AU_w57=edificio[0:,][58000:59000]
AU31=AU_w57[:,4]
AU32=AU_w57[:,5]
AU33=AU_w57[:,6]
plt.figure()
plt.title("Amplitudes con $\omega=2.53993$")
plt.plot(t,AU31,"r",label="Primer piso")
plt.plot(t,AU32,"g",label="Segundo piso")
plt.plot(t,AU33,"b",label="Tercer piso")
plt.ylabel("Amplitud")
plt.xlabel("t")
plt.legend()
plt.savefig("w57.pdf")

AU_w46=edificio[0:,][47000:48000]
AU41=AU_w46[:,4]
AU42=AU_w46[:,5]
AU43=AU_w46[:,6]
plt.figure()
plt.title("Amplitudes con $\omega=2.10435$")
plt.plot(t,AU41,"r",label="Primer piso")
plt.plot(t,AU42,"g",label="Segundo piso")
plt.plot(t,AU43,"b",label="Tercer piso")
plt.ylabel("Amplitud")
plt.xlabel("t")
plt.legend()
plt.savefig("w46.pdf")