import numpy as np

def encontrarPosicionImagen(imgOriginal, objetoABuscar):
  altoOriginal, anchoOriginal = imgOriginal.shape
  altoObjetoBuscar, anchoObjetoBuscar = objetoABuscar.shape
  # Coordenada de inicio de la imagen a buscar en imagen original
  coordenadaInicioImagenOriginal = []

  for i in range(altoOriginal):
    for j in range(anchoOriginal):
      if (imgOriginal[i,j] == objetoABuscar[0,0]):
        filaAPixelesImgOriginal = imgOriginal[i,j:j+anchoObjetoBuscar]
        columnaAPixelesImgOriginal = imgOriginal[i:i+altoObjetoBuscar,j]
        filaAPixelesObjetoBuscar = objetoABuscar[0,:]
        columnaAPixelesObjetoBuscar = objetoABuscar[:,0]
        if (np.array_equal(filaAPixelesImgOriginal, filaAPixelesObjetoBuscar) and 
            np.array_equal(columnaAPixelesImgOriginal, columnaAPixelesObjetoBuscar)):
          pedazoAComparar = imgOriginal[i:i+altoObjetoBuscar, j:j+anchoObjetoBuscar]
          if esPedazoEncontrado(pedazoAComparar, objetoABuscar):
            coordenadaInicioImagenOriginal.append((i, j))
  return coordenadaInicioImagenOriginal
          
def esPedazoEncontrado(pedazoAComparar, objetoABuscar):
  altoPedazoAComparar, anchoPedazoAComparar = pedazoAComparar.shape
  for i in range(altoPedazoAComparar):
    for j in range(anchoPedazoAComparar):
      if pedazoAComparar[i,j] != objetoABuscar[i,j]:
        return False
  return True