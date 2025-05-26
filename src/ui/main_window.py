# interfaz general con pestañas

from nicegui import ui
from src.ui.tab_home import render_home_tab
from src.ui.tab_permutations import render_permutations_tab
from src.ui.tab_search import render_search_tab
from src.ui.tab_vertex_cover import render_vertex_cover_tab
from src.ui.tab_ultrametric import render_ultrametric_tab
from src.ui.tab_additive import render_additive_tab
from src.ui.tab_about import render_about_tab

def render_main_window():
    with ui.header().classes('bg-blue-700 text-white'):
        ui.label('Bioinformatics Algorithms UBB').classes('text-xl font-bold')

    with ui.tabs().props('vertical').classes('w-64 bg-blue-50').style('height: 100vh') as tabs:
        home = ui.tab('Inicio')
        perms = ui.tab('Permutaciones')
        search = ui.tab('Buscar Secuencia')
        vertex = ui.tab('Vertex Cover')
        ultra = ui.tab('Árbol Ultramétrico')
        addit = ui.tab('Árbol Aditivo')
        about = ui.tab('Acerca de')

    with ui.tab_panels(tabs, value=home).classes('w-full p-4'):
        with ui.tab_panel(home):
            render_home_tab()
        with ui.tab_panel(perms):
            render_permutations_tab()
        with ui.tab_panel(search):
            render_search_tab()
        with ui.tab_panel(vertex):
            render_vertex_cover_tab()
        with ui.tab_panel(ultra):
            render_ultrametric_tab()
        with ui.tab_panel(addit):
            render_additive_tab()
        with ui.tab_panel(about):
            render_about_tab()
