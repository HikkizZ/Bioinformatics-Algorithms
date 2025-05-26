# src/ui/tab_vertex_cover.py

from nicegui import ui
import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
import io
import base64

def is_vertex_cover(graph, subset):
    for u, v in graph.edges():
        if u not in subset and v not in subset:
            return False
    return True

def brute_force_vertex_cover(graph):
    nodes = list(graph.nodes())
    for k in range(1, len(nodes) + 1):
        for subset in combinations(nodes, k):
            if is_vertex_cover(graph, subset):
                return set(subset)
    return set()

def greedy_vertex_cover(graph):
    G = graph.copy()
    cover = set()
    while G.number_of_edges() > 0:
        max_degree_node = max(G.degree, key=lambda x: x[1])[0]
        cover.add(max_degree_node)
        G.remove_node(max_degree_node)
    return cover

def dibujar_grafo(G, vertex_cover, titulo, color):
    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots(figsize=(6, 5))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=vertex_cover, node_color=color, node_size=1200, ax=ax)
    ax.set_title(titulo)
    fig.tight_layout()
    return fig

def mostrar_grafico(fig, titulo):
    buf = io.BytesIO()
    fig.set_size_inches(10, 6)  # Asegura tamaño horizontal adecuado
    fig.tight_layout()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_bytes = buf.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    src = f'data:image/png;base64,{img_base64}'

    with ui.dialog() as dialog:
        dialog.classes('w-full max-w-[95vw] max-h-[95vh]')
        with ui.card().classes('w-full h-full items-center justify-center'):
            ui.label(titulo).classes('text-xl font-bold mb-2')
            ui.image(src).classes('w-full max-h-[80vh] object-contain')
            ui.button('CERRAR', on_click=dialog.close).props('color=primary')

    dialog.open()

def render_vertex_cover_tab():
    ui.markdown('## Cobertura de Vértices (Vertex Cover)')
    ui.markdown('Coberturas generadas usando dos algoritmos: - **Fuerza Bruta (Óptimo)** - **Greedy (Aproximado)**')

    nodos_input = ui.input(label='Nodos del grafo (separados por coma)', placeholder='Ej: A, B, C, D, E')
    aristas_input = ui.input(label='Aristas del grafo (como lista de tuplas)', placeholder="Ej: [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E')]")

    ui.markdown("_**Ejemplo de Entrada:**_ **Nodos:** A, B, C, D, E  **Aristas:** [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E')]")

    resultado_label = ui.label()

    imagen_area = ui.row().classes('w-full justify-center items-center')

    def calcular_y_mostrar():
        try:
            nodos = [n.strip() for n in nodos_input.value.split(",") if n.strip()]
            aristas = eval(aristas_input.value)

            G = nx.Graph()
            G.add_nodes_from(nodos)
            G.add_edges_from(aristas)

            bf_cover = brute_force_vertex_cover(G)
            greedy_cover = greedy_vertex_cover(G)

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
            pos = nx.spring_layout(G, seed=42)

            # Brute Force
            ax1.set_title("Fuerza Bruta (Óptimo)")
            nx.draw(G, pos, ax=ax1, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000)
            nx.draw_networkx_nodes(G, pos, nodelist=bf_cover, ax=ax1, node_color='green', node_size=1200)

            # Greedy
            ax2.set_title("Greedy (Aproximado)")
            nx.draw(G, pos, ax=ax2, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000)
            nx.draw_networkx_nodes(G, pos, nodelist=greedy_cover, ax=ax2, node_color='orange', node_size=1200)

            fig.tight_layout()

            # Convertir figura a base64 para mostrar en la app
            buf = io.BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            img_bytes = buf.getvalue()
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
            src = f'data:image/png;base64,{img_base64}'

            imagen_area.clear()
            ui.image(src).classes('w-full h-auto')
            resultado_label.text = "Visualización generada correctamente."

            # Botón para ver imagen en tamaño completo
            ui.button('Ver imagen en grande', on_click=lambda: mostrar_grafico(fig, "Vertex Cover")).props('color=primary')

        except Exception as e:
            resultado_label.text = f"Error: {e}"

    ui.button('MOSTRAR VERTEX COVER', on_click=calcular_y_mostrar).props('color=primary')