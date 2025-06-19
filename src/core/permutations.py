import time
from itertools import permutations as itertools_permutations

def generate_permutations(seq: str) -> tuple[float, int]:
    """
    Genera todas las permutaciones posibles de una secuencia utilizando backtracking.
    Retorna el tiempo de ejecución en milisegundos y el número total de permutaciones únicas.
    """
    seen = set()

    def backtrack(s, path):
        if not s:
            seen.add(path)
            return
        for i in range(len(s)):
            backtrack(s[:i] + s[i+1:], path + s[i])

    start = time.perf_counter()
    backtrack(seq, "")
    end = time.perf_counter()

    tiempo_ms = round((end - start) * 1000, 4)
    return tiempo_ms, len(seen)


def generate_itertools_permutations(seq: str) -> tuple[float, int]:
    """
    Genera todas las permutaciones utilizando la biblioteca itertools.
    Retorna el tiempo de ejecución en milisegundos y el número total de permutaciones generadas.
    """
    start = time.perf_counter()
    perms = list(itertools_permutations(seq))
    end = time.perf_counter()

    tiempo_ms = round((end - start) * 1000, 4)
    return tiempo_ms, len(perms)