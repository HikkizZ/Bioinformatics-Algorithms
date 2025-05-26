from nicegui import ui
from src.core.search import buscar_secuencia_objetivo

def render_search_tab():
    ui.label("Buscar Secuencia en Permutaciones").classes('text-2xl font-bold mb-6')

    entrada_inicial = ui.input(label='Secuencia Inicial (ej: 1,2,3)').classes('w-full')
    entrada_objetivo = ui.input(label='Secuencia Objetivo (ej: 3,2,1)').classes('w-full')

    ui.markdown(
        "**_Ejemplo de uso:_**  \n"
        "**Secuencia inicial:** `1, 2, 3, 4`  \n"
        "**Secuencia objetivo:** `4, 3, 2, 1`  \n"
        "_Nota: Máximo 6 números. Usa comas para separar._"
    ).classes('text-sm italic text-gray-300 mt-4')

    # Contenedores
    botones = ui.row().classes('mt-4 gap-4')
    salida = ui.column().classes('mt-6')
    contenedor_pasos = ui.column().classes('mt-4')

    # Botones (referencias)
    def ejecutar_busqueda():
        salida.clear()
        contenedor_pasos.clear()

        try:
            lista_inicial = [int(x.strip()) for x in entrada_inicial.value.split(",")]
            lista_objetivo = [int(x.strip()) for x in entrada_objetivo.value.split(",")]
        except ValueError:
            with salida:
                ui.label("❌ Error: Ingresa solo números separados por coma.").classes('text-red-500')
            return

        datos = buscar_secuencia_objetivo(lista_inicial, lista_objetivo)
        if "error" in datos:
            with salida:
                ui.label(f"❌ {datos['error']}").classes('text-red-500')
            return

        # 🔍 Resultado
        with salida:
            ui.markdown("### 🔍 Búsqueda de Secuencia").classes('text-2xl text-white font-bold')
            ui.markdown(f"- **Secuencia Inicial:** `{lista_inicial}`\n- **Secuencia Objetivo:** `{lista_objetivo}`").classes('text-white')

            if datos["permutacion"]:
                ui.label(f"✅ Secuencia encontrada en {datos['pasos']} pasos: {datos['permutacion']}").classes('text-green-500 font-bold')
            else:
                ui.label("⚠️ La secuencia no fue encontrada.").classes('text-yellow-500 font-bold')

        # 📄 Registro de Pasos
        with contenedor_pasos:
            ui.markdown("### 📄 Registro de Pasos").classes('text-white text-xl font-bold')
            with ui.row().classes('max-h-[400px] overflow-y-auto flex-wrap gap-2'):
                for paso in datos["log_pasos"]:
                    ui.label(paso).classes('bg-gray-100 text-black p-2 rounded shadow-sm')

    with botones:
        ui.button('BUSCAR SECUENCIA', on_click=ejecutar_busqueda).props('color=primary')

    # Mostrar salida abajo de los botones
    salida
    contenedor_pasos