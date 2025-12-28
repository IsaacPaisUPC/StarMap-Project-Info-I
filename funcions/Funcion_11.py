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
