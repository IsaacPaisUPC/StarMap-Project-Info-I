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
