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
img_prueba1 = fn.cargar_imagen_rgb('data/img_prueba1.png')
img_buscar1 = fn.cargar_imagen_rgb('data/img_buscar1.png')
# img_buscar2 = fn.cargar_imagen_rgb('data/img_buscar2.png')
img_pegar1 = fn.cargar_imagen_rgb('data/img_pegar1.png')
img_pegar2 = fn.cargar_imagen_rgb('data/img_pegar2.png')

st.title("Proyecto Final - Procesamiento de Imágenes")



coords = fn.encontrar_posicion_imgbuscar(img=img_prueba1, img_buscar=img_buscar1)

if len(coords) > 0:
  img_final1 = fn.pegar_img(img=img_prueba1, coords=coords, img_pegar=img_pegar2, img_buscar=img_buscar1)

  fig, axs = plt.subplots(2, 2, figsize=(10, 10))
  axs[0, 0].imshow(img_prueba1)
  axs[0, 0].set_title('Imagen Original')
  axs[0, 0].axis('off')

  axs[0, 1].imshow(img_buscar1)
  axs[0, 1].set_title('Pedazo a Buscar')
  axs[0, 1].axis('off')

  axs[1, 0].imshow(img_pegar2)
  axs[1, 0].set_title('Imagen a Pegar')
  axs[1, 0].axis('off')

  axs[1, 1].imshow(img_final1)
  axs[1, 1].set_title('Imagen Final')
  axs[1, 1].axis('off')

  plt.show()

  st.subheader("Imagenes")

  st.image(img_prueba1, caption='Imagen Original', use_container_width=True)
  st.image(img_buscar1, caption='Pedazo a Buscar', use_container_width=True)
  st.image(img_pegar2, caption='Imagen a Pegar', use_container_width=True)
  st.image(img_final1, caption='Imagen Final', use_container_width=True)
else:
  print("No se encontró el pedazo de imagen a buscar.")
  st.info("No se encontró el pedazo de imagen a buscar.")
