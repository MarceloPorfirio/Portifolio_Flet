import flet as ft
from typing import List

class Carousel(ft.UserControl):
    def __init__(self,controls: List[ft.Control], height: int = 250, **kwargs):
        super().__init__(**kwargs)
        self.carousel = ft.Row(
            height=height,
            scroll=ft.ScrollMode.HIDDEN,
            controls=controls


        )
    def build(self):
        return ft.Column(
            controls=[
                self.carousel
            ]
        )