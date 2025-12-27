"""
Tasca 4
Dissenyeu una funció de nom deleteAdjacency(starmap, constellation, star1, star2), que
donat un mapa estel·lar, un nom de constel·lació, i dos noms d’estrella, elimini la connexió entre
les dues estrelles donades
Exemple:
>>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []},
... 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
>>> deleteAdjacency(starmap, "Great Bear", "Alkaid", "Dubhe")
>>> starmap["Great Bear"]["adjacencies"]["Alkaid"]
[]
"""

  def deleteAdjacency(starmap, constellation, star1, star2):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
    >>> deleteAdjacency(starmap, "Great Bear", "Alkaid", "Dubhe")
    >>> starmap["Great Bear"]["adjacencies"]["Alkaid"]
    []
    """
    if constellation in starmap:
        if star1 in starmap[constellation]['adjacencies'][star2] and star2 in starmap[constellation]['adjacencies'][star1]:
            starmap[constellation]['adjacencies'][star1].remove(star2)
            starmap[constellation]['adjacencies'][star2].remove(star1)
