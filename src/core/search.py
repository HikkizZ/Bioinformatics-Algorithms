from itertools import permutations

def buscar_secuencia_objetivo(inicial, objetivo):
    if len(inicial) > 6 or len(objetivo) > 6:
        return {"error": "Las listas no pueden tener más de 6 elementos"}

    permutaciones = list(permutations(inicial))
    pasos = 0
    log_pasos = []

    for perm in permutaciones:
        pasos += 1
        log_pasos.append(f"Paso {pasos}: {list(perm)}")
        if list(perm) == objetivo:
            return {"pasos": pasos, "permutacion": list(perm), "log_pasos": log_pasos}

    return {"pasos": pasos, "permutacion": None, "log_pasos": log_pasos}