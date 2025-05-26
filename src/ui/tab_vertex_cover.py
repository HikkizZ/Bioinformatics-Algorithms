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

    def mostrar_modal_con_imagen(fig):
        # Generar imagen como base64
        buffer = BytesIO()
        fig.set_size_inches(16, 8)
        fig.tight_layout()
        fig.savefig(buffer, format='png', bbox_inches='tight', dpi=150)
        buffer.seek(0)

        image_bytes = buffer.getvalue()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        image_url = f'data:image/png;base64,{image_base64}'

        # Mostrar modal con imagen y botón de descarga
        with ui.dialog() as dialog:
            with ui.card().classes('w-[95vw] h-[95vh] items-center justify-center'):
                ui.label('Vertex Cover').classes('text-xl font-bold')
                ui.image(image_url).classes('w-full h-[75vh] object-contain')

                def descargar():
                    ui.download(src=image_url, filename='vertex_cover.png')

                ui.button('DESCARGAR COMO PNG', on_click=descargar).props('color=primary').classes('mt-4')
                ui.button('CERRAR', on_click=dialog.close).props('color=secondary')

        dialog.open()

    def ejecutar():
        try:
            fig = calcular_vertex_cover_desde_entrada(nodos_input.value, aristas_input.value)
            mostrar_modal_con_imagen(fig)
            status_label.text = '✅ Visualización generada correctamente.'
            status_label.classes('text-green-500')
        except Exception as e:
            status_label.text = f"❌ Error: {str(e)}"
            status_label.classes('text-red-500')

    ui.button('MOSTRAR VERTEX COVER', on_click=ejecutar).props('color=primary').classes('mt-4')