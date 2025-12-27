"""
Tasca 7
Dissenyeu una funció de nom listAllConstellations(starmap) que, donat un mapa estel·lar,
mostri per pantalla el nom de totes les constel lacions guardades al mapa.

Exemple:
>>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
>>> listAllConstellations (starmap)
Great Bear
>>> starmap = {}
>>> listAllConstellations (starmap)
No hi ha constel·lacions
"""
def listAllConstellations(starmap):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
    >>> listAllConstellations(starmap)
    Great Bear
    >>> starmap = {}
    >>> listAllConstellations(starmap)
    No hi ha constel·lacions
    """
    if len(starmap) == 0:
        print("No hi ha constel·lacions")
    else:
        for constelacio in starmap:
            print(constelacio)
