import numpy as np
import funciones as fn
import streamlit as st
# streamlit run src/main.py

# Array de prueba para funcionamiento del programa
img_prueba = np.array([
  [[25,36,48],[2,25,36],[13,45,79],[14,12,14],[12,58,65]],
  [[6,87,45],[7,7,7],[8,8,8],[9,9,9],[10,10,10]],
  [[11,11,11],[12,12,12],[13,13,13],[14,14,14],[15,15,15]],
  [[16,16,16],[17,17,17],[18,18,18],[19,19,19],[20,20,20]],
  [[21,21,21],[22,22,22],[23,23,23],[24,24,24],[25,25,25]]
  ])

# Pedazo de imagen original a buscar para pegar otra imagen
img_buscar = np.array([
  [[7,7,7],[8,8,8]],
  [[12,12,12],[13,13,13]]
  ])

# Array de prueba que no pertenece a imagen_prueba para detectar errores
img_inexistente = np.array([
  [[99,99,99],[100,100,100]],
  [[101,101,101],[102,102,102]]
  ])

# Array de prueba que se pegará en la imagen original
img_pegar = np.array([
  [[99,99,99],[100,100,100]],
  [[101,101,101],[102,102,102]]
  ])

# Array de prueba por si se quiere pegar un objeto más chico al pedazo a buscar
img_pegar_chico = np.array([
  [[99,99,99], [100,100,100]]
  ])

# Array de prueba por si se quiere pegar un objeto más grande al pedazo a buscar
img_pegar_grande = np.array([
  [[99,99,99], [100,100,100], [101,101,101]],
  [[102,102,102], [103,103,103], [104,104,104]],
  [[105,105,105], [106,106,106], [107,107,107]]
  ])

# Prueba de funciones
coords = fn.encontrar_posicion_imgbuscar(img=img_prueba, img_buscar=img_buscar)

if len(coords) > 0:
  img_final = fn.pegar_img(img=img_prueba, coords=coords, img_pegar=img_pegar_chico, img_buscar=img_buscar)
  print("Imagen original con el objeto pegado:")
  print(img_final)
else:
  print("No se encontró el pedazo de imagen a buscar.")
