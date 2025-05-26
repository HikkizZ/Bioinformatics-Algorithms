from nicegui import ui
from src.core.search import buscar_secuencia

def render_search_tab():
    ui.label('Buscar una Secuencia Objetivo entre Permutaciones').classes('text-2xl font-bold mb-6')

    secuencia_inicial = ui.input('Secuencia Inicial (máx. 6 caracteres)').props('type=text').classes('w-1/2')
    secuencia_objetivo = ui.input('Secuencia Objetivo').props('type=text').classes('w-1/2')

    resultado = ui.label().classes('mt-4 text-lg')

    def al_buscar():
        pasos, encontrada = buscar_secuencia(secuencia_inicial.value.strip(), secuencia_objetivo.value.strip())
        if encontrada:
            resultado.text = f'Secuencias necesarias hasta encontrar objetivo: {pasos}'
        else:
            resultado.text = 'La secuencia objetivo no fue encontrada.'

    ui.button('BUSCAR SECUENCIA', on_click=al_buscar).classes('mt-4')

    # Bloque de ejemplo para guiar al usuario
    ui.label('Ejemplo de uso:').classes('text-lg font-bold mt-6')
    with ui.row():
        ui.label('Secuencia Inicial:').classes('font-semibold')
        ui.label('abc123').classes('italic')
    with ui.row():
        ui.label('Secuencia Objetivo:').classes('font-semibold')
        ui.label('1a2b3c').classes('italic')

    ui.label('Nota: ambas secuencias deben tener los mismos caracteres, pero en distinto orden.').classes('mt-2 italic')