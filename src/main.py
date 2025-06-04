import numpy as np
import funciones as fn
import streamlit as st

import os
directorio_actual = os.getcwd()

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
imagen1fondo = fn.cargar_imagen_rgb('/data/fondos/brasil.png')
imagen1buscar = fn.cargar_imagen_rgb('data/buscar/buscar_brasil.png')
imagen1reemplazar = fn.cargar_imagen_rgb('data/reemplazar/cat.png')
coords1imagen = fn.encontrar_posicion_imgbuscar(img=imagen1fondo, img_buscar=imagen1buscar)

# Cargar imagenes ejemplo 2:
imagen2fondo = fn.cargar_imagen_rgb('data/fondos/bus.png')
imagen2buscar = fn.cargar_imagen_rgb('data/buscar/buscar_bus.png')
imagen2reemplazar = fn.cargar_imagen_rgb('data/reemplazar/mamberroi.png')
coords2imagen = fn.encontrar_posicion_imgbuscar(img=imagen2fondo, img_buscar=imagen2buscar)

# Cargar imagenes ejemplo 3:
imagen3fondo = fn.cargar_imagen_rgb('/data/fondos/f1.png')
imagen3buscar = fn.cargar_imagen_rgb('data/buscar/buscar_f1.png')
imagen3reemplazar = fn.cargar_imagen_rgb('data/reemplazar/simio.png')
coords3imagen = fn.encontrar_posicion_imgbuscar(img=imagen3fondo, img_buscar=imagen3buscar)

# Cargar imagenes de prueba
imagen4fondo = fn.cargar_imagen_rgb('data/fondos/brasil.png')
# Pedazo a buscar que no se encuentra en la imagen de fondo para probar el mensaje de error
imagen4buscar = fn.cargar_imagen_rgb('data/buscar/buscar_bus.png') 
imagen4reemplazar = fn.cargar_imagen_rgb('data/reemplazar/mamberroi.png')
coords4imagen = fn.encontrar_posicion_imgbuscar(img=imagen4fondo, img_buscar=imagen4buscar)

# Diccionario de imagenes y coordenadas
galerias = {
  "Galeria 1": {
    "fondo": imagen1fondo,
    "buscar": imagen1buscar,
    "reemplazar": imagen1reemplazar,
    "coords" : coords1imagen
  },
  "Galeria 2": {
    "fondo": imagen2fondo,
    "buscar": imagen2buscar,
    "reemplazar": imagen2reemplazar,
    "coords": coords2imagen
  },
  "Galeria 3": {
    "fondo": imagen3fondo,
    "buscar": imagen3buscar,
    "reemplazar": imagen3reemplazar,
    "coords": coords3imagen
  },
  "Galeria 4": {
    "fondo": imagen4fondo,
    "buscar": imagen4buscar,
    "reemplazar": imagen4reemplazar,
    "coords": coords4imagen
  }
}

st.set_page_config(page_title="Proyecto Final - Procesamiento de Imágenes", layout="centered")
st.title("Proyecto Final - Procesamiento de Imágenes / Galeria interactiva")

# Lista botones
botones = list(galerias.keys())

# Inicializar estado de los botones
for nombre in botones:
  key = f"Mostrar {nombre}"
  if key not in st.session_state:
    st.session_state[key] = False

# Espacio central con botones verticales
with st.container():
  for nombre in botones:
    key = f"Mostrar {nombre}"
    # Boton centrado
    boton_texto = f"Ocultar {nombre}" if st.session_state[key] else f"Mostrar {nombre}"
    if st.button(boton_texto, key=f"btn_{nombre}"):
      st.session_state[key] = not st.session_state[key]

    # Mostrar / ocultar imagenes
    if st.session_state[key]:
      gal = galerias[nombre]
      col1, col2 = st.columns(2)
      with col1:
        st.image(gal["fondo"], caption=f"Imagen de fondo - {nombre}", use_container_width=True)
        st.image(gal["reemplazar"], caption=f"Imagen a reemplazar - {nombre}", use_container_width=True)
      with col2:
        st.image(gal["buscar"], caption=f"Imagen a buscar - {nombre}", use_container_width=True)
        if len(gal["coords"]) > 0:
          st.image(fn.pegar_img(img=gal["fondo"], coords=gal["coords"], img_pegar=gal["reemplazar"], img_buscar=gal["buscar"]), caption=f"Imagen con reemplazo - {nombre}", use_container_width=True)
        else:
          st.error("No se encontró el pedazo de imagen a buscar en la imagen de fondo.")

