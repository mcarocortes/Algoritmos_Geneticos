'''
Fichero con funciones de utilidad
'''
import pandas as pd
import numpy as np
import random

# Carga el CSV de platos ordenados alfabéticamente por nombre
def cargar_platos():
    datos = pd.read_csv('platos.csv')
    return datos

# Guarda los platos en el fichero CSV
def guardar_platos(datos):
    datos.to_csv('platos.csv', index=False)


def filtrar_tipo(datos, tipo):
    # Filtrar los datos por el tipo de plato
    return datos[datos['Tipo'] == tipo].to_dict(orient='records')

restricciones = {
    "tiempo_max": None,
    "precio_max": None,
    "calorias_max": None,
}

def set_restricciones(tiempo, precio, calorias):
    restricciones["tiempo_max"] = tiempo
    restricciones["precio_max"] = precio
    restricciones["calorias_max"] = calorias

def fitness_function(individuo):

    # Restricciones globales
    tiempo_max = restricciones["tiempo_max"]
    precio_max = restricciones["precio_max"]
    calorias_max = restricciones["calorias_max"]

    platos = individuo.alelos

    # Dividir los platos por tipo
    primeros = [p for p in platos if p["Tipo"] == '1']
    segundos = [p for p in platos if p["Tipo"] == '2']
    postres = [p for p in platos if p["Tipo"] == 'P']

    # Validar estructura del menú
    if len(primeros) != 3 or len(segundos) != 3 or len(postres) != 3:
        return -1000  # Penalización máxima si no hay tres platos de cada tipo

    # Penalización por platos repetidos
    penalizacion = 0
    if len(set(tuple(p.items()) for p in primeros)) != len(primeros):
        penalizacion += 50  # Penalización por duplicados en primeros
    if len(set(tuple(p.items()) for p in segundos)) != len(segundos):
        penalizacion += 50  # Penalización por duplicados en segundos
    if len(set(tuple(p.items()) for p in postres)) != len(postres):
        penalizacion += 50  # Penalización por duplicados en postres

    # Calcular los máximos valores por categoría
    max_calorias = (
        max(primero["Calorias"] for primero in primeros)
        + max(segundo["Calorias"] for segundo in segundos)
        + max(postre["Calorias"] for postre in postres)
    )

    max_tiempo = (
        max(primero["Tiempo"] for primero in primeros)
        + max(segundo["Tiempo"] for segundo in segundos)
        + max(postre["Tiempo"] for postre in postres)
    )

    max_costo = (
        max(primero["Coste"] for primero in primeros)
        + max(segundo["Coste"] for segundo in segundos)
        + max(postre["Coste"] for postre in postres)
    )


    # Penalización por exceder restricciones
    if max_calorias > calorias_max:
        penalizacion += (max_calorias - calorias_max) * 10
    if max_tiempo > tiempo_max:
        penalizacion += (max_tiempo - tiempo_max) * 10
    if max_costo > precio_max:
        penalizacion += (max_costo - precio_max) * 10

    # Precio máximo establecido menos el coste total de preparación de la combinación más cara de platos 
    beneficio = precio_max - max_costo

    # Fitness final
    fitness = max(0, beneficio - penalizacion)

    return fitness


