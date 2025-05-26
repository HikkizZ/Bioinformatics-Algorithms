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
    resultado_texto = ui.label().classes('text-white')

    calcular_btn = ui.button('CALCULAR VERTEX COVER').props('color=primary').classes('mt-4')

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

    def ejecutar_calculo():
        try:
            fig, bf_cover, greedy_cover = calcular_vertex_cover_desde_entrada(nodos_input.value, aristas_input.value)
            resultado_texto.text = f"== Resultados de Vertex Cover ==\nFuerza Bruta: {tuple(bf_cover)}\nAproximación Greedy: {set(greedy_cover)}"
            status_label.text = '✅ Cálculo realizado correctamente.'
            status_label.classes('text-green-500')
            calcular_btn.set_visibility(False)  # Ocultar el botón
            mostrar_btn.set_visibility(True)    # Mostrar botón de mostrar grafo
        except Exception as e:
            status_label.text = f"❌ Error: {str(e)}"
            status_label.classes('text-red-500')

    calcular_btn.on('click', ejecutar_calculo)

    def ejecutar_mostrar():
        try:
            fig, _, _ = calcular_vertex_cover_desde_entrada(nodos_input.value, aristas_input.value)
            mostrar_modal_con_imagen(fig)
        except Exception as e:
            ui.notify(f"Error al mostrar el grafo: {e}", type='negative')

    mostrar_btn = ui.button('MOSTRAR VERTEX COVER', on_click=ejecutar_mostrar).props('color=primary').classes('mt-2')
    mostrar_btn.set_visibility(False)

    # Restaurar visibilidad del botón calcular si se cambia la entrada
    def reactivar_calculo(_=None):
        calcular_btn.set_visibility(True)
        mostrar_btn.set_visibility(False)
        resultado_texto.text = ""
        status_label.text = ""

    nodos_input.on('update:model-value', reactivar_calculo)
    aristas_input.on('update:model-value', reactivar_calculo)