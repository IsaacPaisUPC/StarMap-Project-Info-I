"""
Tasca 20
Càlculs geomètrics — Estrella més propera
Implementeu nearestStar(starmap, constellation, star) que retorni una llista amb el nom
de les estrelles diferents de star amb distància mínima.
"""



def nearestStar(starmap, constellation, star):
    llista = []
    diccionari = {}

    for estrella in starmap[constellation]['stars']:
        if estrella != star:
            dist = distanceBetween(starmap, constellation, star, estrella)
            diccionari[estrella] = dist

    if not diccionari:
        return []

    dist_min = min(diccionari.values())

    for estrella in diccionari:
        if diccionari[estrella] == dist_min:
            llista.append(estrella)

    return llista
