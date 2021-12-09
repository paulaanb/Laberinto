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
place_x = 0
place_y = 0
#Definimos el tunel
class Tunel:
    def __init__(self, x1, y1, x2, y2):
        self.extremo1 = Coordenadas(x1, y1)
        self.extremo2 = Coordenadas(x2, y2)
        
#El laberinto resuelto es el siguiente:
lab_solution =[
    " ", "X", "X", "X", "X", "X",
    " ", "X", " ", " ", " ", " ",
    " ", "X", " ", "X", "X", "S",
    " ", "X", " ", " ", "X", "X",
    " ", " ", "X", " ", "X", "X",
    "X", " ", " ", " ", "X", "X",
]
#Como salir de el
howtogetout = ["ABAJO", "ABAJO", "ABAJO", "ABAJO","DERECHA", "ABAJO", "DERECHA", "DERECHA", "ARRIBA", "ARRIBA", "IZQUIERDA", "ARRIBA", "ARRIBA", "DERECHA", "DERECHA", "DERECHA", "ABAJO"]

#Definimos la función para poder movernos 
def movement():
    print("1-> DERECHA")
    print("2-> IZQUIERDA")
    print("3-> ARRIBA")
    print("4-> ABAJO")
    global place_x
    global place_y
    movement = int(input("Escoja un movimiento entre los disponibles."))
    if movement == 1:
        place_x += 1
        return place_x
    if movement == 2:
        place_x -= 1
        if place_x > 0 and place_x < 6:
            return place_x
        else: 
            print("Ese movimiento ha generado la salida del laberinto.")
    if movement == 3:
        place_y -= 1 
        if place_y > 0 and place_y < 6:
            return place_y
        else:
           print("Ese movimiento ha generado la salida del laberinto.") 
    if movement == 4:
        place_y += 1
        return place_y

#Establecemos una función para empezar a movernos en el laberinto y insertamos el laberinto en blanco
def play():
    global place_x
    global place_y
    lab_initial= [
    "0", "¿?", "¿?", "¿?", "¿?", "¿?",
    "¿?", "¿?", "¿?", "¿?", "¿?", "¿?",
    "¿?", "¿?", "¿?", "¿?", "¿?", "¿?",
    "¿?", "¿?", "¿?", "¿?", "¿?", "¿?",
    "?¿", "¿?", "¿?", "¿?", "¿?", "¿?"
    ]
    print (lab_initial)
    print("Iniciamos el labeerinto en la posición 0, donde las demás posiciones pueden ser la posición que nos lleva a la salida o un obstáculo que nos impide avanzar.")
    