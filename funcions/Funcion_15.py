"""
Tasca 15
Dissenyeu una funció de nom drawAllStars(pen, stars) que, donada una tortuga i un diccionari
d’estrelles (amb coordenades), dibuixi totes les estrelles amb coordenades vàlides [x, y].
"""

def drawAllStars(pen, stars):
    for estrella in stars:
        coord = stars[estrella]
        if isValidCoord(coord):
            drawStar(pen, estrella, coord)
