import flet as ft
from partials.sidebar import Sidebar

class App:
    def __init__(self, page:ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.BLACK
        self.main()

    def main(self):
        self.sidebar = Sidebar()
        self.content = ft.Container()

        layout = ft.ResponsiveRow(
            columns=12,
            controls=[
                self.sidebar,
                self.content,
            ],
            expand=True
        )
        
        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')