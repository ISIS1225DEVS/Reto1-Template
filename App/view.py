﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import copy
import sys
from os import X_OK

import config as cf
import controller

from DISClib.ADT import list as lt

assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas por un rango de años")
    print("3- Listar cronológicamente las adquisiciones")

def printListOptions():
    print("Seleccione la implementación de las listas del catálogo")
    print("1- ARRAY_LIST")
    print("2- SINGLE_LINKED")

def printSortOptions():
    print("Seleccione con qué tipo de implementación desea organizar la lista")
    print("1- Insertion")
    print("2- Shell")
    print("3- Merge")
    print("4- Quick")

def initCatalog(implementation):
    """
    Inicia el catálogo de obras
    """
    return controller.initCatalog(implementation)

def loadData(catalog):
    """
    Carga las obras en la estructura de datos
    """
    controller.loadData(catalog)

def selectSample(catalog, sample):
    """
    Selecciona una muestra de los datos de la longitud que indique el parámetro sample
    """
    return controller.selectSample(catalog, sample)

def sortArtworksByDate(catalog, implementation, initial_year, end_year):
    """
    Ordena las obras en el rango de fechas dispuesto
    """
    return controller.sortArtworksByDate(catalog, implementation, initial_year, end_year)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:

        printListOptions()
        option = input("Seleccione una opción para continuar\n")
        print("Cargando información de los archivos ....")
        
        catalog = initCatalog(option)
        loadData(catalog)
        
    elif int(inputs[0]) == 2:
        pass

    elif int(inputs[0]) == 3:

        sample = input("Digite el tamaño que desea de la muestra\n")
        sub_catalog = copy.deepcopy(catalog)
        sub_catalog["artworks"] = selectSample(catalog, sample)

        printSortOptions()
        option = input("Seleccione una opción para continuar\n")

        initial_year = input("Digite el año inicial:\n")
        end_year = input("Digite el año final:\n")

        time, sorted_artworks = sortArtworksByDate(catalog, option, initial_year, end_year)
        size = lt.size(sorted_artworks)

        print("{size} artworks were loaded.")
        print(f"The time taken to run the algorithm was {time}")

    else:
        sys.exit(0)
