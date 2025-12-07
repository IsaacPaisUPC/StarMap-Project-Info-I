"""
Tasca1
Dissenyeu unaf unció de nom addConstellation(starmap,constellation)que,donat un mapa
estel·lar i un nom de constel·lació, afegeixi una nova constel·lació buida al mapa.
>>>starmap={}
>>>addConstellation(starmap,"GreatBear")
>>>starmap
{'GreatBear':{'stars':{},'adjacencies':{}}}

"""
starmap = {}
constellation = input("Diguem una constel·lació: ")

def addConstellation(starmap, constellation):
    """
    >>> addConstellation(starmap, "GreatBear")
    {'GreatBear': {'stars': {}, 'adjacencies': {}}}
    """
    if starmap.get(constellation):
        print("La constelacio ja existeix")
    else:
        starmap[constellation] = {'stars': {}, 'adjacencies': {}}
        return starmap

print(starmap)
