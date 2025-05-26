# créditos

from nicegui import ui

def render_about_tab():
    ui.markdown('''
    ## Acerca del Proyecto

    Esta aplicación fue desarrollada como práctica profesional del curso **Bioinformática y Biología Computacional** de la Universidad del Bío-Bío (2024-2).

    - **Estudiantes**: Patricia González Caamaño y Felipe Miranda Rebolledo  
    - **Supervisión académica**: Dra. Tatiana Gutiérrez
    - **Lenguaje**: Python  
    - **Interfaz**: NiceGUI  
    - **Contenidos**: Alineamiento, Permutaciones, Vertex Cover, Árboles Ultramétricos y Aditivos

    ---
    ![](src/assets/UBB_Logo.png)
    ''')
