import flet as ft
from typing import List


class Carousel(ft.Column):
    def __init__(self, controls: List[ft.Control], height: int = 250, **kwargs):
        super().__init__(**kwargs)
        self.items = controls
        self.current_index = 0
        self.total = len(controls)

        self.dots = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
            controls=[
                ft.Container(
                    width=24 if i == 0 else 8,
                    height=8,
                    bgcolor=ft.Colors.PRIMARY if i == 0 else ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY),
                    border_radius=4,
                    animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
                )
                for i in range(self.total)
            ],
        )

        self.carousel = ft.Row(
            height=height,
            scroll=ft.ScrollMode.HIDDEN,
            controls=controls,
        )

        self.controls = [
            self.carousel,
            ft.Container(height=10),
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.dots,
                    ft.Row(
                        controls=[
                            self._nav_button(ft.Icons.KEYBOARD_ARROW_LEFT, self.move_backward),
                            self._nav_button(ft.Icons.KEYBOARD_ARROW_RIGHT, self.move_forward),
                        ],
                        spacing=8,
                    ),
                ],
            ),
        ]

    def _nav_button(self, icon, on_click):
        return ft.Container(
            content=ft.IconButton(
                icon=icon,
                icon_color=ft.Colors.WHITE,
                icon_size=20,
                on_click=on_click,
            ),
            bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY),
            border_radius=25,
            border=ft.border.all(1, ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
            on_hover=self._nav_hover,
        )

    def _nav_hover(self, e):
        if e.data == "true":
            e.control.bgcolor = ft.Colors.with_opacity(0.4, ft.Colors.PRIMARY)
        else:
            e.control.bgcolor = ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)
        e.control.update()

    def _update_dots(self):
        for i, dot in enumerate(self.dots.controls):
            if i == self.current_index:
                dot.bgcolor = ft.Colors.PRIMARY
                dot.width = 24
            else:
                dot.bgcolor = ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY)
                dot.width = 8
        self.dots.update()

    def move_backward(self, e):
        self.current_index = max(0, self.current_index - 1)
        self.carousel.scroll_to(delta=-450, duration=400, curve=ft.AnimationCurve.EASE_IN_OUT)
        self._update_dots()
        self.carousel.update()

    def move_forward(self, e):
        self.current_index = min(self.total - 1, self.current_index + 1)
        self.carousel.scroll_to(delta=450, duration=400, curve=ft.AnimationCurve.EASE_IN_OUT)
        self._update_dots()
        self.carousel.update()
