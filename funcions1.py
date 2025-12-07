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
