from itertools import permutations

def buscar_secuencia(inicial: str, objetivo: str) -> tuple[int, bool]:
    """
    Busca la secuencia 'objetivo' a partir de la secuencia 'inicial'
    mediante permutaciones generadas con itertools.

    Retorna:
    - Número de pasos necesarios para encontrar la secuencia
    - True si fue encontrada, False si no
    """
    if len(inicial) > 6 or len(objetivo) > 6:
        return 0, False

    permutaciones = permutations(inicial)
    for i, p in enumerate(permutaciones, 1):
        if ''.join(p) == objetivo:
            return i, True

    return 0, False