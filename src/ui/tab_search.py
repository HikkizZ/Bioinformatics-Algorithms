# lab 6 (buscar secuencia)

from nicegui import ui
from src.core.search import buscar_secuencia

def render_search_tab():
    inicio = ui.input('Secuencia inicial (ej: 1234)').props('maxlength=6')
    objetivo = ui.input('Secuencia objetivo').props('maxlength=6')

    def buscar():
        pasos, encontrado = buscar_secuencia(inicio.value, objetivo.value)
        if encontrado:
            ui.notify(f'Secuencia encontrada en {pasos} pasos')
        else:
            ui.notify('Secuencia no encontrada')

    ui.button('Buscar secuencia', on_click=buscar)
