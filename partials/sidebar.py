import flet as ft
import os
from components.skills import SkillRing, SkillProgressbar
from components.styles import sidebar_section_label


class SidebarHeader(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.photo_container = ft.Container(
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
                spread_radius=5,
                blur_radius=25,
                color=ft.Colors.with_opacity(0.4, ft.Colors.PRIMARY),
            ),
            animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            on_hover=self._on_photo_hover,
        )

        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=self.photo_container,
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
        self.padding = ft.padding.symmetric(vertical=30, horizontal=40)
        self.alignment = ft.alignment.center

    def _on_photo_hover(self, e):
        if e.data == "true":
            self.photo_container.shadow = ft.BoxShadow(
                spread_radius=8, blur_radius=35,
                color=ft.Colors.with_opacity(0.6, ft.Colors.PRIMARY),
            )
            self.photo_container.scale = 1.05
        else:
            self.photo_container.shadow = ft.BoxShadow(
                spread_radius=5, blur_radius=25,
                color=ft.Colors.with_opacity(0.4, ft.Colors.PRIMARY),
            )
            self.photo_container.scale = 1.0
        self.photo_container.update()


class SidebarContent(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand = True

        location = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value='Residência:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='Brasil', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Cidade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='Canoas', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Idade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='33', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
            ]
        )

        languages = ft.Row(
            controls=[
                SkillRing(title='Português', value=1),
                SkillRing(title='Inglês', value=1),
                SkillRing(title='Espanhol', value=0.5)
            ]
        )

        skills = ft.Column(
            controls=[
                SkillProgressbar(title='PYTHON', value=1),
                SkillProgressbar(title='NOSQL', value=0.8),
                SkillProgressbar(title='SQL', value=0.9),
                SkillProgressbar(title='JS', value=0.7),
                SkillProgressbar(title='FLUTTER', value=0.7),
                SkillProgressbar(title='PHP', value=0.6),
            ]
        )

        technologies = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Row(controls=[
                                ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.PRIMARY),
                                ft.Text(value='Flet', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                            ]),
                            ft.Row(controls=[
                                ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.PRIMARY),
                                ft.Text(value='Tkinter', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                            ]),
                            ft.Row(controls=[
                                ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.PRIMARY),
                                ft.Text(value='Flask', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                            ]),
                            ft.Row(controls=[
                                ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.PRIMARY),
                                ft.Text(value='Django', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                            ]),
                        ]
                    ),
                    ft.Column(
                        controls=[
                            ft.Row(controls=[
                                ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.PRIMARY),
                                ft.Text(value='Pandas', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                            ]),
                            ft.Row(controls=[
                                ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.PRIMARY),
                                ft.Text(value='Streamlit', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                            ]),
                            ft.Row(controls=[
                                ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.PRIMARY),
                                ft.Text(value='React', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                            ]),
                            ft.Row(controls=[
                                ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.PRIMARY),
                                ft.Text(value='FireBase', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                            ]),
                        ]
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            )
        )

        cv = ft.Container(
            content=ft.ElevatedButton(
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
                    shape=ft.RoundedRectangleBorder(radius=25),
                    padding=ft.padding.symmetric(horizontal=30, vertical=18),
                    shadow_color=ft.Colors.PRIMARY,
                    elevation=8,
                ),
                on_click=self._open_cv
            ),
            alignment=ft.alignment.center,
            animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
            on_hover=self._cv_hover,
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY),
            ),
        )

        self.bgcolor = ft.Colors.with_opacity(0.3, ft.Colors.BLACK12)
        self.padding = ft.padding.all(20)
        self.border_radius = 15
        self.content = ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                sidebar_section_label("Localização"),
                location,
                ft.Divider(height=30, color=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
                sidebar_section_label("Idiomas"),
                languages,
                ft.Divider(height=30, color=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
                sidebar_section_label("Habilidades"),
                skills,
                ft.Divider(height=30, color=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
                sidebar_section_label("Tecnologias"),
                technologies,
                ft.Divider(height=30, color=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
                cv,
            ]
        )

    def _open_cv(self, e):
        pdf_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'assets', 'Marcelo_Curriculo.pdf'
        )
        os.startfile(pdf_path)

    def _cv_hover(self, e):
        if e.data == "true":
            e.control.scale = 1.05
        else:
            e.control.scale = 1.0
        e.control.update()


class SidebarFooter(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = ft.padding.symmetric(vertical=20)

        self.content = ft.Row(
            controls=[
                self._social_icon('icons/001-instagram.png', 'https://www.instagram.com/marcelobrys/'),
                self._social_icon('icons/002-linkedin.png', 'https://www.linkedin.com/in/marcelo-porf%C3%ADrio-55a198161/'),
                self._social_icon('icons/003-github.png', 'https://github.com/MarceloPorfirio'),
                self._social_icon('icons/004-youtube.png', 'https://www.instagram.com/marcelobrys/'),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )

    def _social_icon(self, image_src: str, url: str) -> ft.Container:
        return ft.Container(
            content=ft.IconButton(
                content=ft.Image(src=image_src, height=18),
                url=url,
            ),
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
            border_radius=10,
            padding=5,
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
            animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
            on_hover=self._icon_hover,
        )

    def _icon_hover(self, e):
        if e.data == "true":
            e.control.bgcolor = ft.Colors.with_opacity(0.25, ft.Colors.PRIMARY)
            e.control.scale = 1.15
            e.control.shadow = ft.BoxShadow(
                spread_radius=2, blur_radius=12,
                color=ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY),
            )
        else:
            e.control.bgcolor = ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY)
            e.control.scale = 1.0
            e.control.shadow = None
        e.control.update()


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
        self.gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[
                ft.Colors.with_opacity(0.95, ft.Colors.ON_SURFACE),
                ft.Colors.with_opacity(0.85, ft.Colors.ON_SURFACE),
                ft.Colors.with_opacity(0.7, ft.Colors.ON_SURFACE),
            ],
            stops=[0.0, 0.5, 1.0],
        )
        self.border = ft.border.only(
            right=ft.BorderSide(1, ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY)),
        )
