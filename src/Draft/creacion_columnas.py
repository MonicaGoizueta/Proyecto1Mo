import pandas as pd
import numpy as np
import sidetable
import pymongo

import folium
import seaborn as sns
import matplotlib.pyplot as plt

from geopy.geocoders import Nominatim

def calcular_precio_por_m2 (x, y):
    div = x/y
    return div
    '''
    Calcula el precio de la vivienda dividido por los metros cuadrados que tenga la vivienda
    Args: 2 parámetros
        parametro1 (int): price
        parámetro2 (int): building_space
    Returns:
        nos devuelve el precio por metro cuadrado
    '''

def puntos2(df, x):
    for i in x:
        df[i] = df [i].replace(",",".")
        df[i] = pd.to_numeric(df[i], errors = "coerce").astype(float)
    return df
    '''
    Sustituye las comas por puntos
    Args: 1 parámetro
        parametro1 (object): va a recibir un parámetro, que puede ser una lista de columnas
    Returns:
        nos devuelve floats, actualizando el string susrtituyendo las comas por puntos
    '''

def quitar_horas(x): 
    try:
        return x.split()[0]
    except: 
        return x
    '''
    separa el string por espacios y se queda con la primera palabra
    Args: 1 parámetros
        parametro1 (str): ad_situation
    Returns:
        nos devuelve lo que se muestra del string antes del primer espacio
    '''
    
def cambiar(x):
    if x == "WA":
        return x.replace("WA", "Washington")

    elif  x == "OR":
        return x.replace("OR", "Oregón")

    else:
        return x.replace("CA", "California")
    '''
    Reemplaza sílabas por palabras
    Args: 1 parámetro
        parametro1 (object): State
    Returns:
        nos devuelve Washington, Oregómn y California, en vez de poner WA, OR, CA
    '''

def latitud_v2 (x):
    locator = Nominatim(user_agent= "myGeocoder")
    try:
        
        location = locator.geocode (x)
        return location.latitude
        
    except:
        return None
    '''
    Nos proporciona la latitud del parámetro que le pasemos
    Args: 1 parámetro
        parametro1 (int): Código postal
    Returns:
        La latitud del código postal
    '''

def longitud_v2 (x):
    locator = Nominatim(user_agent= "myGeocoder")
    try:
        
        location = locator.geocode (x)
        return location.longitude
        
    except:
        return None
    
    '''
    Nos proporciona la longitud del parámetro que le pasemos
    Args: 1 parámetro
        parametro1 (int): Código postal
    Returns:
        La longitud del código postal
    '''