"""
Tasca1
Dissenyeu una funció de nom addConstellation(starmap,constellation) que ,donat un mapa
estel·lar i un nom de constel·lació, afegeixi una nova constel·lació buida al mapa.
>>>starmap={}
>>>addConstellation(starmap,"GreatBear")
>>>starmap
{'GreatBear':{'stars':{},'adjacencies':{}}}

"""
def addConstellation(starmap, constellation):
    """
    >>> starmap = {}
    >>> addConstellation(starmap, "Great Bear")
    >>> starmap
    {'Great Bear': {'stars': {}, 'adjacencies': {}}}
    """
  
    if constellation not in starmap:
        starmap[constellation] = {'stars': {},'adjacencies': {}}
