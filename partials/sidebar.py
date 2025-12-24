import flet as ft
from components.skills import SkillRing,SkillProgressbar

class SidebarHeader(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Container(
                        content=ft.Image(
                            src='images/face-1.jpg',
                            border_radius=ft.border_radius.all(100),
                            width=110,
                            height=110,
                            fit=ft.ImageFit.COVER,
                        ),
                        border=ft.border.all(4, ft.Colors.PRIMARY),
                        border_radius=100,
                        shadow=ft.BoxShadow(
                            spread_radius=3,
                            blur_radius=15,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.PRIMARY),
                        ),
                        animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
                    ),
                    badge=ft.Badge(
                        bgcolor=ft.Colors.PRIMARY,
                        small_size=22,
                    ),
                    alignment=ft.alignment.center,
                ),
                ft.Container(height=15),
                ft.Text(
                    value='Marcelo Porfirio',
                    theme_style=ft.TextThemeStyle.BODY_LARGE,
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(
                    content=ft.Text(
                        value='Desenvolvedor Fullstack',
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                        size=14,
                    ),
                    padding=ft.padding.symmetric(horizontal=15, vertical=5),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                    border_radius=15,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
        )
        self.padding = ft.padding.symmetric(vertical=30,horizontal=40)
        self.alignment = ft.alignment.center

class SidebarContent(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand = True

        location = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value='Residência:',theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='Brasil',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Cidade:',theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='Canoas',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Idade:',theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='33',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
            ]
        )
        languages = ft.Row(
            controls=[
                SkillRing(title='Português',value=1),
                SkillRing(title='Inglês',value=1),
                SkillRing(title='Espanhol',value=0.5)
            ]
        )
        skills = ft.Column(
            controls=[
                SkillProgressbar(title='HTML',value=1),
                SkillProgressbar(title='CSS',value=1),
                SkillProgressbar(title='PYTHON',value=1),
                SkillProgressbar(title='SQL',value=0.9),
                SkillProgressbar(title='JS',value=0.7),
                SkillProgressbar(title='PHP',value=0.6),

            ]

        )
        technologies = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.CHECK,color=ft.Colors.PRIMARY),
                            ft.Text(value='Flet',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ]),
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.CHECK,color=ft.Colors.PRIMARY),
                            ft.Text(value='Tkinter',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.CHECK,color=ft.Colors.PRIMARY),
                            ft.Text(value='Flask',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.CHECK,color=ft.Colors.PRIMARY),
                            ft.Text(value='Django',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ]
                    )
                    ]),
                     ft.Column(
                        controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.CHECK,color=ft.Colors.PRIMARY),
                            ft.Text(value='Pandas',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ]),
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.CHECK,color=ft.Colors.PRIMARY),
                            ft.Text(value='Streamlit',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.CHECK,color=ft.Colors.PRIMARY),
                            ft.Text(value='React',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ]
                    ),ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.CHECK,color=ft.Colors.PRIMARY),
                            ft.Text(value='FireBase',theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ]
                    )


                    ]),

            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            )

        )
        cv = ft.ElevatedButton(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.DOWNLOAD, color=ft.Colors.BLACK, size=20),
                    ft.Text(value='DOWNLOAD CV', color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD, size=14),
                ],
                tight=True,
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=ft.Colors.PRIMARY,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=20),
                padding=ft.padding.symmetric(horizontal=25, vertical=15),
                shadow_color=ft.Colors.PRIMARY,
                elevation=5,
            ),
            url='https://drive.google.com/uc?export=download&id=13kLnuJbBabsRpQsqHjtdOruODf7zPFVO'
        )

        self.bgcolor = ft.Colors.with_opacity(0.3, ft.Colors.BLACK12)
        self.padding = ft.padding.all(20)
        self.border_radius = 15
        self.content = ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                location,
                ft.Divider(height=30, color=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
                languages,
                ft.Divider(height=30, color=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
                skills,
                ft.Divider(height=30, color=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
                technologies,
                ft.Divider(height=30, color=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
                cv,
            ]
        )

class SidebarFooter(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = ft.padding.symmetric(vertical=20)
        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.IconButton(
                        content=ft.Image(src='icons/001-instagram.png',height=18),
                        url='https://www.instagram.com/marcelobrys/',
                    ),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                    border_radius=10,
                    padding=5,
                ),
                ft.Container(
                    content=ft.IconButton(
                        content=ft.Image(src='icons/002-linkedin.png',height=18),
                        url='https://www.linkedin.com/in/marcelo-porf%C3%ADrio-55a198161/',
                    ),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                    border_radius=10,
                    padding=5,
                ),
                ft.Container(
                    content=ft.IconButton(
                        content=ft.Image(src='icons/003-github.png',height=18),
                        url='https://github.com/MarceloPorfirio',
                    ),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                    border_radius=10,
                    padding=5,
                ),
                ft.Container(
                    content=ft.IconButton(
                        content=ft.Image(src='icons/004-youtube.png',height=18),
                        url='https://www.instagram.com/marcelobrys/',
                    ),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                    border_radius=10,
                    padding=5,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )



class Sidebar(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand = True
        self.content = ft.Column(
            controls=[
                SidebarHeader(),
                SidebarContent(),
                SidebarFooter(),

            ]
        )
        self.bgcolor = ft.Colors.ON_SURFACE
