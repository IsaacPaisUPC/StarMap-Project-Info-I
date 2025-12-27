"""
Tasca 9
Dissenyeu una funció de nom getCoordinates(starmap, constellation, star) que, donat un
mapa estel·lar, una constel·lació i una estrella, retorni les coordenades de l'estrella donada.

>>> starmap = {'Great Bear': {'stars': {'Alkaid': [10, 20], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
>>> getCoordinates(starmap, "Great Bear", "Alkaid")
[10, 20]
"""

def getCoordinates(starmap, constellation, star):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [10, 20], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
    >>> getCoordinates(starmap, "Great Bear", "Alkaid")
    [10, 20]
    """
    if constellation in starmap:
        llistaestrelles = starmap[constellation]['stars']
        if star in llistaestrelles:
            return llistaestrelles[star]
