"""
Tasca1
Dissenyeu una funció de nom addConstellation(starmap,constellation) que ,donat un mapa
estel·lar i un nom de constel·lació, afegeixi una nova constel·lació buida al mapa.
>>>starmap={}
>>>addConstellation(starmap,"GreatBear")
>>>starmap
{'GreatBear':{'stars':{},'adjacencies':{}}}

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
mapa estel·lar, una constel·lació i una llista d’estrelles, permeti afegir les estrelles donades a una
constel·lació existent. Cada estrella ha de començar sense adjacències i amb coordenades buides.

Exemple:
>>> starmap = {'GreatBear': {'stars': {}, 'adjacencies': {}}}
>>> addStars(starmap, "GreatBear", ["Alkaid", "Dubhe"])
>>> starmap
{'GreatBear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': [], 'Dubhe': []}}}
"""
def addStars(starmap, constellation, starNames):
    """
    >>> starmap = {'Great Bear': {'stars': {}, 'adjacencies': {}}}
    >>> addStars(starmap, "Great Bear", ["Alkaid", "Dubhe"])
    >>> starmap['Great Bear']['stars']
    {'Alkaid': [], 'Dubhe': []}
    >>> starmap['Great Bear']['adjacencies']
    {'Alkaid': [], 'Dubhe': []}
    """
    if constellation in starmap:
        for star in starNames:
            if star not in starmap[constellation]['stars']:
                starmap[constellation]['stars'][star] = []
                starmap[constellation]['adjacencies'][star] = []

"""
Tasca 3
Dissenyeu una funció de nom addAdjacencies(starmap, constellation, baseStar, neighbors)
que, donat un mapa estel·lar, una constel·lació, una estrella base i una llista d’estrelles adjacents,
estableixi les connexions bidireccionals. No s’han de permetre duplicats ni auto-adjacències. No es
crearà l’adjacència si alguna de les dues estrelles no existeix encara a la constel·lació.

Exemple:
>>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []},
... 'adjacencies': {'Alkaid': [], 'Dubhe': []}}}
>>> addAdjacencies(starmap, "Great Bear", "Alkaid", ["Dubhe"])
>>> starmap["Great Bear"]["adjacencies"]["Alkaid"]
['Dubhe']
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
Dissenyeu una funció de nom deleteAdjacency(starmap,constellation,star1,star2), que
donat un mapa estel·lar, un nom de constel·lació, i dos noms d’estrella, elimini la connexió entre
les dues estrelles donades.
>>>starmap={'GreatBear':{'stars':{'Alkaid':[], 'Dubhe':[]},
...'adjacencies':{'Alkaid':['Dubhe'],'Dubhe':['Alkaid']}}}
>>>deleteAdjacency(starmap,"Great Bear","Alkaid","Dubhe")
>>>starmap["GreatBear"]["adjacencies"]["Alkaid"]
[]
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
Dissenyeu una funció de nom deleteStar(starmap, constellation, star) que, donat un mapa
estel·lar, una constel·lació i un nom d’estrella, elimini l’estrella de la constel·lació (així com totes
les seves adjacències).
>>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []},
... 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
>>> deleteStar(starmap, "Great Bear", "Dubhe")
>>> "Dubhe" in starmap["Great Bear"]["stars"]
False
>>> starmap
{'Great Bear': {'stars': {'Alkaid': []}, 'adjacencies': {'Alkaid': []}}}

"""
def deleteStar(starmap, constellation, star):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []},
    ... 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
    >>> deleteStar(starmap, "Great Bear", "Dubhe")
    >>> "Dubhe" in starmap["Great Bear"]["stars"]
    False
    >>> starmap
    {'Great Bear': {'stars': {'Alkaid': []}, 'adjacencies': {'Alkaid': []}}}
    """
    if constellation in starmap:
        stars = starmap[constellation]['stars']
        adjacencies = starmap[constellation]['adjacencies']
        if star in stars:
           
            for altra in adjacencies[star]:
                if star in adjacencies[altra]:
                    pos = adjacencies[altra].index(star)
                    del adjacencies[altra][pos]
            del adjacencies[star]   
            del stars[star]
"""
Tasca 6
Dissenyeu una funció de nom listAllStars(starmap, constellation), que donat un mapa estel·lar i una constel·lació, 
mostri per pantalla totes les estrelles de la constel·lació i les seves adjacències.
Exemple:
>>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []},
... 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
>>> listAllStars(starmap, "Great Bear")
Great Bear:
Alkaid adjacent a: Dubhe
Dubhe adjacent a: Alkaid
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
Dissenyeu una funció de nom listAllConstellations(starmap) que, donat un mapa estel·lar,
mostri per pantalla el nom de totes les constel lacions guardades al mapa.

Exemple:
>>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
>>> listAllConstellations (starmap)
Great Bear
>>> starmap = {}
>>> listAllConstellations (starmap)
No hi ha constel·lacions
"""
def listAllConstellations(starmap):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
    >>> listAllConstellations(starmap)
    Great Bear
    >>> starmap = {}
    >>> listAllConstellations(starmap)
    No hi ha constel·lacions
    """
    if len(starmap) == 0:
        print("No hi ha constel·lacions")
    else:
        for constelacio in starmap:
            print(constelacio)
"""
Tasca 8
Dissenyeu una funció de nom assignCoordinates(starmap, constellation, star, x, y) que,
donat un mapa estel·lar, una constel·lació, una estrella i les coordenades x i y, assigni les
coordenades [x,y] a l'estrella de la constel·lació donada.

>>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
>>> assignCoordinates(starmap, "Great Bear", "Alkaid", 10, 20)
>>> starmap["Great Bear"]["stars"]["Alkaid"]
[10, 20]
"""

def assignCoordinates(starmap, constellation, star, x, y):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
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
Dissenyeu una funció de nom getCoordinates(starmap, constellation, star) que, donat un
mapa estel·lar, una constel·lació i una estrella, retorni les coordenades de l'estrella donada.

>>> starmap = {'Great Bear': {'stars': {'Alkaid': [10, 20], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
>>> getCoordinates(starmap, "Great Bear", "Alkaid")
[10, 20]
"""

def getCoordinates(starmap, constellation, star):
    """
    >>> starmap = {'Great Bear': {'stars': {'Alkaid': [10, 20], 'Dubhe': []}, 'adjacencies': {'Alkaid': ['Dubhe'], 'Dubhe': ['Alkaid']}}}
    >>> getCoordinates(starmap, "Great Bear", "Alkaid")
    [10, 20]
    """
    if constellation in starmap:
        llistaestrelles = starmap[constellation]['stars']
        if star in llistaestrelles:
            return llistaestrelles[star]
"""
Tasca 10
Dissenyeu una funció de nom isValidCoord(coord) que, donada una coordenada, retorni True si
la coordenada donada és una llista de longitud 2 (p.ex. [x, y]), i False altrament.

>>> isValidCoord([10, 20])
True
>>> isValidCoord((0, 0))
True
>>> isValidCoord([1])
False
>>> isValidCoord("10,20")
False
"""

def isValidCoord(coord):
    """
    >>> isValidCoord([10, 20])
    True
    >>> isValidCoord((0, 0))
    True
    >>> isValidCoord([1])
    False
    >>> isValidCoord("10,20")
    False
    """
    if type(coord) == str:
        return False     
    if type(coord) == int or type(coord) == float:
        return False
    if len(coord) == 2:
        return True
        
    return False

"""
Tasca 11
Dissenyeu una funció de nom shouldDrawOnce(a, b) que, donats dos textos corresponents a
noms d’estrelles, retorni True només si el nom a va abans que b (ordre alfabètic).
NOTA: Aquesta funció s’utilitza per evitar dibuixar dues vegades el mateix segment (bidireccional).

Exemple:
>>> shouldDrawOnce("Alkaid", "Dubhe")
True
>>> shouldDrawOnce("Dubhe", "Alkaid")
False
>>> shouldDrawOnce("A", "A")
False
"""
def shouldDrawOnce(a,b):
    """
    >>> shouldDrawOnce("Alkaid", "Dubhe")
    True
    >>> shouldDrawOnce("Dubhe", "Alkaid")
    False
    >>> shouldDrawOnce("A", "A")
    False
    """
    return a < b
"""
Tasca 12
Dissenyeu una funció de nom setupWindow(constellation, width=800, height=600) que creï
la finestra de turtle, en fixi el títol i la mida, i retorni l’objecte Screen.
Nota: aquestes funcions visuals no tenen doctest.
"""
import turtle

def setupWindow(constellation, width=800, height=600):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title(constellation)
    return screen



"""
Tasca 13
Dissenyeu una funció de nom makePen() que creï i retorni una tortuga a punt per dibuixar. La
configuració de la tortuga ha de ser: amagada, màxima velocitat, llapis aixecat i gruix de línia 2.
"""

import turtle

def makePen():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.pensize(2)
    return pen

"""
Tasca 14
Dissenyeu una funció de nom drawStar(pen, name, coord, pointSize=8, offset=8) que,
donada una tortuga, un nom d'estrella, unes coordenades, la mida de punt i un desplaçament, dibuixi
un punt a coord i escrigui name desplaçat lleugerament per no tapar el punt.
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
Dissenyeu una funció de nom drawAllStars(pen, stars) que, donada una tortuga i un diccionari
d’estrelles (amb coordenades), dibuixi totes les estrelles amb coordenades vàlides [x, y].
"""

def drawAllStars(pen, stars):
    for estrella in stars:
        coord = stars[estrella]
        if isValidCoord(coord):
            drawStar(pen, estrella, coord)


"""
Tasca 16
Dissenyeu una funció de nom drawSegment(pen, aXY, bXY) que, donada una tortuga i dues
coordenades, dibuixi una línia des de aXY=(aX, aY) fins a bXY=(bX, bY).
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
Dissenyeu una funció de nom drawAllSegments(pen, stars, adjacencies) que, donada una
tortuga, un diccionari d’estrelles, i un diccionari d’adjacències, recorri totes les adjacències i dibuixi
segments només quan should_draw_once(a,b) sigui True. Ignoreu noms sense coordenades vàlides.
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
Dissenyeu una funció de nom drawConstellation(starmap, constellation que, fent ús de les
funcions definides anteriorment:
1. Comprova que la constel·lació existeix.
2. Obre finestra i crea llapis.
3. Dibuixa totes les estrelles i segments.
4. Manté la finestra oberta amb turtle.done().
En aquest cas us proporcionem el codi d’aquesta funció que podeu fer servir a la vostra solució i que,
si totes les funcions anteriors han estat correctament implementades, hauria de funcionar.
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
"""
Tasca 22
Persistència avançada — Guardar tot el mapa
Implementeu saveStarmapJSON(starmap, filepath) i loadStarmapJSON(filepath) per desar i
carregar el mapa sencer (totes les constel·lacions).
Exemple:
>>> saveStarmapJSON(starmap, "full_map.json")
>>> newmap = loadStarmapJSON("full_map.json")
>>> isinstance(newmap, dict) and "Great Bear" in newmap
True
"""
import json
def saveStarmapJSON(starmap, filepath):
    """
    >>> saveStarmapJSON(starmap, "full_map.json")
    >>> newmap = loadStarmapJSON("full_map.json")
    >>> isinstance(newmap, dict) and "Great Bear" in newmap
    True
    """
    fitxer= open(filepath,"w")
    json.dump(starmap, fitxer)
    fitxer.close()

def loadStarmapJSON(filepath):
    fitxer = open(filepath, "r")
    variable = json.load(fitxer)
    fitxer.close()
    return variable
"""
Tasca 23
Persistència avançada — Còpia de seguretat
Abans d’una operació destructiva (deleteStar, deleteAdjacency, deleteConstellation), creeu
automàticament un fitxer .bak.json amb l’estat actual de la constel·lació (o del mapa sencer si ho
preferiu).
"""

def backupStarmap(starmap, filepath):
    saveStarmapJSON(starmap, filepath + ".bak.json")


def deleteStarWithBackup(starmap, constellation, star, filepath):
    """
Esto lo que hace es crear una copia de seguridad antes de eliminar una estrella.
    """
    backupStarmap(starmap, filepath)
    deleteStar(starmap, constellation, star)


def deleteConstellationWithBackup(starmap, constellation, filepath):
    """
Y esto lo que hace es crear una copia de seguridad antes de borrar una constelacion.
    """
    backupStarmap(starmap, filepath)

    if constellation in starmap:
        del starmap[constellation]


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
