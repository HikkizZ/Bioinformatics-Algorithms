# lab 8

from nicegui import ui
from src.core.trees import generar_arbol

def render_ultrametric_tab():
    matriz = ui.textarea('Matriz de distancias separadas por coma y salto de línea')
    def graficar():
        fig = generar_arbol(matriz.value, metodo='single')
        ui.pyplot(fig)

    ui.button('Generar Árbol Ultramétrico', on_click=graficar)
