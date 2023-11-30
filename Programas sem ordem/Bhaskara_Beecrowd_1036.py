# -*- coding: iso-8859-1 -*-

from math import sqrt

texto = input('')
lista = texto.split()
a = float(lista[0])
b = float(lista[1])
c = float(lista[2])

DELTA = b**2 - 4*a*c

if DELTA < 0:
    print("Impossivel calcular.")
else:
    if a == 0:
        print("Impossivel calcular.")
    else:
        X1 = (-b + sqrt(DELTA)) /(2*a)
        X2 = (-b - sqrt(DELTA)) / (2*a)
        print(f"R1 = {X1:.5f}\nR2 = {X2:.5f}")
