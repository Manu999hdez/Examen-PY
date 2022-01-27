#Importamos la libreria solicitada usar en este ejercicio
import argparse
#Importamos la libreria para funciones trigonometricas y matematicas
import math

#Funcion para el calculo de la distancia, parametros latitud y longitud
def distancia(lat1, lon1, lat2, lon2):
    #convirtiendo angulos a radianes
    fi1 = lat1 * ((math.pi)/180)
    fi2 =  lat2 * ((math.pi)/180)
    delta_lat = (lat2 - lat1) * ((math.pi)/180)
    delta_lon = (lon2 - lon1) * ((math.pi)/180)
    #Calculando la distancia
    haversine1 = ((math.sin(delta_lat/2))**(2)) + (math.cos(fi1) * math.cos(fi2) * ((math.sin(delta_lon/2))**(2)))
    haversine2 = math.sqrt(haversine1)
    haversine3 = 2 * math.asin(haversine2)
    #Utilice el valor de distancia de la tierra en KM
    dis = 6371 * haversine3
    return dis

#Con la libreria argparse necesitamos que al lado derecho al momento de invocar el archivo digitemos los valores para que estos sean 
#Almacenados en una lista y referenciados por el orden que le asignemos

#declaramos una variable parser para almacenar datos necesarios
parser = argparse.ArgumentParser(description= "Calculo de la distancia en un plano esferico")
#añadimos un nuevo argumento ("como se guardara", "tipo de dato con el que lo almacenaremos", "informacion para el usuario que se puede visualizar
#comando -h" 
parser.add_argument("lat1", type=float, help="para la primera latitud")
parser.add_argument("lon1", type=float, help="para la primera longitud")
parser.add_argument("lat2", type=float, help="para la segunda latitud")
parser.add_argument("lon2", type=float, help="para la segunda longitud")

#guardamos todo en una lista parse.args()
args = parser.parse_args()
#Referenciamos estos valores como parametros para la funcion
valores = distancia(args.lat1,args.lon1,args.lat2,args.lon2)
print ("La distancia es: ","{0:.3f}".format(valores))