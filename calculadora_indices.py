# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 14:55:26 2025

@author: javie
"""

def calcular_IMC(peso:float, altura:float)->float:
    imc=peso/(altura**2)
    return round(imc, 2)

#la altura debe ser en metros

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float)->float:
    gc=1.2*calcular_IMC(peso, altura)+0.23*edad-5.4-valor_genero
    return round(gc, 2)

#la altura debe ser en metros

def calcular_calorias_en_reposo(peso:float, altura:float, edad:int, valor_genero:float)->float:
    tmb=(10*peso)+(6.25*altura)-(5*edad)+valor_genero
    return tmb

#la altura debe ser en centimetros

def calcular_calorias_en_actividad(peso:float, altura:float, edad:int, valor_genero:float,   valor_actividad:float)->float:
    tmb_actividad_fisica= calcular_calorias_en_reposo(peso, altura, edad, valor_genero) *valor_actividad
    
    return round(tmb_actividad_fisica,2)


def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int, valor_genero:float)->str:
     calorias_minimas=(calcular_calorias_en_reposo(peso, altura, edad, valor_genero) *80)/100
     calorias_maximas=(calcular_calorias_en_reposo(peso, altura, edad, valor_genero) *85)/100
     return round(calorias_minimas,2),  round(calorias_maximas,2)


