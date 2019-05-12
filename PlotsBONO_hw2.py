import numpy as np
import matplotlib.pylab as plt
BONO=np.genfromtxt("BONO.txt",delimiter=",") #importa datos
DATOS=BONO[0:,]
t=DATOS[:,0][0:1000] #separa los tiempos
#extrae en 5 listas correspondientes a una frecuencia especifica, 1000 amplitudes para 20 pisos
W10=DATOS[0:20000][:,3]
W1f=DATOS[0:20000][:,4]

W20=DATOS[20000:40000][:,3]
W2f=DATOS[20000:40000][:,4]

W30=DATOS[40000:60000][:,3]
W3f=DATOS[40000:60000][:,4]

W40=DATOS[60000:80000][:,3]
W4f=DATOS[60000:80000][:,4]

W50=DATOS[80000:100000][:,3]
W5f=DATOS[80000:100000][:,4]
#grafica. la leyenda molesta con 20 colores, se agrupan con un criterio arbitrario en edificios pequeños medianos y altos.
plt.figure(figsize=(20,20))
for n in range(20):
    plt.subplot(5,2,1)
    plt.title("Amplitud en primer piso para w=0.5")
    plt.xlabel("t")
    plt.ylabel("Amplitud")
    if(n<10):
        plt.plot(t,W10[1000*n:1000*(n+1)],"r")
    elif(n<17):
        plt.plot(t,W10[1000*n:1000*(n+1)],"b")
    else:
        plt.plot(t,W10[1000*n:1000*(n+1)],"g")
    
    plt.subplot(5,2,2)
    plt.title("Amplitud en ultimo piso para w=0.5")
    plt.xlabel("t")
    plt.ylabel("Amplitud")
    if(n<10):
        plt.plot(t,W10[1000*n:1000*(n+1)],"r")
    elif(n<17):
        plt.plot(t,W10[1000*n:1000*(n+1)],"b")
    else:
        plt.plot(t,W10[1000*n:1000*(n+1)],"g")
    
    plt.subplot(5,2,3)
    plt.title("Amplitud en primer piso para w=1.0")
    plt.xlabel("t")
    plt.ylabel("Amplitud")
    if(n<10):
        plt.plot(t,W20[1000*n:1000*(n+1)],"r")
    elif(n<17):
        plt.plot(t,W20[1000*n:1000*(n+1)],"b")
    else:
        plt.plot(t,W20[1000*n:1000*(n+1)],"g")
    
    plt.subplot(5,2,4)
    plt.title("Amplitud en ultimo piso para w=1.0")
    plt.xlabel("t")
    plt.ylabel("Amplitud")
    if(n<10):
        plt.plot(t,W2f[1000*n:1000*(n+1)],"r")
    elif(n<17):
        plt.plot(t,W2f[1000*n:1000*(n+1)],"b")
    else:
        plt.plot(t,W2f[1000*n:1000*(n+1)],"g")
    
    plt.subplot(5,2,5)
    plt.title("Amplitud en primer piso para w=1.5")
    plt.xlabel("t")
    plt.ylabel("Amplitud")
    if(n<10):
        plt.plot(t,W30[1000*n:1000*(n+1)],"r")
    elif(n<17):
        plt.plot(t,W30[1000*n:1000*(n+1)],"b")
    else:
        plt.plot(t,W30[1000*n:1000*(n+1)],"g")
    
    plt.subplot(5,2,6)
    plt.title("Amplitud en ultimo piso para w=1.5")
    plt.xlabel("t")
    plt.ylabel("Amplitud")
    if(n<10):
        plt.plot(t,W3f[1000*n:1000*(n+1)],"r")
    elif(n<17):
        plt.plot(t,W3f[1000*n:1000*(n+1)],"b")
    else:
        plt.plot(t,W3f[1000*n:1000*(n+1)],"g")
    
    plt.subplot(5,2,7)
    plt.title("Amplitud en primer piso para w=2.0")
    plt.xlabel("t")
    plt.ylabel("Amplitud")
    if(n<10):
        plt.plot(t,W40[1000*n:1000*(n+1)],"r")
    elif(n<17):
        plt.plot(t,W40[1000*n:1000*(n+1)],"b")
    else:
        plt.plot(t,W40[1000*n:1000*(n+1)],"g")
    
    plt.subplot(5,2,8)
    plt.title("Amplitud en ultimo piso para w=2.0")
    plt.xlabel("t")
    plt.ylabel("Amplitud")
    if(n<10):
        plt.plot(t,W4f[1000*n:1000*(n+1)],"r")
    elif(n<17):
        plt.plot(t,W4f[1000*n:1000*(n+1)],"b")
    else:
        plt.plot(t,W4f[1000*n:1000*(n+1)],"g")
    plt.subplot(5,2,9)
    plt.title("Amplitud en primer piso para w=2.5")
    plt.xlabel("t")
    plt.ylabel("Amplitud")
    if(n<10):
        plt.plot(t,W50[1000*n:1000*(n+1)],"r")
    elif(n<17):
        plt.plot(t,W50[1000*n:1000*(n+1)],"b")
    else:
        plt.plot(t,W50[1000*n:1000*(n+1)],"g")
    
    plt.subplot(5,2,10)
    plt.title("Amplitud en ultimo piso para w=2.5")
    plt.xlabel("t")
    plt.ylabel("Amplitud")
    if(n<10):
        plt.plot(t,W5f[1000*n:1000*(n+1)],"r")
    elif(n<17):
        plt.plot(t,W5f[1000*n:1000*(n+1)],"b")
    else:
        plt.plot(t,W5f[1000*n:1000*(n+1)],"g")
plt.savefig("BONO.pdf")