"""
Tasca2
Dissenyeu una funció de nom addStars(starmap,constellation,starNames) que,donat un
mapa estel·lar, una constel·lació i una llista d’estrelles , permeti afegir les estrelles donades a una
constel·lació existent. Cada estrella ha de començar sense adjacències i amb coordenades buides.
>>>starmap={'GreatBear':{'stars':{},'adjacencies':{}}}
>>>addStars(starmap,"GreatBear", ["Alkaid","Dubhe"])
>>>starmap
{'GreatBear':{'stars':{'Alkaid': [],'Dubhe':[]},
...'adjacencies':{'Alkaid':[],'Dubhe':[]}}}
"""

def addStars(starmap, constellation, starNames):
    """
    Afegeix les estrelles de la llista starNames a la constel·lació indicada del starmap.
    Cada estrella s'inicialitza amb coordenades buides ([]) i sense adjacències ([]).
    
    """
    if not starmap.get(constellation):
        print("La constelacio no existeix")

    else:
        for star in starNames:
            if starmap[constellation]['stars'].get(star):
                print("L'estrella " + star + " ja existeix a " + constellation)
            else:
                starmap[constellation]['stars'][star] = []
                starmap[constellation]['adjacencies'][star] = []
