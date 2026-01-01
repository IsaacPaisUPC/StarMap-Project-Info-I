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
