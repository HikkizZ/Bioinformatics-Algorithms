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

def calcular_vertex_cover_desde_input(nodos_texto: str, aristas_texto: str):
    """
    Recibe el texto de nodos y aristas ingresados por el usuario.
    Retorna una figura matplotlib con los grafos dibujados.
    """
    try:
        nodos = [n.strip() for n in nodos_texto.split(",")]
        aristas = eval(aristas_texto)  # 👈 Asegúrate de usar comillas en los nodos: [('A', 'B'), ...]
    except Exception as e:
        raise ValueError(f"Error al procesar la entrada: {e}")

    G = nx.Graph()
    G.add_nodes_from(nodos)
    G.add_edges_from(aristas)

    bf_cover = brute_force_vertex_cover(G.copy())
    greedy_cover = greedy_vertex_cover(G.copy())

    pos = nx.spring_layout(G, seed=42)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.set_title("Fuerza Bruta (Óptimo)")
    ax2.set_title("Greedy (Aproximado)")

    nx.draw(G, pos, ax=ax1, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000)
    nx.draw_networkx_nodes(G, pos, nodelist=bf_cover, node_color='green', ax=ax1, node_size=1200)

    nx.draw(G, pos, ax=ax2, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000)
    nx.draw_networkx_nodes(G, pos, nodelist=greedy_cover, node_color='orange', ax=ax2, node_size=1200)

    fig.tight_layout()
    return fig