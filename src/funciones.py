import numpy as np
import matplotlib.image as mpimg

# pip install pillow
# Libreria para redimensionar imágenes
from PIL import Image

def cargar_imagen_rgb(path):
  """
  Carga una imagen y la convierte a formato RGB sin canal alfa
  :param path: Ruta de la imagen
  :return: Imagen en formato RGB como array de numpy tipo uint8
  """
  img = mpimg.imread(path)

  # Si tiene canal alfa, se elimina
  if img.shape[2] == 4:
    img = img[:, :, :3]

  # Si los valores están en float (0-1), se convierten a uint8 (0-255)
  if img.dtype != np.uint8:
    img = (img * 255).astype(np.uint8)

  return img

# Funcion para encontrar la posicion de un pedazo de imagen dentro de una imagen original
def encontrar_posicion_imgbuscar(img, img_buscar):
  """
  Encuentra la posición de un pedazo de imagen dentro de otra imagen
  :param img: Imagen original
  :param img_buscar: Pedazo de imagen a buscar dentro de la imagen original
  :return: Lista con las coordenadas (fila, columna) de inicio del pedazo encontrado en la imagen original
  """
  # Tamaño de imagen original y pedazo a buscar
  alto_img, ancho_img, canales_img = img.shape
  alto_img_buscar, ancho_img_buscar, canales_img_buscar = img_buscar.shape

  # Variable para almacenar las coordenadas de inicio del pedazo encontrado
  coords = []

  # Ciclo for para recorrer el alto de la imagen original
  for i in range(alto_img):
    # Ciclo for para recorrer el ancho de la imagen original
    for j in range(ancho_img):
      # Verifica si el pixel actual de la imagen original es igual al primer pixel del pedazo a buscar
      # En los tres canales de color (RGB)
      if (img[i,j,0] == img_buscar[0,0,0] and img[i,j,1] == img_buscar[0,0,1] and img[i,j,2] == img_buscar[0,0,2]):

        # Variable para almacenar la fila del tamaño del pedazo a buscar a partir de la coordenada actual
        fila_img = img[i,j:j+ancho_img_buscar]

        # Variable para almacenar la columna del tamaño del pedazo a buscar a partir de la coordenada actual
        columna_img = img[i:i+alto_img_buscar,j]

        # Variable para almacenar la primera fila del pedazo a buscar
        fila_img_buscar = img_buscar[0,:]

        # Variable para almacenar la primera columna del pedazo a buscar
        columna_img_buscar = img_buscar[:,0]

        # Verifica si la fila y columna del pedazo a buscar son iguales a la fila y columna de la imagen original
        # a partir de la coordenada actual
        if (np.array_equal(fila_img, fila_img_buscar) and np.array_equal(columna_img, columna_img_buscar)):
          # Variable para almacenar el pedazo de imagen a comparar para verificar si es el pedazo a buscar
          img_comparar = img[i:i+alto_img_buscar, j:j+ancho_img_buscar]
          # Verifica si el pedazo de imagen a comparar es igual al pedazo a buscar
          if es_pedazo(img_comparar, img_buscar):
            coords.append(i)
            coords.append(j)
  # Retorna las coordenadas encontradas, puede ser una lista vacía si no se encontró el pedazo
  return coords
          
# Funcion para comparar un pedazo de imagen con otro pedazo de imagen
def es_pedazo(img_comparar, img_buscar):
  """
  Compara dos pedazos de imagen para verificar si son iguales
  :param img_comparar: Pedazo de imagen a comparar
  :param img_buscar: Pedazo de imagen a buscar
  :return: True si los pedazos son iguales, False si no lo son
  """
  # Tamaño del pedazo a comparar
  alto_img_comparar, ancho_img_comparar, canales_img_comparar = img_comparar.shape

  # Ciclo for para recorrer el alto del pedazo a comparar
  for i in range(alto_img_comparar):
    # Ciclo for para recorrer el ancho del pedazo a comparar
    for j in range(ancho_img_comparar):
      # Verifica si el pixel del actual pedazo a comparar es diferente al pixel del pedazo a buscar
      if img_comparar[i,j,0] != img_buscar[i,j,0] or img_comparar[i,j,1] != img_buscar[i,j,1] or img_comparar[i,j,2] != img_buscar[i,j,2]:
        # Si hay alguna diferencia, retorna False
        return False
  # Si no hay diferencia, retorna True
  return True

# Funcion para pegar la imagen a pegar en la imagen original
def pegar_img(img, coords, img_pegar, img_buscar):
  """
  Pega un objeto (imagen) en una imagen original en la posición encontrada
  :param img: Imagen original donde se pegará el objeto
  :param coords: Coordenadas (fila, columna) donde se pegará la imagen a pegar
  :param img_pegar: Imagen que se pegará en la imagen original
  :param img_buscar: Pedazo de la imagen original donde se pegará la imagen a pegar
  :return: Imagen original con el objeto pegado
  """
  img_copy = img.copy()
  # Tamaño de la imagen original

  # Variable para almacenar la coordenada de inicio de la imagen a buscar
  i = coords[0]
  j = coords[1]

  # Tamaño de la imagen a pegar
  alto_img_pegar, ancho_img_pegar, canales_img_pegar = img_pegar.shape
  # Tamaño de la imagen a buscar
  alto_img_buscar, ancho_img_buscar, canales_img_buscar = img_buscar.shape
  
  # Verifica si la imagen a pegar es más grande que el pedazo a buscar
  if alto_img_pegar > alto_img_buscar or ancho_img_pegar > ancho_img_buscar or alto_img_pegar < alto_img_buscar or ancho_img_pegar < ancho_img_buscar:
    img_pegar = redimensionar_img(img_pegar, ancho_img_buscar, alto_img_buscar)
  
  # Actualizar tamaño de la imagen a pegar
  alto_img_pegar = alto_img_buscar
  ancho_img_pegar = ancho_img_buscar

  # Ciclo for para recorrer el alto de la imagen a pegar
  for x in range(alto_img_pegar):
    # Ciclo for para recorrer el ancho de la imagen a pegar
    for y in range(ancho_img_pegar):
      # Cambiar valores de la imagen original en las coordenadas correspondientes
      img_copy[i + x, j + y, :] = img_pegar[x, y, :]
  
  # Retorna la imagen original con el objeto pegado
  return img_copy

def redimensionar_img(img, ancho, alto):
  """
  Redimensionar una imagen a un tamaño específico
  :param img: Imagen a redimensionar
  :param ancho: Ancho deseado de la imagen
  :param alto: Alto deseado de la imagen
  :return: Imagen redimensionada
  """
  # Convertir el array de numpy a una imagen de PIL
  img_pil = Image.fromarray(img.astype('uint8'))

  # Redimensionar la imagen
  img_redimensionada = img_pil.resize((ancho, alto))

  # Convertir la imagen redimensionada de nuevo a un array de numpy
  img_redimensionada_np = np.array(img_redimensionada)

  return img_redimensionada_np