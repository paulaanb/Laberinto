# Laberinto
Mi dirección de Github para este repositorio es el siguiente [Github (https://github.com/paulaanb/Laberinto)]
En este proyecto hemos creado un juego de un laberinto en el cual hay una entrada y una salida, con obstáculos entre ellos. 
Para soluciar el juego debes indicar en que direccion deseas moverte, y el programa te indica si em esa posicion hay una obstaculo, o por el contrario es el camino correcto para llegar a la salida.
El diagrama de flujo se muestra a continuación:
<img width="765" alt="Captura de pantalla 2021-12-09 a las 12 45 57" src="https://user-images.githubusercontent.com/91721496/145391507-e49756a2-a288-4f69-86d9-e7219813d0f9.png">


El código es :
```#Importamos las librerias
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
    "¿?", "¿?", "¿?", "¿?", "¿?", "¿?"
    ]
    print(lab_initial)
    print("Iniciamos el laberinto en la posición 0, donde las demás posiciones pueden ser la posición que nos lleva a la salida o un obstáculo que nos impide avanzar.")

while True:    
    #Empezamos con el bucle para los movimientos
    total_place = (place_x*6) + place_y

    #Si la posición elegida es la correcta pasara de ¿? a "", mientras que si es erronea cambiará a X
    lab_initial(total_place) = " "
    movement()
    total_place = (place_x*6) + place_y
    if lab_solution(total_place) == "X":
        print("Ese movimiento ha derivado en un obstáculo, por lo que vuelve a la posición inicial.")
        place_y = 0
        place_x = 0
        print(lab_initial) 
    elif lab_solution(total_place) == " ":
        print("La posición escogida fue correcta, puede continuar el laberinto.")
        lab_initial(total_place)= 0
        print(lab_initial)
    elif lab_solution(total_place) == "S":
        print("¡Enhorabuena! Ha encontrado la salida del laberinto!")
        print("Los pasos para salir fueron los siguientes:")
        print (howtogetout)
        break
        #Finalizamos el bucle
    else: 
        place_x = 0
        place_y = 0
        print("La posición escogida no es posible, por lo que vuelve a la posición inicial.")
        print(lab_initial)

#Establecemos la función para empezar el juego 
play()
