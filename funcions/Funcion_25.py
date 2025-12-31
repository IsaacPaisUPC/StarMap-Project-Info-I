"""
Tasca 25
Consultes — Estrelles aïllades
Implementeu listIsolatedStars(starmap, constellation) que retorni una llista d’estrelles
sense adjacències.
Exemple:
>>> starmap = {'Great Bear': {'stars': {'A':[], 'B':[], 'C':[]},
... 'adjacencies': {'A':['B'], 'B':['A']}}}
>>> listIsolatedStars(starmap, "Great Bear")
['C']

"""
def listIsolatedStars(starmap, constellation):
    """
    >>> starmap = {'Great Bear': {'stars': {'A':[], 'B':[], 'C':[]},'adjacencies': {'A':['B'], 'B':['A']}}}
    >>> listIsolatedStars(starmap, "Great Bear")
    ['C']
    """
    llista=[]
    if constellation not in starmap:
        print("La constel·lació no existeix")
    else:
        for estrella in starmap[constellation]['stars']:
            if estrella not in starmap[constellation]['adjacencies']:
                llista.append(estrella)
    return llista
