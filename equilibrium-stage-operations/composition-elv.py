# -*- coding: utf-8 -*-
"""

@author: Livia Alves Santos
"""

from prettytable import PrettyTable

print("Calcule as composições do vapor e do líquido em equilíbrio a 95°C (368,2 K) para benzeno (A) - tolueno (B) usando a pressão de vapor da tabela abaixo a 101,32 kPa.")

x = PrettyTable(["Temperatura (°C)", "Pressão de vapor A (kPa)", "Pressão de vapor B (kPa)"])
x.add_row([80.1, 101.32, 0])
x.add_row([85, 116.9, 46])
x.add_row([90, 135.5, 54])
x.add_row([95, 155.7, 63.3])
x.add_row([100, 179.2, 74.3])
x.add_row([105, 204.2, 86])
x.add_row([100.6, 240, 101.32])

print(x)

T_table = [80.1, 85.0, 90.0, 95.0, 100.0, 105.0, 100.6]
P_a_table = [101.32, 116.9, 135.5, 155.7, 179.2, 204.2, 240]
P_b_table = [0, 46, 54, 63.3, 74.3, 86, 101.32]
P_a = 0
P_b = 0

i = 0
P = 101.32
T = float(input("Digite a temperatura do sistema em °C, dentre as presentes na tabela: "))

for T_type in T_table:
    if (T_type == T):
        P_a = P_a_table[i]
        P_b = P_b_table[i]
    i += 1
    
x_a = (P - P_b)/(P_a - P_b)
y_a = x_a * P_a / P
x_b = 1 - x_a
y_b = 1 - y_a

print("Composição do vapor: ", round(y_a,3), " de Benzeno e ", round(y_b, 3), " de Tolueno")
print("Composição do líquido: ", round(x_a,3), " de Benzeno e ", round(x_b, 3), " de Tolueno")
        