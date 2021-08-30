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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos
def loadData(catalog):
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtists(catalog):
    artist_file: cf.data_dir + 'MoMA/Artists-utf8-5pct.csv'
    input_file = csv.reader(open(artist_file, encoding= 'utf-8'))
    for art in input_file:
        model.addArtist(catalog, art)

def loadArtworks(catalog):
    artist_file: cf.data_dir + 'MoMA/Artworks-utf8-5pct.csv'
    input_file = csv.reader(open(artist_file, encoding= 'utf-8'))
    for artw in input_file:
        model.addArtist(catalog, artw)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
