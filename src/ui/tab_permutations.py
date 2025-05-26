# lab 6

from nicegui import ui
from src.core.permutations import generate_permutations, itertools_permutations

def render_permutations_tab():
    input_field = ui.input('Ingrese una secuencia (ej: 1234)').props('maxlength=6')
    
    def ejecutar():
        texto = input_field.value.strip()
        t1, total1 = generate_permutations(texto)
        t2, total2 = itertools_permutations(texto)

        ui.notify(f'Backtracking: {total1} permutaciones en {t1:.4f} seg')
        ui.notify(f'itertools: {total2} permutaciones en {t2:.4f} seg')

    ui.button('Comparar algoritmos', on_click=ejecutar)
