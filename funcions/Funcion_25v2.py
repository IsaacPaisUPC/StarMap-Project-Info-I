def listIsolatedStars(starmap, constellation):
    """
    >>> starmap = {'Great Bear': {'stars': {'A':[], 'B':[], 'C':[]},'adjacencies': {'A':['B'], 'B':['A']}}}
    >>> listIsolatedStars(starmap, "Great Bear")
    ['C']
    """
    llista = []
    if constellation not in starmap:
        print("La constel·lació no existeix")
        return [] # Mejor devolver lista vacía que nada

    # Sacamos el diccionario de adjacencias para escribir menos
    adjs = starmap[constellation]['adjacencies']

    for estrella in starmap[constellation]['stars']:
        # CASO 1: No está en el diccionario de adjacencias
        # CASO 2: Está, pero su lista de vecinos está vacía (len == 0)
        if estrella not in adjs or len(adjs[estrella]) == 0:
            llista.append(estrella)
            
    return llista
