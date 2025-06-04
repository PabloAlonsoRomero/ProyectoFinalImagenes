import numpy as np
import funciones as fn
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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

# Prueba funciones con imagenes reales:
# Cargar imagenes ejemplo 1:
imagen1fondo = fn.cargar_imagen_rgb('data/fondos/brasil.png')
imagen1buscar = fn.cargar_imagen_rgb('data/buscar/buscar_brasil.png')
imagen1reemplazar = fn.cargar_imagen_rgb('data/reemplazar/cat.png')
coords1imagen = fn.encontrar_posicion_imgbuscar(img=imagen1fondo, img_buscar=imagen1buscar)

# Cargar imagenes ejemplo 2:
imagen2fondo = fn.cargar_imagen_rgb('data/fondos/bus.png')
imagen2buscar = fn.cargar_imagen_rgb('data/buscar/buscar_bus.png')
imagen2reemplazar = fn.cargar_imagen_rgb('data/reemplazar/mamberroi.png')
coords2imagen = fn.encontrar_posicion_imgbuscar(img=imagen2fondo, img_buscar=imagen2buscar)

# Cargar imagenes ejemplo 3:
imagen3fondo = fn.cargar_imagen_rgb('data/fondos/F1.png')
imagen3buscar = fn.cargar_imagen_rgb('data/buscar/buscar_F1.png')
imagen3reemplazar = fn.cargar_imagen_rgb('data/reemplazar/simio.png')
coords3imagen = fn.encontrar_posicion_imgbuscar(img=imagen3fondo, img_buscar=imagen3buscar)

# Cargar imagenes de prueba
imagen4fondo = fn.cargar_imagen_rgb('data/fondos/brasil.png')
# Pedazo a buscar que no se encuentra en la imagen de fondo para probar el mensaje de error
imagen4buscar = fn.cargar_imagen_rgb('data/fondos/buscar_bus.png') 
imagen4reemplazar = fn.cargar_imagen_rgb('data/reemplazar/mamberroi.png')
coords4imagen = fn.encontrar_posicion_imgbuscar(img=imagen4fondo, img_buscar=imagen4buscar)

st.title("Proyecto Final - Procesamiento de Imágenes")
