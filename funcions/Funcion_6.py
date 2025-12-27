"""
Tasca 6
Dissenyeu una funció de nom listAllStars(starmap, constellation), que donat un mapa estel·lar i una constel·lació, 
mostri per pantalla totes les estrelles de la constel·lació i les seves adjacències.
Exemple:
>>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []},
... 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
>>> listAllStars(starmap, "Great Bear")
Great Bear:
Alkaid adjacent a: Dubhe
Dubhe adjacent a: Alkaid
"""

def listAllStars(starmap, constellation):
    """
    >>> listAllStars({'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}, 'Great Bear')
    Alkaid adjacent a: Dubhe
    Dubhe adjacent a: Alkaid
    """
    for estrella in starmap[constellation]['adjacencies']:
        print( estrella + " adjacent a: "+ ",".join(starmap[constellation]['adjacencies'][estrella]))
