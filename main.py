from nicegui import ui
from src.ui.main_window import render_main_window

render_main_window()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Bioinformatics Algorithms UBB', dark=True)
