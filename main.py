
import constantes

from scipy import signal
import matplotlib.pyplot as plt



#Funcion del pendulo
funcion_transfer_pendulo = signal.lti([-1], [constantes.BRAZO_PENDULO /constantes.RELACION_PIXELS*constantes.MASA_CARRO, 0, -(constantes.MASA_PENDULO + constantes.MASA_CARRO)*constantes.GRAVEDAD])


#Constantes del PID
kp =800.25
Ti =3
Td =87.9

kp=kp*1000
Ti=Ti*1000
Td=Td*1000


#Funcion del sistema realimentado en lazo cerrado con PID
funcion_control_PID = signal.lti([-Ti*Td, -kp*Ti, -1], [constantes.BRAZO_PENDULO/constantes.RELACION_PIXELS*constantes.MASA_CARRO*Ti, Ti*Td, Ti*(kp-((constantes.MASA_PENDULO + constantes.MASA_CARRO)*constantes.GRAVEDAD)), 1])


t,y = signal.step2(funcion_transfer_pendulo)




plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step response')
plt.grid()
plt.show()
