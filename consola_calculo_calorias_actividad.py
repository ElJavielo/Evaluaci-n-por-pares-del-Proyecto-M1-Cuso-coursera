# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 20:36:38 2025

@author: javie
"""

import calculadora_indices as calc

print("En esta funcion se calcula la cantidad de calorías que una persona quema al realizar algún tipo de actividad física (esto es, su tasa metabólica basal según actividad física),")

def ejecutar_calcular_calorias_en_actividad()->None:
    peso=float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura=float(input("Ingrese la altura de la persona (en centimetros): "))
    edad=int(input("Ingrese la edad de la persona: "))
    valor_genero=float(input("Ingrese el genero de la persona en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161: "))
    valor_actividad=float(input("Ingrese el valor de la actividad: "))
    tmb_actividad_fisica=calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    return print(f"Las calorias que la persona quema al realizar alguna actividad fisica son {tmb_actividad_fisica} cal")

ejecutar_calcular_calorias_en_actividad()