# lab 7

from nicegui import ui
from src.core.vertex_cover import calcular_vertex_cover
from matplotlib import pyplot as plt

def render_vertex_cover_tab():
    ui.label('Grafo de ejemplo ya integrado')

    def ejecutar():
        fig = calcular_vertex_cover()
        ui.pyplot(fig)

    ui.button('Mostrar Vertex Cover', on_click=ejecutar)
