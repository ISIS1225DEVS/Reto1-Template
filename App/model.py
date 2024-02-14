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
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {'jobs': None,
                    'skills': None,
                    'employment_types': None,
                    'multilocations': None}
    
    data_structs['jobs'] = lt.newList('SINGLE_LINKED')
    data_structs['skills'] = lt.newList('SINGLE_LINKED')
    data_structs['employment_types'] = lt.newList('SINGLE_LINKED')
    data_structs['multilocations'] = lt.newList('SINGLE_LINKED')

    return data_structs

# Funciones para agregar informacion al modelo

def add_job(data_structs, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    j = new_job(job['title'], job['street'], job['city'], job['country_code'], job['address_text'], job['marker_icon'],
                job['workplace_type'], job['company_name'], job['company_url'], job['company_size'], job['experience_level'],
                job['published_at'], job['remote_interview'], job['open_to_hire_ukrainians'], job['id'], job['display_offer'])
    lt.addLast(data_structs['jobs'], j)
    return data_structs

def add_skill(data_structs, skill):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    s = new_skill(skill['field'], skill['level'], skill['job_title'])
    lt.addLast(data_structs['skills'], s)
    return data_structs

def add_employment_type(data_structs, employment_type):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    et = new_employment_type(employment_type['type'], employment_type['job_title'], employment_type['currency'],
                            employment_type['min_salary'], employment_type['max_salary'])
    lt.addLast(data_structs['employments_types'], et)
    return data_structs

def add_multilocation(data_structs, multilocation):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    m = new_employment_type(multilocation['location'], multilocation['city'], multilocation['job_title'])
    lt.addLast(data_structs['multilocations'], m)
    return data_structs

# Funciones para creacion de datos

def new_job(title,street,city,country_code,address_text,marker_icon,workplace_type,company_name,company_url,company_size,
            experience_level,published_at,remote_interview,open_to_hire_ukrainians,id,display_offer):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    job = {'title': '',
           'street': '',
           'city': '',
           'country_code': '',
           'address_text': '',
           'marker_icon': '',
           'workplace_type': '',
           'company_name': '',
           'company_url': '',
           'company_size': '',
           'experience_level': '',
           'published_at': '',
           'remote_interview': '',
           'open_to_hire_ukrainians': '',
           'id': '',
           'display_offer': ''}
    
    job['title'] = title
    job['street'] = street
    job['city'] = city
    job['country_code'] = country_code
    job['address_text'] = address_text
    job['marker_icon'] = marker_icon
    job['workplace_type'] = workplace_type
    job['company_name'] = company_name
    job['company_url'] = company_url
    job['company_size'] = company_size
    job['experience_level'] = experience_level
    job['published_at'] = published_at
    job['remote_interview'] = remote_interview
    job['open_to_hire_ukrainians'] = open_to_hire_ukrainians
    job['id'] = id
    job['display_offer'] = display_offer
    return job

def new_skill(field, level, title):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    skill = {'field': '',
             'level': '',
             'title': ''}
    
    skill['field'] = field
    skill['level'] = level
    skill['title'] = title
    return skill

def new_employment_type(type, title, currency, min_salary, max_salary):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    employment_type = {'type': '',
                       'title': '',
                       'currency': '',
                       'min_salary': '',
                       'max_salary': ''}
    
    employment_type['type'] = type
    employment_type['title'] = title
    employment_type['currency'] = currency
    employment_type['min_salary'] = min_salary
    employment_type['max_salary'] = max_salary  
    return employment_type

def new_multilocation(location, city, title):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    multilocation = {'location': '',
                     'city': '',
                     'title': ''}
    
    multilocation['location'] = location
    multilocation['city'] = city
    multilocation['title'] = title
    return multilocation

# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass

def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
