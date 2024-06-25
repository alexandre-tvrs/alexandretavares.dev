import flet as ft
# import webbrowser
from projects_lists import get_projects


def main(page: ft.Page):
    page.title = "Alexandre Tavares"
    page.description = "Professional profile of Alexandre Tavares"
    page.theme_mode = ft.ThemeMode.DARK

    def ChatTCC(e):
        open_url("https://github.com/alexandre-tvrs/backend-tcc")
        
    def WrathOfElements(e):
        open_url("https://github.com/alexandre-tvrs/wrath-of-elements")
        
    def TargonApp(e):
        open_url("https://github.com/alexandre-tvrs/target-generator")
        
    def ProjectENV(e):
        open_url("https://github.com/alexandre-tvrs/-api-project.env")
        
    def KotaroBOT(e):
        open_url("https://github.com/alexandre-tvrs/kotaro-bot")
        
    def LoLResultPrevision(e):
        open_url("https://google.com")
    
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
    
    projects = []
    
    for project in get_projects():
        projects.append(
            ft.CupertinoListTile(
                title = ft.Text(project.name, size='24', weight='BOLD'),
                subtitle = ft.Text(project.description, size='18'),
                leading = ft.Image("https://cdn-icons-png.flaticon.com/512/25/25231.png", height=35, width=35),
                additional_info = ft.Text("GitHub", size='18'),
                trailing = ft.Icon(ft.icons.ARROW_RIGHT),
                on_click = eval(project.name),
            )
        )
        
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
    
    projects_page = ft.Row(
        [
            ft.Column(
                [
                    project for project in projects
                ],
            ),    
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        wrap=True,
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
        [
          ft.Column(
            [
                ft.Text("Contact", size='36', weight='BOLD'),
                ft.Text("Email: alexandre.j.tavares.jr@gmail.com", size='24'),
                ft.Text("Phone: +55 11 91178-7430", size='24'),
                ft.Row(
                    [
                        ft.CupertinoButton(
                            content=ft.Image("https://seeklogo.com/images/W/whatsapp-logo-0DBD89C8E2-seeklogo.com.png", height=35, width=35),
                            on_click=lambda e: open_url("https://wa.me/5511911787430"),
                            ),
                        ft.CupertinoButton(
                            content=ft.Image("https://static.vecteezy.com/system/resources/previews/006/892/625/original/discord-logo-icon-editorial-free-vector.jpg", height=35, width=35),
                            on_click=lambda e: open_url("https://discord.gg/XszRx6mBzE"),
                        ),
                    ],
                )
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