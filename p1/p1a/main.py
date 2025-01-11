import numpy as np
import matplotlib.pyplot as plt

from math import sqrt
from scipy.odr import *

ypoints = [0, 0.9873, 1.9795, 2.9765, 3.9736, 4.9707, 5.0000] # TENSÕES MEDIDAS
xpoints = [0, 300, 600, 900, 1200, 1500, 1510] # VALORES DAS RESISTÊNCIAS

current = (ypoints[6] - ypoints[5])/10
print("corrente medida: ", current)


# PLOT
y = ypoints
x = xpoints

m = 0.05*300
y_err = [5/1023]*7
x_err = [0.000001, m, sqrt(2)*m, sqrt(3)*m, 2*m, sqrt(5)*m, sqrt(5*m**2 + 0.01)]

print(sqrt(5)*m)
exit()


def linear_func(p, x):
    m, c = p
    return m * x + c

linear_model = Model(linear_func)
data = RealData(x, y, sx=x_err, sy=y_err)
odr = ODR(data, linear_model, beta0=[1., 0.])
out = odr.run()

x_fit = np.linspace(min(x), max(x), 1000)
y_fit = linear_func(out.beta, x_fit)

# plot
plt.errorbar(x, y, xerr=x_err, yerr=y_err, linestyle='None', marker='+', label='Medições com incertezas')
plt.plot(x_fit, y_fit, label='Ajuste linear', color='red')

plt.xlabel("Resistência (Ω)")
plt.ylabel("Tensão (V)")
plt.legend()
plt.savefig("VxR.png", dpi=300)
plt.show()



ang_coef = (y_fit[len(y_fit) - 1] - y_fit[0])/(x_fit[len(x_fit) - 1] - x_fit[0])
print("coeficiente angular do ajuste linear: ", ang_coef)


'''

Cálculo das resistências (CALIBRAÇÃO DOS RESISTORES DE 300)

'''
ypoints = [0, 0.9873, 1.9795, 2.9765, 3.9736, 4.9707, 5.0000]

print("\n Tensões:")

q1 = ypoints[1] - ypoints[0]
q2 = ypoints[2] - ypoints[1]
q3 = ypoints[3] - ypoints[2]
q4 = ypoints[4] - ypoints[3]
q5 = ypoints[5] - ypoints[4]

print("q1: ", q1)
print("q2: ", q2)
print("q3: ", q3)
print("q4: ", q4)
print("q5: ", q5)

print("\n Resistências:")

r1 = q1 / ang_coef
r2 = q2 / ang_coef
r3 = q3 / ang_coef
r4 = q4 / ang_coef
r5 = q5 / ang_coef

print("r1: ", r1)
print("r2: ", r2)
print("r3: ", r3)
print("r4: ", r4)
print("r5: ", r5)