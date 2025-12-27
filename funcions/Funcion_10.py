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
