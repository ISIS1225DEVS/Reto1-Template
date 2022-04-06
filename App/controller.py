﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) anyS later version.
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalogARRAY():
    """
    llamada la funcion de Inicialización del catalogo
    """
    catalog = model.newCatalogARRAY()
    return catalog

def initCatalogLINKED():
    catalog = model.newCatalogLINKED()
    return catalog


# Funciones para la carga de datos

def loadData(catalog):
    """
    carga los datos de los archivos en la estructura de datos
    """
    loadVideos(catalog)

def loadVideos(catalog):
    videosfile = cf.data_dir + 'Kaggle/videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addvideo(catalog, video) 

# Funciones de ordenamiento
def sortvideos(catalog, size):
    return model.sortvideos(catalog, size)

# Funciones de consulta sobre el catálogo
