"""
Tasca 16
Dissenyeu una funció de nom drawSegment(pen, aXY, bXY) que, donada una tortuga i dues
coordenades, dibuixi una línia des de aXY=(aX, aY) fins a bXY=(bX, bY).
"""

def drawSegment(pen, aXY, bXY):
    
    aX, aY = aXY
    bX, bY = bXY

    pen.penup()
    pen.goto(aX, aY)

    pen.pendown()
    pen.goto(bX, bY)
