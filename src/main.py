import numpy as np
import funciones as fn

# Prueba imagen original
imgOriginal = np.array([[1,2,3,4,5],
                           [6,7,8,9,10],
                           [11,12,13,14,15],
                           [16,17,18,19,20],
                           [21,22,23,24,25]])

# Objeto a buscar
objetoABuscar = np.array([[7,8],
                          [12,13]])

# Objeto a buscar que no existe
objetoABuscarInexistente = np.array([[99,100],
                                      [101,102]])

# Objeto a pegar
objetoAPegar = np.array([[99,100],
                          [101,102]])

# Prueba de funciones
coordenadaInicioImagenOriginal = fn.encontrarPosicionImagen(imgOriginal=imgOriginal, objetoABuscar=objetoABuscar)
print("Coordenadas de inicio de la imagen original:", coordenadaInicioImagenOriginal)

if (len(coordenadaInicioImagenOriginal) == 0):
  print("No se encontró el objeto a buscar en la imagen original.")
