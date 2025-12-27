"""
Tasca4
Dissenyeu una funció de nom deleteAdjacency(starmap,constellation,star1,star2), que
donat un mapa estel·lar, un nom de constel·lació, i dos noms d’estrella, elimini la connexió entre
les dues estrelles donades.
>>>starmap={'GreatBear':{'stars':{'Alkaid':[], 'Dubhe':[]},
...'adjacencies':{'Alkaid':['Dubhe'],'Dubhe':['Alkaid']}}}
>>>deleteAdjacency(starmap,"Great Bear","Alkaid","Dubhe")
>>>starmap["GreatBear"]["adjacencies"]["Alkaid"]
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
        stars = starmap[constellation]['stars']
  
        if star1 in stars and star2 in stars:  
            adjs = starmap[constellation]['adjacencies']
            if star2 in adjs[star1]:
                adjs[star1].remove(star2)
            if star1 in adjs[star2]:
                adjs[star2].remove(star1)
