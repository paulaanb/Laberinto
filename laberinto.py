#Importamos las librerias
import math
import os
import random
import re
import sys

#Establecemos las coordenadas de nuestro laberinto
class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def comparate(self,x,y):
        if(self.x==x and self.y==y):
            return True
        else:
            return False
#Definimos el tunel
class Tunel:
    def __init__(self, x1, y1, x2, y2):
        self.extremo1 = Coordenadas(x1, y1)
        self.extremo2 = Coordenadas(x2, y2)
        
#El laberinto resuelto es el siguiente:
lab_solution =[
    " ", "X", "X", "X", "X",
    " ", "X", " ", " ", " ",
    " ", "X", " ", "X", "S",
    " ", "X", " ", " ", "X",
    " ", " ", "X", " ", "X",
    "X", " ", " ", " ", "X",
]
#Como salir de el
howtogetout = ["ABAJO", "ABAJO", "ABAJO", "ABAJO","DERECHA", "ABAJO", "DERECHA", "DERECHA", "ARRIBA", "ARRIBA", "IZQUIERDA", "ARRIBA", "ARRIBA", "DERECHA", "DERECHA", "ABAJO"]

