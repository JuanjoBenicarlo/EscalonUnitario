
import constantes

from scipy import signal
import matplotlib.pyplot as plt

#Constantes del PID
kp =800000
Ti =0.7
Td =87900

#Funcion del pendulo
funcion_transfer_pendulo = signal.lti([-1], [constantes.BRAZO_PENDULO /constantes.RELACION_PIXELS*(constantes.MASA_PENDULO + constantes.MASA_CARRO), 0, -(constantes.MASA_PENDULO + constantes.MASA_CARRO)*constantes.GRAVEDAD])

#Funcion del pendulo en lazo cerrado con un PID
funcion_control = signal.lti([Td, kp], [constantes.BRAZO_PENDULO/constantes.RELACION_PIXELS*(constantes.MASA_PENDULO + constantes.MASA_CARRO)*Ti,kp*Ti*Td, Ti*(kp-((constantes.MASA_PENDULO + constantes.MASA_CARRO)*constantes.GRAVEDAD)), kp])


t,y = signal.step2(funcion_control)




plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step response')
plt.grid()
plt.show()
