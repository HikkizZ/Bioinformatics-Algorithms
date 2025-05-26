# lab 6

from nicegui import ui
import itertools
import time

def permutacion_basica(lista):
    if len(lista) <= 1:
        return [lista]
    resultado = []
    for i in range(len(lista)):
        resto = lista[:i] + lista[i+1:]
        for p in permutacion_basica(resto):
            resultado.append([lista[i]] + p)
    return resultado

def render_permutations_tab():
    ui.label('Generar Permutaciones de una Secuencia').classes('text-2xl font-bold mb-6')

    entrada = ui.input('Ingresa una secuencia (máximo 6 caracteres)').props('type=text').classes('w-1/2')
    salida = ui.label().classes('mt-4 text-lg')

    def calcular_permutaciones():
        secuencia = list(entrada.value.strip())
        if len(secuencia) > 6:
            salida.text = 'La secuencia debe tener un máximo de 6 caracteres.'
            return

        # Algoritmo personalizado
        inicio1 = time.time()
        resultado1 = permutacion_basica(secuencia)
        fin1 = time.time()
        tiempo1 = round((fin1 - inicio1) * 1000, 3)

        # itertools
        inicio2 = time.time()
        resultado2 = list(itertools.permutations(secuencia))
        fin2 = time.time()
        tiempo2 = round((fin2 - inicio2) * 1000, 3)

        salida.text = (
            f'Permutaciones encontradas: {len(resultado2)}\n\n'
            f'Algoritmo básico: {tiempo1} ms\n'
            f'itertools.permutations: {tiempo2} ms'
        )

    ui.button('GENERAR PERMUTACIONES', on_click=calcular_permutaciones).classes('mt-4')

    # Bloque de ejemplo
    ui.label('Ejemplo de uso:').classes('text-lg font-bold mt-6')
    with ui.row():
        ui.label('Secuencia:').classes('font-semibold')
        ui.label('abc1').classes('italic')
    ui.label('Nota: Se recomienda ingresar letras o dígitos sin espacios.').classes('mt-2 italic')
