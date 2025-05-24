import flet as ft
from src.core.needleman_wunsch import NeedlemanWunschStepper

def construir_matriz_visual(matriz, seq1, seq2, paso_pos=None):
    encabezado = ft.Row([
        ft.Container(width=40),
        *[ft.Container(content=ft.Text(c), width=40, alignment=ft.alignment.center) for c in "-" + seq2]
    ])

    filas = []
    for i, fila in enumerate(matriz):
        letra = "-" if i == 0 else seq1[i - 1]
        fila_visual = ft.Row([
            ft.Container(content=ft.Text(letra), width=40, alignment=ft.alignment.center),
            *[
                ft.Container(
                    content=ft.Text(
                        str(val),
                        color=ft.Colors.BLACK if paso_pos == (i, j) else None,
                    ),
                    width=40,
                    height=40,
                    alignment=ft.alignment.center,
                    border=ft.border.all(1),
                    bgcolor=ft.Colors.YELLOW_200 if paso_pos == (i, j) else None,
                )
                for j, val in enumerate(fila)
            ]
        ])
        filas.append(fila_visual)

    return [encabezado] + filas

def main_view(page: ft.Page):
    page.title = "Alineamiento Global - Needleman-Wunsch"
    page.scroll = ft.ScrollMode.ALWAYS
    page.padding = 20

    seq1_input = ft.TextField(label="Secuencia 1", value="GATTACA", width=300)
    seq2_input = ft.TextField(label="Secuencia 2", value="GCATGCU", width=300)
    match_input = ft.TextField(label="Match", value="1", width=100)
    mismatch_input = ft.TextField(label="Mismatch", value="-1", width=100)
    gap_input = ft.TextField(label="Gap", value="-2", width=100)

    matriz_output = ft.Column()
    alineacion_output = ft.Text()
    stepper_ref = {"obj": None}

    def inicializar(e):
        s1 = seq1_input.value.upper()
        s2 = seq2_input.value.upper()
        match = int(match_input.value)
        mismatch = int(mismatch_input.value)
        gap = int(gap_input.value)

        stepper_ref["obj"] = NeedlemanWunschStepper(s1, s2, match, mismatch, gap)
        matriz_output.controls = construir_matriz_visual(stepper_ref["obj"].matriz, s1, s2, paso_pos=(0, 0))
        alineacion_output.value = "Listo para iniciar pasos o ejecutar completo."
        page.update()

    def siguiente(e):
        if not stepper_ref["obj"]:
            return
        result = stepper_ref["obj"].step()
        if result is None:
            alineacion_output.value = "Matriz completada. Puedes aplicar traceback."
        else:
            matriz, _, pos = result
            s1 = seq1_input.value.upper()
            s2 = seq2_input.value.upper()
            matriz_output.controls = construir_matriz_visual(matriz, s1, s2, paso_pos=pos)
        page.update()

    def ejecutar_completo(e):
        if not stepper_ref["obj"]:
            return
        stepper_ref["obj"].run_all()
        s1 = seq1_input.value.upper()
        s2 = seq2_input.value.upper()
        matriz = stepper_ref["obj"].matriz
        matriz_output.controls = construir_matriz_visual(matriz, s1, s2)
        alineacion_output.value = "Matriz completada."
        page.update()

    def ejecutar_traceback(e):
        if not stepper_ref["obj"]:
            return
        s1 = seq1_input.value.upper()
        s2 = seq2_input.value.upper()
        a1, a2 = stepper_ref["obj"].traceback()
        alineacion_output.value = f"Alineación óptima:\n{s1} → {a1}\n{s2} → {a2}"
        page.update()

    page.add(
        ft.Column([
            ft.Row([seq1_input, seq2_input]),
            ft.Row([match_input, mismatch_input, gap_input]),
            ft.Row([
                ft.ElevatedButton("Inicializar", on_click=inicializar),
                ft.ElevatedButton("Siguiente Paso", on_click=siguiente),
                ft.ElevatedButton("Ejecutar Todo", on_click=ejecutar_completo),
                ft.ElevatedButton("Traceback", on_click=ejecutar_traceback),
            ]),
            ft.Text("Matriz de alineamiento:", weight="bold", size=16),
            matriz_output,
            ft.Text("Resultado:", weight="bold", size=16),
            alineacion_output,
        ], spacing=20)
    )
