"""
Tasca 8
Dissenyeu una funció de nom assignCoordinates(starmap, constellation, star, x, y) que,
donat un mapa estel·lar, una constel·lació, una estrella i les coordenades x i y, assigni les
coordenades [x,y] a l'estrella de la constel·lació donada.

>>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
>>> assignCoordinates(starmap, "Great Bear", "Alkaid", 10, 20)
>>> starmap["Great Bear"]["stars"]["Alkaid"]
[10, 20]
"""

def assignCoordinates(starmap, constellation, star, x, y):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
    >>> assignCoordinates(starmap, "Great Bear", "Alkaid", 10, 20)
    >>> starmap["Great Bear"]["stars"]["Alkaid"]
    [10, 20]
    """
    if constellation in starmap:
        llistaestrelles = starmap[constellation]['stars']
        if star in llistaestrelles:
            llistaestrelles[star] = [x, y]
