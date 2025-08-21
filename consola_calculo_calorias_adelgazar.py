# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 20:47:38 2025

@author: javie
"""

import calculadora_indices as calc

print("En esta funcion se calcula el rango de calorías recomendado, que debe consumir una persona diariamente en caso de que desee adelgazar")

def ejecutar_consumo_calorias_recomendado_para_adelgazar ()->None:
    peso=float(input("Ingrese el peso de la persona (en kilogramos): "))
    altura=float(input("Ingrese la altura de la persona (en centimetros): "))
    edad=int(input("Ingrese la edad de la persona: "))
    valor_genero=float(input("Ingrese el genero de la persona en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161: "))
    calorias_minimas, calorias_maximas=calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    return print(f"Para adelgazar es recomendado que consumas entre: {calorias_minimas} y {calorias_maximas} calorías al día")

ejecutar_consumo_calorias_recomendado_para_adelgazar ()