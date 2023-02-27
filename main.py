# para H(s) = K / ((s/w0)+1)
import constantes

from scipy import signal
import matplotlib.pyplot as plt

import random
from control import *
from control.matlab import *

#import numpy as np



#kp =47.730321342110116
#Ti =0.22498303939937347
#Td =38.23503303643766
#kp =33.37927658476574
#Ti =0.11233938325347914
#Td =55.40990901610341
#kp =72.81133838667631
#Ti =0.006073211551112734
#Td =0.3894354372943942
#Td =38.94354372943942

#este es el que tengo
kp =800
Ti =100/0.3
Td =88

#este hace el sistema estable
kp =7800
Ti =100/0.3
Td =9900


#kp =0.865151570233651
#Ti =0.0020356216237229054
#Td =810.9146381122296

funcion_transfer_pendulo = signal.lti([-1], [constantes.BRAZO_PENDULO /constantes.RELACION_PIXELS*(10+200), 0, -(10+100)*constantes.GRAVEDAD]) # Creamos el sistema
#funcion_transfer_pendulo = signal.lti([-1], [constantes.BRAZO_PENDULO*100, 0, -(10+100)*constantes.GRAVEDAD]) # Creamos el sistema

funcion_control = signal.lti([Td, kp], [constantes.BRAZO_PENDULO*(10+100)*Ti,kp*Ti*Td, Ti*(kp-((10+100)*constantes.GRAVEDAD)), kp])
#funcion_control = signal.lti([kd, kp], [constantes.BRAZO_PENDULO*100,-kd, -((10+100)*constantes.GRAVEDAD)- kp])


t,y = signal.step2(funcion_transfer_pendulo)
average = sum(abs(y))/len(y)
print(average, sum(abs(y)),len(y))


plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step response')
plt.grid()
plt.show()








contador = 0
while contador < 55000:
    kp = random.uniform(0.2,10.0)
    Ti = random.uniform(0.0,0.2)
    Td = random.uniform(0.9,100.0)

    funcion_control = signal.lti([kp * Ti * Td, kp * Ti, kp],
                                 [constantes.BRAZO_PENDULO / constantes.RELACION_PIXELS * (10 + 200) * Ti,
                                  kp * Ti * Td, Ti * (kp - ((10 + 100) * constantes.GRAVEDAD)), kp])

    t,y = signal.step2(funcion_control)
    contador += 1
    average = sum(abs(y)) / len(y)
    #if ((len(t) > 120) or ((y[99]>0.5) and y[99]< 5)) :
    if (average >-70 and average < 70) :
        #plt.plot(t, y)
        #plt.xlabel('Time [s]')
        #plt.ylabel('Amplitude')
        #plt.title('Step response')
        #plt.grid()
        #plt.show()
        print (kp, Ti , Td, len(t), y[99])
        break
    print (contador, len(t), y[99], average)
