# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 19:36:15 2025

@author: javie
"""

import calculadora_indices as calc

print("En esta funcion se calcula el índice de masa corporal de una persona")

def ejecutar_calcular_IMC()->None:
    peso=float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura=float(input("Ingrese la altura de la persona (en metros): "))
    IMC=calc.calcular_IMC(peso, altura)
    return print("El IMC de la persona es: ",IMC)

ejecutar_calcular_IMC()