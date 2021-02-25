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
    print("\nBienvenido: ")
    print('1- Seleccion de el tipo de lista para cargar los datos.')
    print("2- Cargar información en el catalogo.")
    print("3- Consultar buenos videos por categoria y pais.")
    print('4- Consultar video tendencia por pais.')
    print('5- Consultar video tendencia por categoria.')
    print('6- Consultar videos con mas likes.')
    print("0- Salir\n")

def printListOptions():
    print('Ingrese el numero correspondiente al tipo de lista que desee: ')
    print(' 1. ARRAY_LIST.')
    print(' 2. LINKED LIST.')

def initCatalog(listType):
    'The catalog is initialized'
    return controller.initCatalog(listType)

def loadData(catalog):
    'Load the videos into the data structure'
    controller.loadData(catalog)

catalog = None

listType = None

'Menu principal'

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')

    if int(inputs[0]) == 1:
        listSelection = False
        while listSelection == False:
            printListOptions()
            listTypeSelection = input('Opción seleccionada: ')
            if int(listTypeSelection[0]) == 1:
                listType = 'ARRAY_LIST'
                print('\nSeleciono ARRAY_LIST')
                input('Seleccion exitosa! Oprima ENTER para continuar...')
                listSelection = True
            elif int(listTypeSelection[0]) == 2:
                listType = 'SINGLE_LINKED'
                print('\nSeleciono lINKED_LIST')
                input('Seleccion exitosa! Oprima ENTER para continuar...')
                listSelection = True
            else:
                input('\nSeleccion Erronea! Oprima ENTER para continuar...')

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos...\n")
        catalog = initCatalog(listType)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargados: ' + str(lt.size(catalog['categories'])))
        #print(type(catalog['videos']['elements']),'\n')

    elif int(inputs[0]) == 3:
        pass

    else:
        sys.exit(0)
sys.exit(0)
