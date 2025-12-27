"""
Tasca 3
Dissenyeu una funció de nom addAdjacencies(starmap, constellation, baseStar, neighbors)
que, donat un mapa estel·lar, una constel·lació, una estrella base i una llista d’estrelles adjacents,
estableixi les connexions bidireccionals. No s’han de permetre duplicats ni auto-adjacències. No es
crearà l’adjacència si alguna de les dues estrelles no existeix encara a la constel·lació.

Exemple:
>>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []},
... 'adjacencies': {'Alkaid': [], 'Dubhe': []}}}
>>> addAdjacencies(starmap, "Great Bear", "Alkaid", ["Dubhe"])
>>> starmap["Great Bear"]["adjacencies"]["Alkaid"]
['Dubhe']
"""
def addAdjacencies(starmap, constellation, baseStar, neighbors):
    """
    Donat un mapa estel·lar, una constel·lació, una estrella base i una llista
    d’estrelles adjacents, estableix les connexions bidireccionals.

    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': [], 'Dubhe': []}}}
    >>> addAdjacencies(starmap, "Great Bear", "Alkaid", ["Dubhe"])
    >>> starmap["Great Bear"]["adjacencies"]["Alkaid"]
    ['Dubhe']
    """
    if constellation in starmap and baseStar in starmap[constellation]['stars']:
        for estrella in neighbors:
            if estrella == baseStar:
                pass 
            elif estrella not in starmap[constellation]['stars']:
                pass
            else:
                adjs = starmap[constellation]['adjacencies']
                if estrella not in adjs[baseStar]:
                    adjs[baseStar].append(estrella)
                if baseStar not in adjs[estrella]:
                    adjs[estrella].append(baseStar)
