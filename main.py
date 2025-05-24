import flet as ft
from src.ui.main_view import main_view

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    main_view(page)

if __name__ == "__main__":
    ft.app(target=main)
