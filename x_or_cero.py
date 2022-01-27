import numpy as np
ganador = None

def quien_gana(game):
  global winner 
  diagonales = diagonal()
  filas = fila()
  columnas = columna()
  if filas:
    ganador = filas
  elif columnas :
    ganador = columnas
  elif diagonal :
    ganador = diagonales
  else:
    ganador = None
  return ganador


def diagonal() :
  if game[1][1] == " ":
    return None
  elif game[0][0] == game[1][1] and game[2][2] == game[1][1]:
    return game[1][1]
  elif game[2][0] ==  game[1][1] and game[1][2] == game[1][1]:
    return game [1][1]

def fila():
  if game[0][0] == game[0][1] and game[0][0] == game[0][2] and game[0][0] != " ":
    return game[0][0]
  elif game[1][0] == game[1][1] and game[1][0] == game[1][2] and game[1][0] != " ":
    return game[1][0]
  elif game[2][0] == game[2][1] and game[2][0] == game[2][2] and game[2][0] != " ":
    return game[2][0]
  else:
    return None
def columna():
  if game[0][0] == game[1][0] and game[0][0] == game[2][0] and game[0][0] != " ":
    return game[0][0]
  elif game[0][1] == game[1][1] and game[0][1] == game[2][1] and game[0][1] != " ":
    return game[0][1]
  elif game[0][2] == game[1][2] and game[0][2] == game[2][2] and game[0][2] != " ":
    return game[0][2]
  else:
    return None

## Al momento de cargar un numpy array y se quieran utilizar espacios vacios 
## se utilizara comilla con espacio " " en lugar de None o "" <- sin espacio  
game = np.array([[" ", " ", "X"],
                 [" ", " ", " "],
                 ["X", "X", "X"]])
x_or_o = quien_gana(game)
print("El ganador es: ",x_or_o)