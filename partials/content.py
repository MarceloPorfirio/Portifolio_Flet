import flet as ft

class MainContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand=True

    def build(self):
        banner = ft.Container(
            content=ft.ResponsiveRow(
                columns=12,
                vertical_alignment=ft.CrossAxisAlignment.END,
                controls=[
                    ft.Container(
                        padding=ft.padding.all(50),
                        content=ft.Column(
                            controls=[
                                
                            ]
                        )
                    )
                ]
            )

        )
        experience = ft.Container()
        projects = ft.Container()
        prices = ft.Container()
        testimonials = ft.Container()
        logos = ft.Container()
        footer = ft.Container()


        return ft.Container(
            content=ft.Column(
                controls=[
                    banner,
                    experience,
                    projects,
                    prices,
                    testimonials,
                    logos,
                    footer
                ]
            ),
            bgcolor=ft.colors.BACKGROUND,
            padding=ft.padding.all(30)
        )