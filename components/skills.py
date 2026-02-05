import flet as ft

class Skill:
    def __init__(self, title: str, value: float):
        self.title = title
        self.value = value

class SkillRing(Skill, ft.Column):
    def __init__(self, title: str, value: float, **kwargs):
        Skill.__init__(self, title, value)
        ft.Column.__init__(self, **kwargs)
        self.expand = True
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Stack(
                controls=[
                    ft.PieChart(
                        sections=[
                            ft.PieChartSection(value=self.value, color=ft.Colors.PRIMARY, radius=5),
                            ft.PieChartSection(value=1 - self.value, color=ft.Colors.BLACK26, radius=5)
                        ],
                        sections_space=0,
                        center_space_color=ft.Colors.with_opacity(0.05, ft.Colors.PRIMARY),
                        height=70
                    ),
                    ft.Container(
                        content=ft.Text(value=f'{self.value:.0%}', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        alignment=ft.alignment.center,
                        height=70,
                    )
                ]
            ),
            ft.Text(value=self.title, theme_style=ft.TextThemeStyle.BODY_LARGE)
        ]

class SkillProgressbar(Skill, ft.Container):
    def __init__(self, title: str, value: float, **kwargs):
        Skill.__init__(self, title, value)
        ft.Container.__init__(self, **kwargs)
        self.content = ft.Column(
            spacing=6,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value=self.title, theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value=f'{self.value:.0%}', theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Container(
                    content=ft.ProgressBar(
                        value=self.value,
                        color=ft.Colors.PRIMARY,
                        bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                    ),
                    border_radius=4,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    height=8,
                ),
            ]
        )
