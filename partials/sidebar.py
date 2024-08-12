import flet as ft

class SidebarHeader(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Badge(
                        content=ft.Image(
                            src='images/face-1.jpg',
                            border_radius=ft.border_radius.all(100),
                            width=100,
                        ),
                        alignment=ft.alignment.bottom_right,
                        bgcolor=ft.colors.PRIMARY,
                        small_size=20,
                    )
                ]
            )
        )
    
class SidebarContent(ft.UserControl):
    def build(self):
        return ft.Container()
    
class SidebarFooter(ft.UserControl):
    def build(self):
        return ft.Container()
    


class Sidebar(ft.UserControl):
    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    SidebarHeader(),
                    SidebarContent(),
                    SidebarFooter(),

                ]
            ),
            bgcolor=ft.colors.BACKGROUND
        )