import flet as ft

class Skill(ft.UserControl): # classe mãe,utilizada para mudar as propriedades das demais classes
    def __init__(self, title: str, value: float):
        super().__init__()
        self.title = title
        self.value = value

class SkillRing(Skill): # Herda as propriedades da classe mae
    def build(self):
        self.expand = True # adiciona permitindo que o stack principal se expanda
        return ft.Column(
                    controls=[
                        ft.Stack(
                            controls=[
                                ft.PieChart(
                                    sections=[
                                        ft.PieChartSection(value=self.value,color=ft.colors.PRIMARY,radius=5),
                                        ft.PieChartSection(value=1 - self.value,color=ft.colors.BLACK26,radius=5)
                                    ],
                                    sections_space=0,
                                    center_space_color=ft.colors.BLACK12,
                                    height=70
                                ),
                                ft.Container(
                                    content=ft.Text(value=f'{self.value:.0%}',theme_style=ft.TextThemeStyle.BODY_LARGE,color='white'),
                                    alignment=ft.alignment.center,
                                    height=70,
                                )
                            ]
                        ),
                        ft.Text(value=self.title,theme_style=ft.TextThemeStyle.BODY_LARGE,color='white')
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    # expand=True,
                )

class SkillProgressbar(Skill):
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                controls=[
                    ft.Text(value=self.title,theme_style=ft.TextThemeStyle.BODY_LARGE,color='white'),
                    ft.Text(value=f'{self.value:.0%}',theme_style=ft.TextThemeStyle.BODY_MEDIUM,color='white')
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.ProgressBar(value=self.value, color=ft.colors.PRIMARY,bgcolor=ft.colors.BLACK26),
            ft.Divider(height=10,color=ft.colors.BLACK12)
                ]
            )
        )