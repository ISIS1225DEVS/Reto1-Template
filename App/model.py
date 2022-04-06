﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is freesdfasdfsf software: you can redistribute it and/or modify
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalogARRAY():
    """
    inicializa el catalogo de video y su informacion
    """
    catalog = {'videos': None,
               'categorias': None,
               'paises':None,
               'tag':None}
    
    catalog['videos'] = lt.newList('ARRAY_LSIT', cmpfunction = funcompare) 
    catalog['categorias'] = lt.newList('ARRAY_LIST', 
                                       cmpfunction = comparecategory)
    catalog['paises'] = lt.newList('ARRAY_LIST', 
                                   cmpfunction = comparecountry)
    catalog['tag'] =lt.newList()

    return catalog

def newCatalogLINKED():
    """
    inicializa el catalogo de video y su informacion
    """
    catalog = {'videos': None,
               'categorias': None,
               'paises':None,
               'tag':None}
    
    catalog['videos'] = lt.newList()
    catalog['categorias'] = lt.newList('SINGLE_LINKED', 
                                       cmpfunction = comparecategory)
    catalog['paises'] = lt.newList('SINGLE_LINKED', 
                                   cmpfunction = comparecountry)
    catalog['tag'] =lt.newList()

    return catalog


# Funciones para agregar informacion al catalogo

def addvideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    categorias = video['category_id'] 
    categorias =str(categorias)
    paises = video['country']
    newcountry(catalog, paises.strip(), video)
    newcategory(catalog, categorias.strip(), video)


def newcategory(catalog, categorynumber, video):
    categorias= catalog['categorias']
    poscategoria = lt.isPresent(categorias, categorynumber)
    if poscategoria >0:
        category = lt.getElement(categorias, poscategoria)
    else:
        category = addnewcategory(categorynumber)
        lt.addLast(categorias, category)
    lt.addLast(category['videos'], video)
    
    
def newcountry(catalog, countryname, video):
    paises = catalog['paises']
    pospaises = lt.isPresent(paises, countryname)
    if pospaises > 0:
        country = lt.getElement(paises, pospaises)
    else:
        country = addnewcountry(countryname)
        lt.addLast(paises, country)
    lt.addLast(country['videos'], video)
      


# Funciones para creacion de datos

def addnewcategory(categorynumber):
    category = {'number_category': "", "videos": None}
    category['number_category'] = categorynumber
    category['videos'] = lt.newList('ARRAY_LIST')
    return category


def addnewcountry(countryname):
    country = {'name_country': "", "videos": None}
    country['name_country'] = countryname
    country['videos'] = lt.newList('ARRAY_LIST')
    return country


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def comparecategory(categorynumber1, category):
    if (categorynumber1.lower() == category['number_category'].lower()):
        return 0
    return -1


def comparecountry(countryname1, country):
    if (countryname1.lower() == country['name_country'].lower()):
        return 0
    return -1

def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    if video1['views'] < video2['views']:
        return True
    else:
        return False
    
def funcompare(video1,video2):
    if video1['video_id'] > video2['video_id']:
        return 1
    if video1['video_id'] < video2['video_id']:
        return -1
    else:
        return 0


# Funciones de ordenamiento
def sortvideos(catalog, size):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = sa.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
     