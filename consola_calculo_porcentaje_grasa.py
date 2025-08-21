# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 20:14:28 2025

@author: javie
"""
import calculadora_indices as calc

print("En esta funcion se calcula el porcentaje de grasa de una persona")

def ejecutar_calcular_porcentaje_grasa()->None:
    peso=float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura=float(input("Ingrese la altura de la persona (en metros): "))
    edad=int(input("Ingrese la edad de la persona: "))
    valor_genero=float(input("Ingrese el genero de la persona: "))
    gc=calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    return print(f"El porcentaje de grasa de la persona es {gc}%")
    # El f alprincipio y el {} sirve para ingresar un resultado como str

ejecutar_calcular_porcentaje_grasa()