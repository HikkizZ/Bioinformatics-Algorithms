import time
from itertools import permutations as itertools_permutations

def generate_permutations(seq: str) -> tuple[float, int]:
    """
    Genera todas las permutaciones posibles de una secuencia utilizando backtracking.
    Retorna el tiempo de ejecución y el número total de permutaciones únicas.
    """
    seen = set()

    def backtrack(s, path):
        if not s:
            seen.add(path)
            return
        for i in range(len(s)):
            backtrack(s[:i] + s[i+1:], path + s[i])

    start = time.time()
    backtrack(seq, "")
    end = time.time()

    return round(end - start, 4), len(seen)


def generate_itertools_permutations(seq: str) -> tuple[float, int]:
    """
    Genera todas las permutaciones utilizando la biblioteca itertools.
    Retorna el tiempo de ejecución y el número total de permutaciones generadas.
    """
    start = time.time()
    perms = list(itertools_permutations(seq))
    end = time.time()

    return round(end - start, 4), len(perms)
