#!/usr/bin/env python
'''
Institut Icària
Programació - 1r Batxillerat - Curs 2024-25
Descripció llarga del programa. Indicar que fa el
programa i el resultat esperat.
'''
__author__ = "Ilyas Bouaid"
__email__ = "ibouaid@instituticaria.cat"
__date__ = "30/10/2009"

Dividend = int(input("Ingresar dividend"))
Divisor = int(input("Ingresar divisor"))
Quocient = (Dividend)//(Divisor)
Residu = (Dividend) % (Divisor)
print(f"Divisió: {Dividend}/{Divisor}")
print(f"Quocient: {Quocient}")
print(f"Residu: {Residu}")
