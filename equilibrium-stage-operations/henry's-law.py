"""
@author: Livia Alves Santos | liviaalveseq@gmail.com
"""

"""
Qual deve ser a concentração de oxigênio dissolvido em água a 278K quando a solução
está em equilíbrio com ar na pressão total de 1 atm?

A constante da lei de Henry é 4.38*10^4 atm/fração molar
"""

# Calcular pressão parcial

H = 4.38*10**4
P = float(input("Insira a pressão total do sistema em atm: "))
y_O2 = 0.21
P_O2 = y_O2 * P

# Calcular xa de O2

x_O2 = P_O2 / H # [mol de O2/mol de solução]

# Calcular massa de O2 que está dissolvida na água

m_O2 = x_O2 * 32

# Calcular concentração de O2 na solução

c_O2 = (m_O2 * 100) / 18

print("A concetração de oxigêncio dissolvido em água a 298K é: " + str(round(c_O2,5)) + " (% m/m)")