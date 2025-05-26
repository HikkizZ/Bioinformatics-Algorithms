from nicegui import ui
from io import BytesIO
import base64
from src.core.trees import generar_arbol


def render_additive_tab():
    ui.label("Generación de Árbol Aditivo desde una matriz de distancias")\
        .classes("text-md font-semibold mb-4")

    matriz_input = ui.textarea(
        label='Matriz de Distancias',
        placeholder='Ejemplo: [[0, 2, 4], [2, 0, 5], [4, 5, 0]]'
    ).props('rows=5').classes('w-full')

    ui.markdown("**_Ejemplo válido:_** `[[0, 2, 4], [2, 0, 5], [4, 5, 0]]`")\
        .classes('text-sm text-gray-400 mb-2')

    status_label = ui.label().classes('text-green-500')

    def mostrar_modal(fig):
        buffer = BytesIO()
        fig.set_size_inches(10, 6)
        fig.tight_layout()
        fig.savefig(buffer, format='png', bbox_inches='tight', dpi=150)
        buffer.seek(0)
        image_bytes = buffer.getvalue()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        image_url = f'data:image/png;base64,{image_base64}'

        with ui.dialog() as dialog:
            with ui.card().classes('w-[95vw] h-[90vh] flex flex-col items-center justify-center'):
                ui.label('Árbol Aditivo').classes('text-xl font-bold mb-4')
                ui.image(image_url).classes('max-w-full max-h-[70vh] object-contain')
                with ui.row().classes('justify-center mt-4'):
                    ui.button('📥 DESCARGAR COMO PNG',
                        on_click=lambda: ui.download(src=image_url, filename='arbol_aditivo.png')
                    ).props('color=primary')
                    ui.button('❌ CERRAR', on_click=dialog.close).props('color=secondary')
        dialog.open()

    def calcular_y_mostrar():
        try:
            fig = generar_arbol(matriz_input.value, metodo='single')
            mostrar_modal(fig)
            status_label.text = '✅ Visualización generada correctamente.'
            status_label.classes('text-green-500')
        except Exception as e:
            status_label.text = f"❌ Error: {str(e)}"
            status_label.classes('text-red-500')

    ui.button('🌳 GENERAR ÁRBOL ADITIVO', on_click=calcular_y_mostrar)\
        .props('color=primary').classes('mt-4')