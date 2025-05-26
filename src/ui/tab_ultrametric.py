from nicegui import ui
from io import BytesIO
import base64
from src.core.trees import generar_arbol


def render_ultrametric_tab():
    ui.markdown('## Árbol Ultramétrico (Clustering Jerárquico)').classes('mb-4')

    ui.label('Ingrese una matriz cuadrada simétrica de distancias').classes('text-md')

    matriz_input = ui.textarea(
        label='Matriz de Distancias',
        placeholder='Ejemplo: [[0, 2, 4], [2, 0, 5], [4, 5, 0]]'
    ).props('rows=5').classes('w-full')


    ui.markdown("**_Ejemplo válido:_** `[[0, 2, 4], [2, 0, 5], [4, 5, 0]]`").classes('text-sm')

    estado_label = ui.label().classes('text-green-500')
    imagen_modal_url = None  # para mantener última imagen

    def mostrar_modal(fig):
        nonlocal imagen_modal_url

        buffer = BytesIO()
        fig.set_size_inches(16, 8)
        fig.tight_layout()
        fig.savefig(buffer, format='png', bbox_inches='tight', dpi=150)
        buffer.seek(0)

        image_bytes = buffer.getvalue()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        imagen_modal_url = f'data:image/png;base64,{image_base64}'

        with ui.dialog() as dialog:
            with ui.card().classes('w-[98vw] h-[90vh] flex flex-col items-center justify-center'):
                ui.label('Árbol Ultramétrico').classes('text-xl font-bold mb-4')
                ui.image(imagen_modal_url).classes('max-w-full max-h-[65vh] object-contain overflow-auto')
                with ui.row().classes('justify-center mt-4'):
                    ui.button('📥 Descargar PNG', on_click=lambda: ui.download(src=imagen_modal_url, filename='ultrametric_tree.png')).props('color=primary')
                    ui.button('❌ Cerrar', on_click=dialog.close).props('color=secondary')
        dialog.open()

    def calcular_ultrametrico():
        try:
            fig = generar_arbol(matriz_input.value, metodo='average')
            mostrar_modal(fig)
            estado_label.text = '✅ Árbol generado correctamente.'
            estado_label.classes('text-green-500')
        except Exception as e:
            estado_label.text = f"❌ Error: {str(e)}"
            estado_label.classes('text-red-500')

    ui.button('🌳 GENERAR ÁRBOL ULTRAMÉTRICO', on_click=calcular_ultrametrico).props('color=primary').classes('mt-4')