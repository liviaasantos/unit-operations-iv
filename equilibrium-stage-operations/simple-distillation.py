
"""
@author: Livia Alves Santos
"""

"""
Uma mistura gasosa a 1,0 atm de pressão absoluta, que contem ar e CO2, está em contato em um estágio simples de
mistura contínua com água pura a 293 K. As duas correntes de saída gasosa e líquida atingem o equilíbrio. O fluxo de
gás de entrada é 100 kgmol/h, com uma fração molar de CO2 de yA2 = 0,20. O fluxo de líquido alimentado é 300 kgmol
água/h. Calcule a quantidade e a composição das duas saídas. Considere que a água não vaporiza para a fase gasosa.
"""

from sympy import Symbol
from sympy import solve

## Balanço de massa por componente (CO2)

#Fluxo em kmol, usando 1 hora como base de cálculo
L_0 = 300
L_1 = 300
V_1 = 100
V_2 = 100

y_CO2 = 0.2

P = float(input("Insira a pressão do sistema em atm: "))

# Balanço: 100 * y_1 = 100 * 0.2 - 300 * x_1
# y_1 = 0.2 - 3 * x_1

# Pela lei de Henry: y_a * P = H * x_a

# Assim, o balanço fica: H * x_1 =0.2 * P - 3 * x_1 * P

H = 0.142*10**4 #atm/fração molar

# Coeficientes da equação

a = 1+(3*P)/H
b = 0.2*P/H

x = Symbol('x_1')


x_CO2 = round(solve(a*x - b,x)[0],7)
y_CO2 = round(H * x_CO2,7)
x_H2O = round(1 - x_CO2,7)
y_ar = round(1 - y_CO2,7)

print("\nComposição do vapor: " + str(y_CO2) + " de CO2 e " + str(y_ar) + " de ar")
print("\nComposição do líquido: " + str(x_CO2) + " de CO2 " + str(x_H2O) + " de água")




