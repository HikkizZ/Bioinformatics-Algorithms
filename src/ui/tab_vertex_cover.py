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

    btn_calcular = ui.button('CALCULAR VERTEX COVER').props('color=primary').classes('mt-4')
    with ui.row().classes('gap-4 mt-2'):
        btn_mostrar = ui.button('MOSTRAR VERTEX COVER').props('color=primary')
        btn_fuerza_bruta = ui.button('MOSTRAR SOLO FUERZA BRUTA').props('color=green')
        btn_greedy = ui.button('MOSTRAR SOLO GREEDY').props('color=orange')

    btn_limpiar = ui.button('LIMPIAR BÚSQUEDA').props('color=secondary').classes('mt-2')

    # Ocultar todos inicialmente
    for btn in [btn_mostrar, btn_fuerza_bruta, btn_greedy, btn_limpiar]:
        btn.set_visibility(False)

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
            fig, bf, greedy = calcular_vertex_cover_desde_entrada(nodos_input.value, aristas_input.value)

            resultado_texto.content = f"""### == Resultados de Vertex Cover ==
**Fuerza Bruta**: {bf}  
**Aproximación Greedy**: {greedy}"""
            resultado_texto.set_visibility(True)

            status_label.text = '✅ Cálculo realizado correctamente.'
            status_label.classes('text-green-500')

            btn_calcular.set_visibility(False)
            for btn in [btn_mostrar, btn_fuerza_bruta, btn_greedy, btn_limpiar]:
                btn.set_visibility(True)

        except Exception as e:
            resultado_texto.set_visibility(False)
            status_label.text = f"❌ Error: {str(e)}"
            status_label.classes('text-red-500')

    def mostrar():
        try:
            fig, _, _ = calcular_vertex_cover_desde_entrada(nodos_input.value, aristas_input.value)
            mostrar_modal_con_imagen(fig)
        except Exception as e:
            ui.notify(f"Error al mostrar: {e}", type='negative')

    def mostrar_solo_fuerza_bruta():
        try:
            _, bf_cover, _ = calcular_vertex_cover_desde_entrada(nodos_input.value, aristas_input.value)
            import networkx as nx
            import matplotlib.pyplot as plt

            nodos = [n.strip() for n in nodos_input.value.split(',')]
            aristas = eval(aristas_input.value)
            G = nx.Graph()
            G.add_nodes_from(nodos)
            G.add_edges_from(aristas)

            pos = nx.spring_layout(G, seed=42)
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.set_title("Fuerza Bruta (Óptimo)")
            nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000)
            nx.draw_networkx_nodes(G, pos, nodelist=bf_cover, ax=ax, node_color='green', node_size=1200)

            mostrar_modal_con_imagen(fig)
        except Exception as e:
            ui.notify(f"Error en fuerza bruta: {e}", type='negative')

    def mostrar_solo_greedy():
        try:
            _, _, greedy_cover = calcular_vertex_cover_desde_entrada(nodos_input.value, aristas_input.value)
            import networkx as nx
            import matplotlib.pyplot as plt

            nodos = [n.strip() for n in nodos_input.value.split(',')]
            aristas = eval(aristas_input.value)
            G = nx.Graph()
            G.add_nodes_from(nodos)
            G.add_edges_from(aristas)

            pos = nx.spring_layout(G, seed=42)
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.set_title("Greedy (Aproximado)")
            nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000)
            nx.draw_networkx_nodes(G, pos, nodelist=greedy_cover, ax=ax, node_color='orange', node_size=1200)

            mostrar_modal_con_imagen(fig)
        except Exception as e:
            ui.notify(f"Error en greedy: {e}", type='negative')

    def limpiar():
        nodos_input.value = ''
        aristas_input.value = ''
        resultado_texto.set_visibility(False)
        status_label.text = ''
        btn_calcular.set_visibility(True)
        for btn in [btn_mostrar, btn_fuerza_bruta, btn_greedy, btn_limpiar]:
            btn.set_visibility(False)

    btn_calcular.on_click(calcular)
    btn_mostrar.on_click(mostrar)
    btn_fuerza_bruta.on_click(mostrar_solo_fuerza_bruta)
    btn_greedy.on_click(mostrar_solo_greedy)
    btn_limpiar.on_click(limpiar)

    nodos_input.on('input', lambda _: btn_calcular.set_visibility(True))
    aristas_input.on('input', lambda _: btn_calcular.set_visibility(True))