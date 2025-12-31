"""
Tasca 24
Consultes — Comptar estrelles
Implementeu countStars(starmap, constellation) que retorni el nombre total d’estrelles.
Exemple:
>>> starmap = {'Great Bear': {'stars': {'A':[], 'B':[], 'C':[]}, 'adjacencies':{}}}
>>> countStars(starmap, "Great Bear")
3
"""
def countStars(starmap, constellation):
    """
    >>> starmap = {'Great Bear': {'stars': {'A':[], 'B':[], 'C':[]}, 'adjacencies':{}}}
    >>> countStars(starmap, "Great Bear")
    3
    """
    if constellation in starmap:
        contador = 0
        for estrella in starmap[constellation]['stars']:
            contador = contador + 1
        return contador
             
    else:
        print(" La contel·lació no existeix")
