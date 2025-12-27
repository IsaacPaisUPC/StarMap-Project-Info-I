"""
Tasca 5
Dissenyeu una funció de nom deleteStar(starmap, constellation, star) que, donat un mapa
estel·lar, una constel·lació i un nom d’estrella, elimini l’estrella de la constel·lació (així com totes
les seves adjacències).
>>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []},
... 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
>>> deleteStar(starmap, "Great Bear", "Dubhe")
>>> "Dubhe" in starmap["Great Bear"]["stars"]
False
>>> starmap
{'Great Bear': {'stars': {'Alkaid': []}, 'adjacencies': {'Alkaid': []}}}

"""
def deleteStar(starmap, constellation, star):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []},
    ... 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
    >>> deleteStar(starmap, "Great Bear", "Dubhe")
    >>> "Dubhe" in starmap["Great Bear"]["stars"]
    False
    >>> starmap
    {'Great Bear': {'stars': {'Alkaid': []}, 'adjacencies': {'Alkaid': []}}}
    """
    if constellation in starmap:
        stars = starmap[constellation]['stars']
        adjacencies = starmap[constellation]['adjacencies']
        if star in stars:
           
            for altra in adjacencies[star]:
                if star in adjacencies[altra]:
                    pos = adjacencies[altra].index(star)
                    del adjacencies[altra][pos]
            del adjacencies[star]   
            del stars[star]         
