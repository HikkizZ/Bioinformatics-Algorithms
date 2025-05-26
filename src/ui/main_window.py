from nicegui import ui
from src.ui.tab_home import render_home_tab
from src.ui.tab_permutations import render_permutations_tab
from src.ui.tab_search import render_search_tab
from src.ui.tab_vertex_cover import render_vertex_cover_tab
from src.ui.tab_ultrametric import render_ultrametric_tab
from src.ui.tab_additive import render_additive_tab
from src.ui.tab_about import render_about_tab

def render_main_window():
    ui.query('body').classes('bg-black text-white')

    with ui.header().classes('bg-blue-700 text-white'):
        ui.label('Bioinformatics Algorithms UBB').classes('text-xl font-bold')

    with ui.element().classes('flex w-full h-[calc(100vh-3rem)]'):  # Altura total menos header (3rem aprox)
        with ui.tabs().props('vertical').classes('w-1/5 h-full bg-blue-100 text-black') as tabs:
            tab_home = ui.tab('INICIO')
            tab_perm = ui.tab('PERMUTACIONES')
            tab_search = ui.tab('BUSCAR SECUENCIA')
            tab_vertex = ui.tab('VERTEX COVER')
            tab_ultra = ui.tab('ÁRBOL ULTRAMÉTRICO')
            tab_add = ui.tab('ÁRBOL ADITIVO')
            tab_about = ui.tab('ACERCA DE')

        with ui.tab_panels(tabs, value=tab_home).classes('w-4/5 h-full p-6 overflow-auto'):
            with ui.tab_panel(tab_home):
                render_home_tab()
            with ui.tab_panel(tab_perm):
                render_permutations_tab()
            with ui.tab_panel(tab_search):
                render_search_tab()
            with ui.tab_panel(tab_vertex):
                render_vertex_cover_tab()
            with ui.tab_panel(tab_ultra):
                render_ultrametric_tab()
            with ui.tab_panel(tab_add):
                render_additive_tab()
            with ui.tab_panel(tab_about):
                render_about_tab()