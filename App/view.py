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

import config as cf
import sys
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
    print("3- Clasificar las obras de un artista por técnica")
    print("4- Clasificar las obras por la nacionalidad de sus creadores")
    print("5- Transportar obras de un departamento")
    print("6- Proponer una nueva exposición en el museo")

def printListOptions():
    print("Seleccione la implementación de las listas del catálogo")
    print("1- ARRAY_LIST")
    print("2- SINGLE_LINKED")

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
        pass
    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass

    else:
        sys.exit(0)