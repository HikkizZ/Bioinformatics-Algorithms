import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations


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


def calcular_vertex_cover_desde_entrada(nodos_str: str, aristas_str: str):
    """
    Recibe cadenas de texto con nodos separados por coma y aristas como lista de tuplas.
    Devuelve un gráfico matplotlib con el resultado del Vertex Cover.
    """
    try:
        nodos = [n.strip() for n in nodos_str.split(',')]
        aristas = eval(aristas_str)
        if not isinstance(aristas, list):
            raise ValueError("Las aristas deben ser una lista de tuplas.")

        G = nx.Graph()
        G.add_nodes_from(nodos)
        G.add_edges_from(aristas)

        bf_cover = brute_force_vertex_cover(G.copy())
        greedy_cover = greedy_vertex_cover(G.copy())

        pos = nx.spring_layout(G, seed=42)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # Aumenta altura
        ax1.set_title("Fuerza Bruta (Óptimo)")
        ax2.set_title("Greedy (Aproximado)")

        nx.draw(G, pos, ax=ax1, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000)
        nx.draw_networkx_nodes(G, pos, nodelist=bf_cover, ax=ax1, node_color='green', node_size=1200)

        nx.draw(G, pos, ax=ax2, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000)
        nx.draw_networkx_nodes(G, pos, nodelist=greedy_cover, ax=ax2, node_color='orange', node_size=1200)

        plt.tight_layout()
        return fig, bf_cover, greedy_cover

    except Exception as e:
        raise ValueError(f"Error al procesar los datos: {e}")