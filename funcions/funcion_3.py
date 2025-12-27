def addAdjacencies(starmap,constellation,baseStar,neighbors):
    """
    >>> addAdjacencies(starmap,"Great Bear", "Alkaid", ["Dubhe"])
    {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
    >>> addAdjacencies(starmap,"Osa Major", "Alkaid", ["Dubhe"])
    La constelacio no existeix
    >>> addAdjacencies(starmap,"Great Bear", "Alfa", ["Dubhe"])
    L'estrella base no existeix
    >>> addAdjacencies(starmap,"Great Bear", "Alkaid", ["Alkaid"])
    No es poden establir autoadjecencies
    
    """
    if constellation not in starmap:
        print("La constelacio no existeix")
    else:
        if baseStar not in starmap[constellation]['stars']: 
            print("L'estrella base no existeix")
        else:
            for estrella in neighbors:
                if estrella == baseStar:
                    print("No es poden establir autoadjecencies")
                    return # Aixo es perque passi els doctestos(perque no hem surti el diccionari depres del print), alhora de guardar ns si donara error perque representa que la funcio no te res. 
                else:
                    if estrella not in starmap[constellation]['stars']:
                        print(" l'estrella amb la que vols establir una adjecencia no existeix")
                    else:
                        if estrella not in starmap[constellation]['adjacencies'][baseStar]:
                            starmap[constellation]['adjacencies'][baseStar].append(estrella)
                        if baseStar not in starmap[constellation]['adjacencies'][estrella]:
                            starmap[constellation]['adjacencies'][estrella].append(baseStar)
            return starmap
