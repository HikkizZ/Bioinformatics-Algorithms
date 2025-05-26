from nicegui import ui
from io import BytesIO
import base64
from src.core.vertex_cover import calcular_vertex_cover_desde_entrada


def render_vertex_cover_tab():
    ui.label("Coberturas generadas usando dos algoritmos: - "
             "<b>Fuerza Bruta (Óptimo)</b> - <b>Greedy (Aproximado)</b>").classes("text-md").style("margin-bottom: 1rem")

    nodos_input = ui.input(label='Nodos del grafo (separados por coma)').classes('w-full')
    aristas_input = ui.input(label='Aristas del grafo (como lista de tuplas)').classes('w-full')

    ui.markdown("**_Ejemplo de Entrada:_** "
                "**Nodos:** A, B, C, D, E  "
                "**Aristas:** [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E')]").classes('text-sm')

    status_label = ui.label().classes('text-green-500')

    resultado_texto = ui.markdown('').classes('text-white')
    resultado_texto.set_visibility(False)

    # BOTONES
    btn_calcular = ui.button('CALCULAR VERTEX COVER').props('color=primary')
    btn_mostrar = ui.button('MOSTRAR VERTEX COVER').props('color=primary').classes('mt-2')
    btn_limpiar = ui.button('LIMPIAR BÚSQUEDA').props('color=secondary').classes('mt-2')

    btn_mostrar.set_visibility(False)
    btn_limpiar.set_visibility(False)

    def mostrar_modal_con_imagen(fig):
        buffer = BytesIO()
        fig.set_size_inches(16, 8)
        fig.tight_layout()
        fig.savefig(buffer, format='png', bbox_inches='tight', dpi=150)
        buffer.seek(0)

        image_bytes = buffer.getvalue()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        image_url = f'data:image/png;base64,{image_base64}'

        with ui.dialog() as dialog:
            with ui.card().classes('w-[98vw] h-[90vh] flex flex-col items-center justify-center'):
                ui.label('Vertex Cover').classes('text-xl font-bold mb-4')
                ui.image(image_url).classes('max-w-full max-h-[65vh] object-contain overflow-auto')
                with ui.row().classes('justify-center mt-4'):
                    ui.button('DESCARGAR COMO PNG', on_click=lambda: ui.download(src=image_url, filename='vertex_cover.png')).props('color=primary')
                    ui.button('CERRAR', on_click=dialog.close).props('color=secondary')

        dialog.open()

    def calcular():
        try:
            fig, fuerza_bruta, greedy = calcular_vertex_cover_desde_entrada(nodos_input.value, aristas_input.value)

            resultado_texto.content = f"""### == Resultados de Vertex Cover ==
**Fuerza Bruta**: {fuerza_bruta}  
**Aproximación Greedy**: {greedy}"""
            resultado_texto.set_visibility(True)

            status_label.text = '✅ Resultado calculado correctamente.'
            status_label.classes('text-green-500')

            btn_calcular.set_visibility(False)
            btn_mostrar.set_visibility(True)
            btn_limpiar.set_visibility(True)

        except Exception as e:
            resultado_texto.set_visibility(False)
            status_label.text = f"❌ Error: {str(e)}"
            status_label.classes('text-red-500')

    def mostrar():
        try:
            fig, _, _ = calcular_vertex_cover_desde_entrada(nodos_input.value, aristas_input.value)
            mostrar_modal_con_imagen(fig)
        except Exception as e:
            ui.notify(f"Error: {e}", type='negative')

    def limpiar():
        nodos_input.value = ''
        aristas_input.value = ''
        resultado_texto.set_visibility(False)
        btn_mostrar.set_visibility(False)
        btn_limpiar.set_visibility(False)
        btn_calcular.set_visibility(True)
        status_label.text = ''

    # Conectar eventos
    btn_calcular.on_click(calcular)
    btn_mostrar.on_click(mostrar)
    btn_limpiar.on_click(limpiar)

    # Reaparecer botón calcular si el usuario cambia campos
    nodos_input.on('input', lambda _: btn_calcular.set_visibility(True))
    aristas_input.on('input', lambda _: btn_calcular.set_visibility(True))
