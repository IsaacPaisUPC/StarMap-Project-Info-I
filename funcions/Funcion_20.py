"""
Tasca 20
Càlculs geomètrics — Estrella més propera
Implementeu nearestStar(starmap, constellation, star) que retorni una llista amb el nom
de les estrelles diferents de star amb distància mínima.
Exemple:
>>> starmap = {'Great Bear': {'stars': {'A':[0,0],'B':[3,4],'C':[10,0]},
'adjacencies':{}}}
>>> nearestStar(starmap, "Great Bear", "C")
['B']
"""
def nearestStar(starmap, constellation, star):
    """
    >>> starmap = {'Great Bear': {'stars': {'A':[0,0],'B':[3,4],'C':[10,0]},'adjacencies':{}}}
    >>> nearestStar(starmap, "Great Bear", "C")
    ['B']
    >>> starmap = {'Great Bear': {'stars': {'A':[4,3],'B':[4,-3],'C':[10,0]},'adjacencies':{}}}
    >>> nearestStar(starmap, "Great Bear", "C")
    ['A', 'B']
    """
    llista= []
    diccionari= {}
    for estrella in starmap[constellation]['stars']:
        if estrella != star:
            dist =round(distanceBetween(starmap, constellation, star, estrella),2)
            diccionari[estrella]= dist
            
    dist_min= round(min(diccionari.values()),2)
    for estrella in diccionari:
        if diccionari[estrella] == dist_min:
            llista.append(estrella)

    return llista
