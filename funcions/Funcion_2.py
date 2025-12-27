"""
Tasca2
Dissenyeu una funció de nom addStars(starmap,constellation,starNames) que, donat un
mapa estel·lar, una constel·lació i una llista d’estrelles, permeti afegir les estrelles donades a una
constel·lació existent. Cada estrella ha de començar sense adjacències i amb coordenades buides.

Exemple:
>>> starmap = {'GreatBear': {'stars': {}, 'adjacencies': {}}}
>>> addStars(starmap, "GreatBear", ["Alkaid", "Dubhe"])
>>> starmap
{'GreatBear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': [], 'Dubhe': []}}}
"""
def addStars(starmap, constellation, starNames):
    """
    >>> starmap = {'Great Bear': {'stars': {}, 'adjacencies': {}}}
    >>> addStars(starmap, "Great Bear", ["Alkaid", "Dubhe"])
    >>> starmap['Great Bear']['stars']
    {'Alkaid': [], 'Dubhe': []}
    >>> starmap['Great Bear']['adjacencies']
    {'Alkaid': [], 'Dubhe': []}
    """
    if constellation in starmap:
        for star in starNames:
            if star not in starmap[constellation]['stars']:
                starmap[constellation]['stars'][star] = []
                starmap[constellation]['adjacencies'][star] = []
