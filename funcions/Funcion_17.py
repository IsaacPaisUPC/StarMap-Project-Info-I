"""
Tasca 17
Dissenyeu una funció de nom drawAllSegments(pen, stars, adjacencies) que, donada una
tortuga, un diccionari d’estrelles, i un diccionari d’adjacències, recorri totes les adjacències i dibuixi
segments només quan should_draw_once(a,b) sigui True. Ignoreu noms sense coordenades vàlides.
"""

def drawAllSegments(pen, stars, adjacencies):
    for estrella_1, conectades in adjacencies.items():

        if estrella_1 not in stars or not isValidCoord(stars[estrella_1]):
            continue

        for estrella_2 in conectades:

            if estrella_2 not in stars or not isValidCoord(stars[estrella_2]):
                continue

            if shouldDrawOnce(estrella_1, estrella_2):
                drawSegment( pen,stars[estrella_1],stars[estrella_2])

