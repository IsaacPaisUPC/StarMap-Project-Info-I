"""
functions.py
Conjunt de funcions per gestionar el mapa estel·lar.
"""
import turtle
import json

"""
Tasca1
Dissenyeu una funció de nom addConstellation(starmap,constellation) que ,donat un mapa
estel·lar i un nom de constel·lació, afegeixi una nova constel·lació buida al mapa.
"""
def addConstellation(starmap, constellation):
    """
    >>> starmap = {}
    >>> addConstellation(starmap, "Great Bear")
    >>> starmap
    {'Great Bear': {'stars': {}, 'adjacencies': {}}}
    """
    if constellation not in starmap:
        starmap[constellation] = {'stars': {},'adjacencies': {}}

"""
Tasca2
Dissenyeu una funció de nom addStars(starmap,constellation,starNames) que, donat un
mapa estel·lar, una constel·lació i una llista d’estrelles...
"""
def addStars(starmap, constellation, starNames):
    """
    >>> starmap = {'Great Bear': {'stars': {}, 'adjacencies': {}}}
    >>> addStars(starmap, "Great Bear", ["Alkaid", "Dubhe"])
    >>> starmap['Great Bear']['stars']
    {'Alkaid': [], 'Dubhe': []}
    """
    if constellation in starmap:
        for star in starNames:
            if star not in starmap[constellation]['stars']:
                starmap[constellation]['stars'][star] = []
                starmap[constellation]['adjacencies'][star] = []

"""
Tasca 3
Dissenyeu una funció de nom addAdjacencies...
"""
def addAdjacencies(starmap, constellation, baseStar, neighbors):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': [], 'Dubhe': []}}}
    >>> addAdjacencies(starmap, "Great Bear", "Alkaid", ["Dubhe"])
    >>> starmap["Great Bear"]["adjacencies"]["Alkaid"]
    ['Dubhe']
    """
    if constellation in starmap and baseStar in starmap[constellation]['stars']:
        for estrella in neighbors:
            if estrella == baseStar:
                pass 
            elif estrella not in starmap[constellation]['stars']:
                pass
            else:
                adjs = starmap[constellation]['adjacencies']
                if estrella not in adjs[baseStar]:
                    adjs[baseStar].append(estrella)
                if baseStar not in adjs[estrella]:
                    adjs[estrella].append(baseStar)

"""
Tasca4
Dissenyeu una funció de nom deleteAdjacency...
"""
def deleteAdjacency(starmap, constellation, star1, star2):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
    >>> deleteAdjacency(starmap, "Great Bear", "Alkaid", "Dubhe")
    >>> starmap["Great Bear"]["adjacencies"]["Alkaid"]
    []
    """
    if constellation in starmap:
        stars = starmap[constellation]['stars']
        if star1 in stars and star2 in stars:  
            patata = starmap[constellation]['adjacencies']
            if star2 in patata[star1]:
                patata[star1].remove(star2)
            if star1 in patata[star2]:
                patata[star2].remove(star1)

"""
Tasca 5
Dissenyeu una funció de nom deleteStar...
"""
def deleteStar(starmap, constellation, star):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, ...}}
    >>> deleteStar(starmap, "Great Bear", "Dubhe")
    >>> "Dubhe" in starmap["Great Bear"]["stars"]
    False
    """
    if constellation in starmap:
        stars = starmap[constellation]['stars']
        adjacencies = starmap[constellation]['adjacencies']
        if star in stars:
            for altra in adjacencies[star]:
                if star in adjacencies[altra]:
                    if star in adjacencies[altra]:
                        adjacencies[altra].remove(star)
            del adjacencies[star]   
            del stars[star]

"""
Tasca 6
Dissenyeu una funció de nom listAllStars...
"""
def listAllStars(starmap, constellation):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
    >>> listAllStars(starmap, "Great Bear")
    Great Bear:
    Alkaid adjacent a: Dubhe
    Dubhe adjacent a: Alkaid
    """
    if constellation in starmap:
        print(constellation + ":")
        patata = starmap[constellation]['adjacencies']
        for estrella in patata:
            estrellasadyascentes = ", ".join(patata[estrella]) 
            print(estrella + " adjacent a: " + estrellasadyascentes)

"""
Tasca 7
Dissenyeu una funció de nom listAllConstellations...
"""
def listAllConstellations(starmap):
    """
    >>> listAllConstellations({})
    No hi ha constel·lacions
    """
    if len(starmap) == 0:
        print("No hi ha constel·lacions")
    else:
        for constelacio in starmap:
            print(constelacio)

"""
Tasca 8
Dissenyeu una funció de nom assignCoordinates...
"""
def assignCoordinates(starmap, constellation, star, x, y):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': []}, 'adjacencies': {'Alkaid': []}}}
    >>> assignCoordinates(starmap, "Great Bear", "Alkaid", 10, 20)
    >>> starmap["Great Bear"]["stars"]["Alkaid"]
    [10, 20]
    """
    if constellation in starmap:
        llistaestrelles = starmap[constellation]['stars']
        if star in llistaestrelles:
            llistaestrelles[star] = [x, y]

"""
Tasca 9
Dissenyeu una funció de nom getCoordinates...
"""
def getCoordinates(starmap, constellation, star):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [10, 20]}, ...}}
    >>> getCoordinates(starmap, "Great Bear", "Alkaid")
    [10, 20]
    """
    if constellation in starmap:
        llistaestrelles = starmap[constellation]['stars']
        if star in llistaestrelles:
            return llistaestrelles[star]

"""
Tasca 10
Dissenyeu una funció de nom isValidCoord...
"""
def isValidCoord(coord):
    """
    >>> isValidCoord([10, 20])
    True
    """
    if type(coord) == str:
        return False     
    if type(coord) == int or type(coord) == float:
        return False
    if type(coord) == list and len(coord) == 2:
        return True
    return False

"""
Tasca 11
Dissenyeu una funció de nom shouldDrawOnce...
"""
def shouldDrawOnce(a,b):
    """
    >>> shouldDrawOnce("Alkaid", "Dubhe")
    True
    """
    return a < b

"""
Tasca 12
Dissenyeu una funció de nom setupWindow...
"""
import turtle
def setupWindow(constellation, width=800, height=600):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title(constellation)
    return screen

"""
Tasca 13
Dissenyeu una funció de nom makePen...
"""
def makePen():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.pensize(2)
    return pen

"""
Tasca 14
Dissenyeu una funció de nom drawStar...
"""
def drawStar(pen, name, coord, pointSize=8, offset=8):
    x = coord[0]
    y = coord[1]
    pen.goto(x, y)
    pen.dot(pointSize)
    pen.goto(x + offset, y + offset)
    pen.write(name)

"""
Tasca 15
Dissenyeu una funció de nom drawAllStars...
"""
def drawAllStars(pen, stars):
    for estrella in stars:
        coord = stars[estrella]
        if isValidCoord(coord):
            drawStar(pen, estrella, coord)

"""
Tasca 16
Dissenyeu una funció de nom drawSegment...
"""
def drawSegment(pen, aXY, bXY):
    aX, aY = aXY
    bX, bY = bXY
    pen.penup()
    pen.goto(aX, aY)
    pen.pendown()
    pen.goto(bX, bY)

"""
Tasca 17
Dissenyeu una funció de nom drawAllSegments...
"""
def drawAllSegments(pen, stars, adjacencies):
    for estrella_1, conectades in adjacencies.items():
        if estrella_1 not in stars or not isValidCoord(stars[estrella_1]):
            continue
        for estrella_2 in conectades:
            if estrella_2 not in stars or not isValidCoord(stars[estrella_2]):
                continue
            if shouldDrawOnce(estrella_1, estrella_2):
                drawSegment( pen,stars[estrella_1],stars[estrella_2])

"""
Tasca 18
Dissenyeu una funció de nom drawConstellation...
"""
def drawConstellation(starmap, constellation):
    """
    Dibuixa la constel·lació indicant estrelles (punt+nom) i segments (adjacències).
    Obre una finestra Turtle i es queda oberta fins que la tanques.
    """
    if constellation not in starmap:
        raise KeyError("Constel·lació inexistent")
    data = starmap[constellation]
    stars = data.get('stars', {})
    adjs = data.get('adjacencies', {})
    try:
        turtle.TurtleScreen._RUNNING = True
    except Exception:
        pass
    try:
        turtle.Screen().clearscreen()
    except turtle.Terminator:
        try:
            turtle.TurtleScreen._RUNNING = True
        except Exception:
            pass
    
    setupWindow(constellation)
    pen = makePen()

    drawAllStars(pen, stars)
    drawAllSegments(pen, stars, adjs)
    turtle.done()

"""
Tasca 19
Càlculs geomètrics — Distància entre dues estrelles
"""
def distanceBetween(starmap, constellation, starA, starB):
    """
    >>> starmap = {'Great Bear': {'stars': {'A':[0,0], 'B':[3,4]},'adjacencies':{}}}
    >>> round(distanceBetween(starmap, "Great Bear", "A", "B"), 2)
    5.0
    """
    if constellation not in starmap:
         print("La constel·lació  no existeix")
         return None
    else:
        if starA not in starmap[constellation]['stars']:
             print("L'estrella " + starA+ " no existeix al mapa")
             return None
        else:
            if starB not in starmap[constellation]['stars']:
                print("L'estrella" + starB+ " no existeix al mapa")
                return None
            else:
                coordA= getCoordinates(starmap,constellation,starA)
                coordB= getCoordinates(starmap,constellation,starB)
                
                if isValidCoord(coordA) == False:
                    print("l'estrella "+ starA+ " no te coordenades")
                    return None
                else:
                    if isValidCoord(coordB)== False:
                        print("l'estrella "+ starB+ " no te coordenades")
                        return None
                    else:
                        dist =((coordB[0]-coordA[0])**2 + ( coordB[1]- coordA[1])**2)**0.5
                        return dist

"""
Tasca 20
Càlculs geomètrics — Estrella més propera
"""
def nearestStar(starmap, constellation, star):
    llista = []
    diccionari = {}

    if constellation not in starmap or star not in starmap[constellation]['stars']:
        return []

    for estrella in starmap[constellation]['stars']:
        if estrella != star:
            dist = distanceBetween(starmap, constellation, star, estrella)
            if dist is not None:
                diccionari[estrella] = dist

    if not diccionari:
        return []

    dist_min = min(diccionari.values())

    for estrella in diccionari:
        if diccionari[estrella] == dist_min:
            llista.append(estrella)

    return llista

"""
Tasca 22
Persistència avançada — Guardar tot el mapa
"""
import json
def saveStarmapJSON(starmap, filepath):
    """
    >>> saveStarmapJSON(starmap, "full_map.json")
    >>> newmap = loadStarmapJSON("full_map.json")
    >>> isinstance(newmap, dict) and "Great Bear" in newmap
    True
    """
    try:
        fitxer= open(filepath,"w")
        json.dump(starmap, fitxer)
        fitxer.close()
    except:
        print("Error guardant fitxer")

def loadStarmapJSON(filepath):
    try:
        fitxer = open(filepath, "r")
        variable = json.load(fitxer)
        fitxer.close()
        return variable
    except:
        return {}

"""
Tasca 23
Persistència avançada — Còpia de seguretat
"""
def backupStarmap(starmap, filepath):
    saveStarmapJSON(starmap, filepath + ".bak.json")

def deleteStarWithBackup(starmap, constellation, star, filepath):
    """
    Copia seguretat abans d'eliminar estrella.
    """
    backupStarmap(starmap, filepath)
    deleteStar(starmap, constellation, star)

def deleteConstellationWithBackup(starmap, constellation, filepath):
    """
    Copia seguretat abans de borrar constel·lació.
    """
    backupStarmap(starmap, filepath)

    if constellation in starmap:
        del starmap[constellation]
def deleteAdjacencyWithBackup(starmap, constellation, starA, starB, filepath):
    backupStarmap(starmap, filepath)
    deleteAdjacency(starmap, constellation, starA, starB)

"""
Tasca 24
Consultes — Comptar estrelles
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
        return 0

"""
Tasca 25
Estrelles aïllades
"""
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
