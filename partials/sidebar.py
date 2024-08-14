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
                    ),
                    ft.Text(value='Marcelo Porfirio',theme_style=ft.TextThemeStyle.BODY_LARGE,color=ft.colors.WHITE),
                    ft.Text(value='Desenvolvedor Fullstack',theme_style=ft.TextThemeStyle.BODY_MEDIUM,color=ft.colors.WHITE)
                
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            ),
            padding=ft.padding.symmetric(vertical=20,horizontal=40),
            alignment=ft.alignment.center,
        )
    
class SidebarContent(ft.UserControl):
    def build(self):
        location = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value='Residência:',theme_style=ft.TextThemeStyle.BODY_LARGE,color='white'),
                        ft.Text(value='Brasil',theme_style=ft.TextThemeStyle.BODY_MEDIUM,color='white'),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Cidade:',theme_style=ft.TextThemeStyle.BODY_LARGE,color='white'),
                        ft.Text(value='Canoas',theme_style=ft.TextThemeStyle.BODY_MEDIUM,color='white'),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Idade:',theme_style=ft.TextThemeStyle.BODY_LARGE,color='white'),
                        ft.Text(value='33',theme_style=ft.TextThemeStyle.BODY_MEDIUM,color='white'),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
            ]
        )
        languages = ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Stack(
                            controls=[
                                ft.PieChart(
                                    sections=[
                                        ft.PieChartSection(value=100,color=ft.colors.PRIMARY,radius=5),
                                        ft.PieChartSection(value=0,color=ft.colors.BLACK26,radius=5)
                                    ],
                                    sections_space=0,
                                    center_space_color=ft.colors.BLACK12,
                                    height=70
                                ),
                                ft.Container(
                                    content=ft.Text(value='100%',theme_style=ft.TextThemeStyle.BODY_LARGE,color='white'),
                                    alignment=ft.alignment.center,
                                    height=70,
                                )
                            ]
                        ),
                        ft.Text(value='Português',theme_style=ft.TextThemeStyle.BODY_LARGE,color='white')
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                )
            ]
        )
        skills = ft.Container()
        technologies = ft.Container()
        cv = ft.Container()
        

        return ft.Container(
            bgcolor=ft.colors.BLACK12,
            padding=ft.padding.all(20),
            content=ft.Column(
                controls=[
                    location,
                    ft.Divider(height=30),
                    languages,
                    ft.Divider(height=30),
                    skills,
                    ft.Divider(height=30),
                    technologies,
                    ft.Divider(height=30),
                    cv,
                ]
            )
        )
    
class SidebarFooter(ft.UserControl):
    def build(self):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=10),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(src='icons/001-instagram.png',height=15,color='white'),
                        url='https://www.instagram.com/marcelobrys/'
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/002-linkedin.png',height=15,color='white'),
                        url='https://www.linkedin.com/in/marcelo-porf%C3%ADrio-55a198161/'
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/003-github.png',height=15,color='white'),
                        url='https://github.com/MarceloPorfirio'
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/004-youtube.png',height=15,color='white'),
                        url='https://www.instagram.com/marcelobrys/'
                    ),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    


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
            bgcolor=ft.colors.ON_BACKGROUND
        )