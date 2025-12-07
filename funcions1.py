starmap= {}
constellation= input("Diguem una constel·lació: ")

def addConstellation(starmap, constellation):
    """
    >>> addConstellation(starmap, "Great Bear")
    {'Great Bear': {'stars': {}, 'adjacencies': {}}}
    
    """
    if starmap.get(constellation):
        print("La constelacio ja existeix")
    else:
       starmap[constellation]= {'star':{},'adejecencies':{}}
       return starmap
            
print(starmap)
