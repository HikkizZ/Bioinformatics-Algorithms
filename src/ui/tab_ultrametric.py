# lab 8

from nicegui import ui
from src.core.trees import generar_arbol

def render_ultrametric_tab():
    ui.label('Árbol Ultramétrico (Método Average-Linkage)').classes('text-2xl font-bold mb-6')

    entrada = ui.textarea('Ingrese la matriz de distancias (formato tipo [[0,1,2],[1,0,3],[2,3,0]])').classes('w-full h-32')

    resultado = ui.label().classes('mt-4 text-lg')

    def generar():
        try:
            figura = generar_arbol(entrada.value, metodo='average')
            ui.pyplot(figure=figura)
            resultado.text = 'Árbol generado correctamente.'
        except Exception as e:
            resultado.text = f'Error: {e}'

    ui.button('GENERAR ÁRBOL ULTRAMÉTRICO', on_click=generar).classes('mt-4')

    # Bloque de ejemplo
    ui.label('Ejemplo de uso:').classes('text-lg font-bold mt-6')
    ui.label('Ingrese algo como:').classes('font-semibold')
    ui.label('[[0, 5, 9, 9, 8], [5, 0, 10, 10, 9], [9, 10, 0, 8, 7], [9, 10, 8, 0, 3], [8, 9, 7, 3, 0]]').classes('italic')
    ui.label('Nota: la matriz debe ser cuadrada, simétrica y con ceros en la diagonal.').classes('mt-2 italic')