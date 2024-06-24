import flet as ft
# import webbrowser
from projects_lists import get_projects


def main(page: ft.Page):
    page.title = "Alexandre Tavares"
    page.description = "Professional profile of Alexandre Tavares"
    page.theme_mode = ft.ThemeMode.DARK
    
    def open_url(url: str):
        page.launch_url(url)
        
    def go_to_about_page():
        page.clean()
        page.add(intro_page)
        page.add(page_changer)
        page.update()
        
    def go_to_projects_page():
        page.clean()
        page.add(projects_page)
        page.add(page_changer)
        page.update()
        
    def go_to_experience_page():
        page.clean()
        page.add(experience_page)
        page.add(page_changer)
        page.update()
        
    def go_to_contact_page():
        page.clean()
        page.add(contact_page)
        page.add(page_changer)
        page.update()
        
    def on_change(e):
        value = int(e.data[2])
        if value == 1:
            go_to_about_page()
        elif value == 2:
            go_to_projects_page()
        elif value == 3:
            go_to_experience_page()
        elif value == 4:
            go_to_contact_page()
    
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
    
    projects = [
        ft.CupertinoButton(
            content=ft.Card(
                content=ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Image("project_wallpaper.jpg", height=50, width=200, fit='COVER'),
                                ft.Text(f"{project.name}", size='18', weight='BOLD', width=200, height=30,),
                                ft.Text(f"{project.description}", size='14', max_lines=3, width=200, height=80),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            on_click=lambda e: open_url(project.git_url),
        ) for project in get_projects()
    ]
        
    intro_page = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("Alexandre Tavares", size='36', weight='BOLD'),
                    ft.Text("Software Engineer | Machine Learning Engineer", size='24'),
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
    
    projects_page = ft.GridView(
        controls=projects,
        expand=True,
        runs_count=5,
        child_aspect_ratio=1.25,
    )
    
    experience_page = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("Experience", size='36', weight='BOLD'),
                    ft.Text("Software Developer | Software Engineer | Machine Learning Engineer", size='24'),
                    ft.Text("2023 - Present", size='18', weight='BOLD'),
                    ft.Text("Software Engineer at KONIA", size='18'),
                    ft.Text("2022 - 2023", size='18', weight='BOLD'),
                    ft.Text("DevOps Consultant at KONIA", size='18'),
                    ft.Text("2021 - 2022", size='18', weight='BOLD'),
                    ft.Text("SAM Consultant at SoftwareONE", size='18'),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ), 
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    contact_page = ft.Row(
        expand=True,
    )
    
    page_changer = ft.Row(
        [
          ft.Column(
              [
                ft.SegmentedButton(
                    selected={1},
                    allow_multiple_selection=False,
                    segments=[
                        ft.Segment(
                            value=1,
                            label=ft.Text("About", size='18', weight='BOLD'),
                            icon=ft.Icon(ft.icons.PERSON),
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
                    on_change=on_change,
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