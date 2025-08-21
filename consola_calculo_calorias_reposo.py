# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 20:27:32 2025

@author: javie
"""

print("En esta funcion se calcula la cantidad de calorías que una persona quema estando en reposo(esto es, su tasa metabólica basal)")

import calculadora_indices as calc

def ejecutar_calcular_calorias_en_reposo()->None:
    peso=float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura=float(input("Ingrese la altura de la persona (en centimetros): "))
    edad=int(input("Ingrese la edad de la persona: "))
    valor_genero=float(input("Ingrese el genero de la persona: "))
    tmb=calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return print(f"Las calorias que la persona quema estando en estado de reposo son {tmb} cal")

ejecutar_calcular_calorias_en_reposo()