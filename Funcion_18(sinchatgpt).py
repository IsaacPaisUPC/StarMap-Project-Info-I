def drawConstellation(starmap, constellation):
    """
    Dibuixa la constel·lació indicant estrelles i segments.
    """
    if constellation not in starmap:
        print("Error: La constel·lació no existeix.")
        return
    stars = starmap[constellation]['stars']
    adjs = starmap[constellation]['adjacencies']
    setupWindow(constellation)
    pen = makePen()
    drawAllStars(pen, stars)
    drawAllSegments(pen, stars, adjs)
    turtle.done()
