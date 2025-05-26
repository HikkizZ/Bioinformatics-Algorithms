# bienvenida

from nicegui import ui

def render_home_tab():
    ui.image('src/assets/UBB_Logo.png').classes('w-48')
    ui.markdown('''
    # Bienvenido
    Esta aplicación permite explorar algoritmos fundamentales de bioinformática desarrollados en Python. 
    Cada sección corresponde a un laboratorio del curso de Bioinformática y Biología Computacional de la Universidad del Bío-Bío.
    ''')
