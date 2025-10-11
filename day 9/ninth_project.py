import os 
import re
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = '/Users/diegovelazquez/Documents/Mi_Gran_Directorio'

mi_patron = r'N\D{3}-\d{5}'
fecha_hoy = datetime.date.today()
numeros_encontrados = []
archivos_encontrados = []

def buscar_numero(archivo, patron):
    archivo = open(archivo,'r')
    texto = archivo.read()

    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ''
    
def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a),mi_patron)
            if resultado != '':
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())
    
def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Busqueda: {fecha_hoy.day}/{fecha_hoy.month}/{fecha_hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f'{a}\t{numeros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Numeros encontrados: {len(numeros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)

crear_listas()
mostrar_todo()


