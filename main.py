# Importação de bibliotecas
import flet as ft


def main(page: ft.Page):
    page.title = "Alexandre Tavares"
    page.description = "Professional profile of Alexandre Tavares"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    grid = ft.Container()
    
    footer = ft.Container()
    
    layout = ft.Column(
        expand=True,
        controls=[
            grid,
            footer
        ]
    )
    
    page.add(layout)
    
    page.update()


if __name__ == "__main__":
    ft.app(main, assets_dir="assets")