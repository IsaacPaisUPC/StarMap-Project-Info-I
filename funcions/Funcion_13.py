"""
Tasca 13
Dissenyeu una funció de nom makePen() que creï i retorni una tortuga a punt per dibuixar. La
configuració de la tortuga ha de ser: amagada, màxima velocitat, llapis aixecat i gruix de línia 2.
"""

import turtle

def makePen():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.pensize(2)
    return pen
