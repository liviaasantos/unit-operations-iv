"""
@author: Livia Alves Santos
"""

import matplotlib.pyplot as plt
from prettytable import PrettyTable

T = [68.7, 79.4, 93.3, 107.2, 125.7]
P_a = [101.3, 136.7, 197.3, 284, 456]
P_b = [16.1, 23.1, 37.1, 57.9, 101.3]
i = 0
x_a = []
y_a = []
P = 101.325

print("\nOs dados de pressão de vapor para a mistura hexano-octano são apresentados na Tabela 1, onde A é o hexano e B o octano:")

x = PrettyTable(["Temperatura (°C)", "Pressão de vapor A (kPa)", "Pressão de vapor B (kPa)"])
x.add_row([68.7, 101.3, 16.1])
x.add_row([79.4, 136.7, 23.1])
x.add_row([93.3, 197.3, 37.1])
x.add_row([107.2, 284, 57.9])
x.add_row([125.7, 456, 101.3])

print(x)

print('Montar o diagrama de ponto de ebulição (T versus composição ou T versus x e y) para esse sistema.')

while i < len(T):
    #calculando composição de x_a
    w = (P - P_b[i])/(P_a[i] - P_b[i])
    #calculando composição de y_a
    t = (w * P_a[i])/P
    
    i += 1
    
    x_a.append(w)
    y_a.append(t)

# 300 represents number of points to make between x_a.min and x_a.max

plt.plot(x_a, T, 'g', label=r'$x hexano$', linewidth=2)
plt.plot(y_a, T, 'r', label=r'$y hexano$', linewidth=2)
plt.legend(loc='best')
plt.xlabel('x / y')
plt.ylabel('T')
plt.title('T vs x e y')
plt.show()

    
