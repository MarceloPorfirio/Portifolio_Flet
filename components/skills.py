import flet as ft

class Skill: # classe mãe,utilizada para mudar as propriedades das demais classes
    def __init__(self, title: str, value: float):
        self.title = title
        self.value = value

class SkillRing(Skill, ft.Column): # Herda as propriedades da classe mae
    def __init__(self, title: str, value: float, **kwargs):
        Skill.__init__(self, title, value)
        ft.Column.__init__(self, **kwargs)
        self.expand = True # adiciona permitindo que o stack principal se expanda
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [
            ft.Stack(
                controls=[
                    ft.PieChart(
                        sections=[
                            ft.PieChartSection(value=self.value,color=ft.Colors.PRIMARY,radius=5),
                            ft.PieChartSection(value=1 - self.value,color=ft.Colors.BLACK26,radius=5)
                        ],
                        sections_space=0,
                        center_space_color=ft.Colors.BLACK12,
                        height=70
                    ),
                    ft.Container(
                        content=ft.Text(value=f'{self.value:.0%}',theme_style=ft.TextThemeStyle.BODY_LARGE),
                        alignment=ft.alignment.center,
                        height=70,
                    )
                ]
            ),
            ft.Text(value=self.title,theme_style=ft.TextThemeStyle.BODY_LARGE)
        ]

class SkillProgressbar(Skill, ft.Container):
    def __init__(self, title: str, value: float, **kwargs):
        Skill.__init__(self, title, value)
        ft.Container.__init__(self, **kwargs)
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value=self.title,theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value=f'{self.value:.0%}',theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.ProgressBar(value=self.value, color=ft.Colors.PRIMARY,bgcolor=ft.Colors.BLACK26),
                ft.Divider(height=10,color=ft.Colors.BLACK12)
            ]
        )
