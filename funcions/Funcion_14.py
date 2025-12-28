"""
Tasca 14
Dissenyeu una funció de nom drawStar(pen, name, coord, pointSize=8, offset=8) que,
donada una tortuga, un nom d’estrella, unes coordenades, la mida de punt i un desplaçament, dibuixi
un punt a coord i escrigui name desplaçat lleugerament per no tapar el punt.
"""

def drawStar(pen, name, coord, pointSize=8, offset=8):
    coord= x,y
    pen.goto(x,y)
    pen.dot(pointSize)
    pen.goto(x+offset, y+offset)
    pen.write(name)
