def limpiar_secuencia(secuencia: str) -> str:
    """
    Elimina espacios y convierte la secuencia a mayúsculas.
    """
    return secuencia.replace(" ", "").upper()


def validar_secuencia_numerica(secuencia: str) -> bool:
    """
    Verifica que la secuencia esté compuesta únicamente por dígitos y tenga máximo 6 caracteres.
    """
    return secuencia.isdigit() and len(secuencia) <= 6


def parsear_lista(texto: str) -> list:
    """
    Intenta evaluar una lista a partir de un string (ej: '1,2,3' → [1,2,3]).
    """
    try:
        return [int(x.strip()) for x in texto.split(",")]
    except:
        raise ValueError("El formato de la lista es inválido. Usa números separados por coma.")