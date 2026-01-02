def listIsolatedStars(starmap, constellation):
    """
    >>> starmap = {'Great Bear': {'stars': {'A':[], 'B':[], 'C':[]},'adjacencies': {'A':['B'], 'B':['A']}}}
    >>> listIsolatedStars(starmap, "Great Bear")
    ['C']
    """
    llista = []
    if constellation not in starmap:
        print("La constel·lació no existeix")
        return []


    adjs = starmap[constellation]['adjacencies']

    for estrella in starmap[constellation]['stars']:
      
        if estrella not in adjs or len(adjs[estrella]) == 0:
            llista.append(estrella)
            
    return llista
