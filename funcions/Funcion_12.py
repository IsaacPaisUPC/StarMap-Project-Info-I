"""
Tasca 12
Dissenyeu una funció de nom setupWindow(constellation, width=800, height=600) que creï
la finestra de turtle, en fixi el títol i la mida, i retorni l’objecte Screen.
Nota: aquestes funcions visuals no tenen doctest.
"""
import turtle

def setupWindow(constellation, width=800, height=600):
    screen = turtle.Screen()
    screen.title(constellation)
    return screen
