from nicegui import ui
from src.core.permutations import generate_permutations, generate_itertools_permutations

def render_permutations_tab():
    ui.label('Comparación de Algoritmos de Permutaciones').classes('text-2xl font-bold mb-6')

    entrada = ui.input('Ingresa una secuencia (máximo 6 caracteres)').props('type=text').classes('w-1/2')
    resultado = ui.markdown('').classes('mt-4 text-sm')

    boton_limpiar = ui.button('LIMPIAR BÚSQUEDA', on_click=lambda: None).props('color=secondary').classes('mt-2')
    boton_limpiar.set_visibility(False)  # Ocultar inicialmente

    def comparar():
        secuencia = entrada.value.strip()

        if len(secuencia) > 6:
            resultado.set_content('❌ La secuencia debe tener un máximo de 6 caracteres.')
            return

        tiempo_back, cantidad_back = generate_permutations(secuencia)
        tiempo_iter, cantidad_iter = generate_itertools_permutations(secuencia)

        comentario = '### 🧠 Comentarios sobre los resultados\n'

        if tiempo_back > tiempo_iter:
            comentario += (
                "**Itertools** es más rápido, ya que está optimizado en C y no verifica duplicados,\n"
                "por lo que genera todas las permutaciones posibles de manera directa.\n\n"
                "**Backtracking**, en cambio, realiza verificaciones adicionales para evitar duplicados,\n"
                "lo que consume más tiempo.\n\n"
            )
        elif tiempo_back < tiempo_iter:
            comentario += (
                "**Backtracking** fue más rápido, probablemente porque la secuencia contiene duplicados,\n"
                "y el uso de `set()` ayudó a reducir la cantidad de permutaciones generadas.\n\n"
                "**Itertools** genera todas las combinaciones, incluidos los duplicados.\n\n"
            )
        else:
            comentario += (
                "Ambos enfoques tuvieron tiempos similares, lo que podría deberse\n"
                "al tamaño pequeño de la secuencia o a optimizaciones internas.\n\n"
            )

        comentario += (
            "### 🧩 Comentario general sobre ambos algoritmos\n"
            "- `itertools` es ideal para simplicidad y velocidad en listas pequeñas sin duplicados.\n"
            "- `backtracking` es útil cuando se requiere evitar duplicados y mayor control.\n\n"
            "En general, si no te importan los duplicados, itertools es preferible. "
            "Si necesitas filtrarlos, usa backtracking.\n"
        )

        resultado.set_content(
            f'### 📊 Comparación de Algoritmos\n'
            f'- Backtracking: **{cantidad_back}** permutaciones en **{tiempo_back:.4f} ms**\n'
            f'- Itertools: **{cantidad_iter}** permutaciones en **{tiempo_iter:.4f} ms**\n\n'
            f'{comentario}'
        )

        boton_limpiar.set_visibility(True)  # Mostrar botón

    def limpiar():
        entrada.value = ''
        resultado.set_content('')
        boton_limpiar.set_visibility(False)

    boton_limpiar.on_click(limpiar)

    ui.button('COMPARAR ALGORITMOS', on_click=comparar).props('color=primary').classes('mt-4')

    # Ejemplo
    ui.label('Ejemplo de uso:').classes('text-lg font-bold mt-6')
    with ui.row():
        ui.label('Secuencia:').classes('font-semibold')
        ui.label('1123').classes('italic')
    ui.label('Nota: Se recomienda ingresar letras o dígitos sin espacios.').classes('mt-2 italic')