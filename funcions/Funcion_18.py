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
