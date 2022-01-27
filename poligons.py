import numpy as np
import numpy as np
from shapely import geometry
import random as rdm
 
#Se crean las dimensiones de los 10 poligonos (x,y)
polygons = np.random.randint(0,200,(10, rdm.randint(3,6) ,2))
#Contadores
i=0
cont_inter = 0
#Recorremos el arreglo con las dimensiones 
for puntos in polygons:
  #Convertimos a poligono mediante los puntos(x,y)
  figure = geometry.Polygon(puntos)
  #Aproximar los puntos por rectas tangentes
  a = geometry.polygon.LinearRing(puntos)
  #Caluclamos el are con el object.area
  cal_area = figure.area
  #Recorremos para saber con quienes interecta dicha figura
  for d in polygons:
    #Aproximamos de nuevo los puntos
    b = geometry.polygon.LinearRing(d)
    #con el metodo inicial.instersects(final) buscamos si se interesectan 
    inter = a.intersects(b)
    #Para no contar los mimos pares ordenados o poligono, creamos esta restriccion
    if a == b:
      pass
    #Si se intercectan, sera contado
    elif inter == True:
      cont_inter += 1
    else:
      continue
  print("Polygon: [",i,"]"," Area: ", cal_area, " Intersects: ",cont_inter)
  #Reiniicmaos contador de intersecciones y aumentamos el contador de poligonos
  i += 1
  cont_inter = 0