# -*- coding: utf-8 -*-
"""
Created on Wed Oct  29 15:06:35 2023

@author: Doramitzi Herrera
"""

import json

def calcular_imc(estatura, peso):
    # Fórmula del IMC: peso (kg) / estatura (m) ** 2
    imc = peso / (estatura ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "bajo_peso"
    elif 18.5 <= imc < 24.9:
        return "normal"
    elif 25 <= imc < 29.9:
        return "sobrepeso"
    else:
        return "obesidad"

def obtener_plan_nutricional(clasificacion, enfermedad=None):
    with open("planes_nutricionales.json", "r") as file:
        planes_nutricionales = json.load(file)
    
    if clasificacion:
        plan_nutricional = planes_nutricionales.get(clasificacion, None)
        if plan_nutricional:
            print(f"\nPlan Nutricional basado en el IMC: {plan_nutricional['descripcion']}")
            print(f"Recomendaciones de ejercicio: {plan_nutricional['ejercicio']}")
    if enfermedad:
         plan_enfermedad = planes_nutricionales.get(enfermedad, None)
         if plan_enfermedad:
             print(f"\nPlan Nutricional para {enfermedad.capitalize()}: {plan_enfermedad['descripcion']}")
             print(f"Recomendaciones de ejercicio: {plan_enfermedad['ejercicio']}")

# Bucle principal para permitir al usuario calcular el IMC múltiples veces
while True:
    # Obtener datos del usuario
    while True:
        try:
            estatura = float(input("Ingrese su estatura en metros: "))
            peso = float(input("Ingrese su peso en kilogramos: "))
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos para estatura y peso.")

    # Preguntar sobre enfermedades
    enfermedad = input("¿Padece alguna enfermedad? (si/no): ").lower()

    if enfermedad == "si":
        nombre_enfermedad = input("Ingrese el nombre de la enfermedad: ").lower()
    else:
        nombre_enfermedad = None

    # Calcular IMC
    imc = calcular_imc(estatura, peso)

    # Clasificar IMC
    clasificacion = clasificar_imc(imc)

    # Mostrar planes nutricionales
    obtener_plan_nutricional(clasificacion, nombre_enfermedad)

    # Preguntar al usuario si desea calcular el IMC nuevamente
    respuesta = input("¿Desea calcular el IMC nuevamente? (si/no): ").lower()
    if respuesta != "si":
        break  # Salir del bucle principal si la respuesta no es "si"
