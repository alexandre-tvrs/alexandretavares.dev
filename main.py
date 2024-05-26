import flet as ft
import webbrowser


def main(page: ft.Page):
    page.title = "Alexandre Tavares"
    page.description = "Professional profile of Alexandre Tavares"
    page.theme_mode = ft.ThemeMode.DARK
    
    def open_url(url: str):
        webbrowser.open(url)
    
    images = [
        ft.CupertinoButton(
            content=ft.Image("https://cdn-icons-png.flaticon.com/512/25/25231.png", height=35, width=35),
            on_click=lambda e: open_url("https://github.com/alexandre-tvrs"),
        ),
        ft.CupertinoButton(
            content=ft.Image("https://cdn-icons-png.flaticon.com/512/766/766173.png", height=35, width=35),
            on_click=lambda e: open_url("https://docs.google.com/document/d/17xS8tuKMtReBqdBXrNqGlvLXoyFuKTILcWmGb4BL4Xs/edit?usp=sharing"),
        ),
        ft.CupertinoButton(
            content=ft.Image("https://cdn-icons-png.flaticon.com/512/61/61109.png", height=35, width=35),
            on_click=lambda e: open_url("https://www.linkedin.com/in/dev-alexandre-tavares/"),
        ),
    ]
        
    intro_page = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("Alexandre Tavares", size='36', weight='BOLD'),
                    ft.Text("Software Engineer | Machine Learning Engineer", size='24',),
                    ft.Row(
                        [
                            image for image in images
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    page_changer = ft.Row(
        [
          ft.Column(
              [
                ft.SegmentedButton(
                    selected={1,},
                    allow_multiple_selection=False,
                    segments=[
                        ft.Segment(
                            value=1,
                            label=ft.Text("About", size='18', weight='BOLD'),
                            icon=ft.Icon(ft.icons.PERSON)
                        ),
                        ft.Segment(
                            value=2,
                            label=ft.Text("Projects", size='18', weight='BOLD'),
                            icon=ft.Icon(ft.icons.PERSON)
                        ),
                        ft.Segment(
                            value=3,
                            label=ft.Text("Experience", size='18', weight='BOLD'),
                            icon=ft.Icon(ft.icons.PERSON)
                        ),
                        ft.Segment(
                            value=4,
                            label=ft.Text("Contact", size='18', weight='BOLD'),
                            icon=ft.Icon(ft.icons.PERSON)
                        ),
                    ],
                ),
              ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          )  
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
        
    
    page.add(intro_page)
    page.add(page_changer)
    
    page.update()


ft.app(main, assets_dir="assets")