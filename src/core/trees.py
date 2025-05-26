import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage

def parse_matrix(text: str) -> np.ndarray:
    """
    Convierte texto crudo en matriz NumPy.
    Ejemplo de entrada: [[0, 2, 4], [2, 0, 5], [4, 5, 0]]
    """
    try:
        matrix = eval(text)
        matrix = np.array(matrix)

        # Validaciones
        if not isinstance(matrix, np.ndarray):
            raise ValueError("No es una matriz válida.")
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("La matriz debe ser cuadrada.")
        if not np.allclose(matrix, matrix.T):
            raise ValueError("La matriz debe ser simétrica.")
        if not np.all(np.diag(matrix) == 0):
            raise ValueError("La diagonal principal debe contener solo ceros.")

        return matrix
    except Exception as e:
        raise ValueError(f"Error al procesar la matriz: {e}")

def generar_arbol(matrix_text: str, metodo: str = 'average'):
    """
    Genera un árbol jerárquico (ultramétrico o aditivo) a partir de una matriz de distancias.
    método: 'average' → ultramétrico, 'single' → aditivo
    """
    matrix = parse_matrix(matrix_text)
    triu = matrix[np.triu_indices(len(matrix), 1)]
    linked = linkage(triu, method=metodo)

    # Crear grafo a partir de linkage
    G = nx.Graph()
    n = len(matrix)
    for i, (a, b, dist, _) in enumerate(linked):
        node_id = n + i
        G.add_edge(int(a), node_id, weight=round(dist, 2))
        G.add_edge(int(b), node_id, weight=round(dist, 2))

    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_edge_attributes(G, 'weight')

    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, ax=ax)
    ax.set_title(f"Árbol {'Ultramétrico' if metodo == 'average' else 'Aditivo'}")
    return fig