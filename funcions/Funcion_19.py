"""
Tasca 19
Càlculs geomètrics — Distància entre dues estrelles
Implementeu una funció distanceBetween(starmap, constellation, starA, starB) que retorni la distància euclidiana entre dues estrelles amb coordenades definides (x, y).
Exemple:
>>> starmap = {'Great Bear': {'stars': {'A':[0,0], 'B':[3,4]},
'adjacencies':{}}}
>>> round(distanceBetween(starmap, "Great Bear", "A", "B"), 2)
5.0
A tenir en compte: Valideu que ambdues estrelles tinguin coordenades. Gestioneu els errors amb
missatges clars.
"""
def distanceBetween(starmap, constellation, starA, starB):
    """
    >>> starmap = {'Great Bear': {'stars': {'A':[0,0], 'B':[3,4]},'adjacencies':{}}}
    >>> round(distanceBetween(starmap, "Great Bear", "A", "B"), 2)
    5.0
    """
    if constellation not in starmap:
         print("La constel·lació  no existeix")
    else:
        if starA not in starmap[constellation]['stars']:
             print("L'estrella " + starA+ " no existeix al mapa")
        else:
            if starB not in starmap[constellation]['stars']:
                print("L'estrella" + starB+ " no existeix al mapa")
            else:
                coordA= getCoordinates(starmap,constellation,starA)
                coordB= getCoordinates(starmap,constellation,starB)
                
                if isValidCoord(coordA) == False:
                    print("l'estrella "+ starA+ " no te coordenades")
                else:
                    if isValidCoord(coordB)== False:
                        print("l'estrella "+ starB+ " no te coordenades")
                    else:
                        dist =((coordB[0]-coordA[0])**2 + ( coordB[1]- coordA[1])**2)**0.5
                        return dist
