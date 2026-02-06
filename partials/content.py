import flet as ft
from components.styles import glassmorphism_container, section_header


class ProjectItem(ft.Container):
    def __init__(self, title: str, description: str, url: str,
                 index: int = 0, category: str = "Web", **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.description = description
        self.url = url
        self.index = index
        self.category = category

        self.padding = ft.padding.all(30)
        self.bgcolor = ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE)
        self.border_radius = 15
        self.border = ft.border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY))
        self.animate_scale = ft.Animation(200, ft.AnimationCurve.EASE_OUT)
        self.animate = ft.Animation(200, ft.AnimationCurve.EASE_OUT)
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        )

        self.height = 280
        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Container(
                    width=50,
                    height=4,
                    bgcolor=ft.Colors.PRIMARY,
                    border_radius=2,
                    margin=ft.margin.only(bottom=10),
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                value=f"0{self.index}",
                                size=12,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.PRIMARY,
                            ),
                            padding=ft.padding.symmetric(horizontal=10, vertical=4),
                            border=ft.border.all(1, ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY)),
                            border_radius=8,
                        ),
                        ft.Container(
                            content=ft.Text(
                                value=self.category,
                                size=11,
                                weight=ft.FontWeight.W_600,
                                color=ft.Colors.with_opacity(0.7, ft.Colors.WHITE),
                            ),
                            padding=ft.padding.symmetric(horizontal=10, vertical=4),
                            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                            border_radius=8,
                        ),
                    ],
                    spacing=8,
                ),
                ft.Container(height=10),
                ft.Text(value=self.title, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                ft.Container(height=8),
                ft.Text(value=self.description, theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ft.Container(expand=True),
                ft.Container(
                    content=ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    value='VER AO VIVO',
                                    theme_style=ft.TextThemeStyle.BODY_LARGE,
                                    color=ft.Colors.PRIMARY,
                                    weight=ft.FontWeight.BOLD,
                                    size=13,
                                ),
                                ft.Icon(name=ft.Icons.ARROW_OUTWARD, size=16, color=ft.Colors.PRIMARY),
                            ],
                            tight=True,
                            spacing=6,
                        ),
                        url=self.url,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=ft.padding.symmetric(horizontal=20, vertical=12),
                        )
                    ),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
                    border_radius=10,
                ),
            ]
        )
        self.on_hover = self._on_hover

    def _on_hover(self, e):
        if e.data == "true":
            self.scale = 1.03
            self.border = ft.border.all(1, ft.Colors.with_opacity(0.4, ft.Colors.PRIMARY))
            self.shadow = ft.BoxShadow(
                spread_radius=3,
                blur_radius=25,
                color=ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY),
                offset=ft.Offset(0, 8),
            )
        else:
            self.scale = 1.0
            self.border = ft.border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY))
            self.shadow = ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, 4),
            )
        self.update()


class ServiceItem(ft.Container):
    def __init__(self, icon: str, title: str, description: str,
                 highlights: list = None, **kwargs):
        super().__init__(**kwargs)

        self.bgcolor = ft.Colors.with_opacity(0.3, ft.Colors.ON_SURFACE)
        self.padding = ft.padding.all(30)
        self.border_radius = 20
        self.border = ft.border.only(
            top=ft.BorderSide(3, ft.Colors.PRIMARY),
            left=ft.BorderSide(1, ft.Colors.with_opacity(0.15, ft.Colors.PRIMARY)),
            right=ft.BorderSide(1, ft.Colors.with_opacity(0.15, ft.Colors.PRIMARY)),
            bottom=ft.BorderSide(1, ft.Colors.with_opacity(0.15, ft.Colors.PRIMARY)),
        )
        self.shadow = ft.BoxShadow(
            spread_radius=2,
            blur_radius=20,
            color=ft.Colors.with_opacity(0.15, ft.Colors.BLACK),
            offset=ft.Offset(0, 5),
        )
        self.animate_scale = ft.Animation(200, ft.AnimationCurve.EASE_OUT)
        self.animate = ft.Animation(200, ft.AnimationCurve.EASE_OUT)
        self.height = 380

        highlight_controls = []
        if highlights:
            for h in highlights:
                highlight_controls.append(
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.CHECK_CIRCLE, color=ft.Colors.PRIMARY, size=18),
                            ft.Text(value=h, size=13, weight=ft.FontWeight.W_500),
                        ],
                        spacing=8,
                    )
                )

        self.content = ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            controls=[
                ft.Container(
                    content=ft.Icon(name=icon, color=ft.Colors.PRIMARY, size=40),
                    padding=ft.padding.all(20),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                    border_radius=50,
                ),
                ft.Container(height=5),
                ft.Text(
                    value=title,
                    theme_style=ft.TextThemeStyle.LABEL_LARGE,
                    size=18,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    value=description,
                    theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                    size=13,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.with_opacity(0.7, ft.Colors.WHITE),
                ),
                ft.Container(expand=True),
                ft.Divider(height=10, color=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY)),
                ft.Column(spacing=10, controls=highlight_controls),
            ]
        )
        self.on_hover = self._on_hover

    def _on_hover(self, e):
        if e.data == "true":
            self.scale = 1.05
            self.shadow = ft.BoxShadow(
                spread_radius=4,
                blur_radius=30,
                color=ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY),
                offset=ft.Offset(0, 10),
            )
        else:
            self.scale = 1.0
            self.shadow = ft.BoxShadow(
                spread_radius=2,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.15, ft.Colors.BLACK),
                offset=ft.Offset(0, 5),
            )
        self.update()


class CertificationItem(ft.Container):
    def __init__(self, title: str, institution: str, year: str,
                 icon: str = None, url: str = None, **kwargs):
        super().__init__(**kwargs)

        if icon is None:
            icon = ft.Icons.WORKSPACE_PREMIUM

        self.bgcolor = ft.Colors.with_opacity(0.3, ft.Colors.ON_SURFACE)
        self.padding = ft.padding.all(25)
        self.border_radius = 16
        self.border = ft.border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY))
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        )
        self.animate_scale = ft.Animation(200, ft.AnimationCurve.EASE_OUT)
        self.animate = ft.Animation(200, ft.AnimationCurve.EASE_OUT)

        link_row = []
        if url:
            link_row.append(
                ft.TextButton(
                    content=ft.Row(
                        controls=[
                            ft.Text(value='Ver certificado', size=12, color=ft.Colors.PRIMARY,
                                    weight=ft.FontWeight.W_600),
                            ft.Icon(name=ft.Icons.ARROW_OUTWARD, size=14, color=ft.Colors.PRIMARY),
                        ],
                        tight=True,
                        spacing=4,
                    ),
                    url=url,
                )
            )

        self.content = ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Container(
                    content=ft.Icon(name=icon, color=ft.Colors.PRIMARY, size=30),
                    padding=ft.padding.all(15),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                    border_radius=14,
                ),
                ft.Column(
                    expand=True,
                    spacing=4,
                    controls=[
                        ft.Text(
                            value=title,
                            theme_style=ft.TextThemeStyle.LABEL_LARGE,
                            size=15,
                        ),
                        ft.Text(
                            value=institution,
                            size=13,
                            color=ft.Colors.with_opacity(0.7, ft.Colors.WHITE),
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text(
                                        value=year,
                                        size=11,
                                        weight=ft.FontWeight.W_600,
                                        color=ft.Colors.PRIMARY,
                                    ),
                                    padding=ft.padding.symmetric(horizontal=10, vertical=3),
                                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                                    border_radius=8,
                                ),
                                *link_row,
                            ],
                            spacing=10,
                        ),
                    ],
                ),
            ],
        )
        self.on_hover = self._on_hover

    def _on_hover(self, e):
        if e.data == "true":
            self.scale = 1.02
            self.border = ft.border.all(1, ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY))
            self.shadow = ft.BoxShadow(
                spread_radius=2, blur_radius=20,
                color=ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY),
                offset=ft.Offset(0, 6),
            )
        else:
            self.scale = 1.0
            self.border = ft.border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY))
            self.shadow = ft.BoxShadow(
                spread_radius=1, blur_radius=15,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, 4),
            )
        self.update()


class MainContent(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand = True

        # --- Helper: Stat Card ---
        def stat_card(icon: str, number: str, label: str) -> ft.Container:
            card = glassmorphism_container(
                col={'xs': 6, 'md': 3},
                padding=ft.padding.all(25),
                animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    controls=[
                        ft.Icon(name=icon, color=ft.Colors.PRIMARY, size=32),
                        ft.Text(
                            value=number,
                            size=36,
                            weight=ft.FontWeight.W_900,
                            color=ft.Colors.PRIMARY,
                        ),
                        ft.Text(
                            value=label,
                            size=14,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.W_500,
                        ),
                    ],
                ),
            )
            card.on_hover = lambda e: _stat_hover(e, card)
            return card

        def _stat_hover(e, card):
            if e.data == "true":
                card.scale = 1.05
                card.shadow = ft.BoxShadow(
                    spread_radius=2, blur_radius=25,
                    color=ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY),
                )
            else:
                card.scale = 1.0
                card.shadow = ft.BoxShadow(
                    spread_radius=0, blur_radius=20,
                    color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                )
            card.update()

        # --- Banner ---
        banner = ft.Container(
            shadow=ft.BoxShadow(
                color=ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY),
                offset=ft.Offset(x=0, y=-50),
                spread_radius=-30,
                blur_radius=30,
            ),
            image=ft.DecorationImage(
                src='images/bg_2.jpg',
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                opacity=0.3,
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[
                    ft.Colors.with_opacity(0.7, ft.Colors.ON_SURFACE),
                    ft.Colors.with_opacity(0.5, ft.Colors.PRIMARY),
                ],
            ),
            bgcolor=ft.Colors.ON_SURFACE,
            margin=ft.margin.only(top=30),
            border_radius=20,
            padding=20,
            content=ft.ResponsiveRow(
                columns=12,
                vertical_alignment=ft.CrossAxisAlignment.END,
                controls=[
                    ft.Container(
                        col={'md': 12, 'lg': 8},
                        padding=ft.padding.all(50),
                        content=ft.Column(
                            controls=[
                                ft.ShaderMask(
                                    content=ft.Text(
                                        value='Descubra meu Incrível Portifólio',
                                        theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
                                        color=ft.Colors.WHITE,
                                    ),
                                    shader=ft.LinearGradient(
                                        begin=ft.alignment.center_left,
                                        end=ft.alignment.center_right,
                                        colors=[ft.Colors.WHITE, ft.Colors.PRIMARY],
                                    ),
                                    blend_mode=ft.BlendMode.SRC_IN,
                                ),
                                ft.Text(
                                    value='Fullstack Developer & UI Designer',
                                    size=18,
                                    weight=ft.FontWeight.W_500,
                                    color=ft.Colors.with_opacity(0.7, ft.Colors.WHITE),
                                    italic=True,
                                ),
                                ft.Text(
                                    spans=[
                                        ft.TextSpan(text='<', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                        ft.TextSpan(text='code', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                        ft.TextSpan(text='>', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                        ft.TextSpan(
                                            text='Eu desenvolvo aplicativos iOS e Android, softwares para MacOS, Windows e Linux. Além de Websites Responsivos e Tratamento de Dados.',
                                            style=ft.TextStyle(size=16),
                                        ),
                                        ft.TextSpan(text='</', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                        ft.TextSpan(text='code', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                        ft.TextSpan(text='>', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                        ft.TextSpan(text=' |', style=ft.TextStyle(
                                            color=ft.Colors.PRIMARY,
                                            weight=ft.FontWeight.BOLD,
                                            size=18,
                                        )),
                                    ],
                                    theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                                ),
                                ft.ElevatedButton(
                                    bgcolor=ft.Colors.PRIMARY,
                                    content=ft.Row(
                                        controls=[
                                            ft.Text(value='Explore agora', color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD, size=16),
                                            ft.Icon(name=ft.Icons.ARROW_FORWARD_ROUNDED, color=ft.Colors.BLACK, size=20),
                                        ],
                                        tight=True,
                                        spacing=10,
                                    ),
                                    url='#',
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=30),
                                        padding=ft.padding.symmetric(horizontal=40, vertical=22),
                                        shadow_color=ft.Colors.PRIMARY,
                                        elevation=10,
                                    ),
                                )
                            ],
                            spacing=30,
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ),
                ]
            )
        )

        # --- Experience Stats ---
        experience = ft.Container(
            padding=ft.padding.symmetric(vertical=20),
            content=ft.ResponsiveRow(
                columns=12,
                spacing=20,
                run_spacing=20,
                controls=[
                    stat_card(ft.Icons.WORK_OUTLINE, "3+", "Anos de\nexperiência"),
                    stat_card(ft.Icons.CODE, "100+", "Projetos\nconcluídos"),
                    stat_card(ft.Icons.PEOPLE_OUTLINE, "200+", "Clientes\nsatisfeitos"),
                    stat_card(ft.Icons.LANGUAGE, "5+", "Linguagens de\ndomínio"),
                ],
            ),
        )

        # --- Projects ---
        projects = ft.Container(
            padding=ft.padding.symmetric(horizontal=20, vertical=20),
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ProjectItem(
                        title='Site Lavanderia',
                        description='Site completo de uma lavanderia, com informações sobre o negócio, exposição de serviços e contato.',
                        url='https://allcleancb.netlify.app/',
                        index=1, category='Web',
                        col={'xs': 12, 'md': 6, 'lg': 4},
                    ),
                    ProjectItem(
                        title='Sistema de Agendamento',
                        description='Sistema desenvolvido para fins de agendamento de serviços estéticos.',
                        url='https://github.com/MarceloPorfirio/Navigation_Flet/blob/main/agenda.py',
                        index=2, category='App',
                        col={'xs': 12, 'md': 6, 'lg': 4},
                    ),
                    ProjectItem(
                        title='Sistema de Agendamento de Estética',
                        description='Sistema completo de agendamento de serviços estéticos com gestão de horários e clientes.',
                        url='https://studiojuliabrys.icoders.com.br',
                        index=3, category='Web',
                        col={'xs': 12, 'md': 6, 'lg': 4},
                    ),
                    ProjectItem(
                        title='DashBoard Supermarket',
                        description='Modelo de analise de dados detalhada de um dashboard fictício de supermercados.',
                        url='https://dashsupermarket-brm4ykhyagv7egfofsv7yr.streamlit.app/',
                        index=4, category='Data',
                        col={'xs': 12, 'md': 6, 'lg': 4},
                    ),
                    ProjectItem(
                        title='iCoders',
                        description='Site institucional da iCoders, empresa de desenvolvimento de software e soluções digitais.',
                        url='https://icoders.com.br',
                        index=5, category='Web',
                        col={'xs': 12, 'md': 6, 'lg': 4},
                    ),
                    ProjectItem(
                        title='Card Ecommerce',
                        description='Um card interativo para utilização em diversas páginas de web e desktop.\n',
                        url='https://github.com/MarceloPorfirio/Card_Ecommerce',
                        index=6, category='UI',
                        col={'xs': 12, 'md': 6, 'lg': 4},
                    ),
                ],
                spacing=30,
                run_spacing=30,
            ),
        )

        # --- Serviços ---
        services = ft.ResponsiveRow(
            columns=12,
            spacing=30,
            run_spacing=30,
            controls=[
                ServiceItem(
                    icon=ft.Icons.WEB,
                    title='Desenvolvimento Web',
                    description='Sites modernos, responsivos e otimizados para performance.',
                    highlights=['Landing Pages', 'Sites Institucionais', 'E-commerce', 'SEO'],
                    col={'xs': 12, 'lg': 4},
                ),
                ServiceItem(
                    icon=ft.Icons.PHONE_IPHONE,
                    title='Apps Multiplataforma',
                    description='Aplicativos nativos para iOS, Android, Windows, Mac e Linux.',
                    highlights=['Flet / Flutter', 'UI Responsiva', 'APIs REST', 'Banco de Dados'],
                    col={'xs': 12, 'lg': 4},
                ),
                ServiceItem(
                    icon=ft.Icons.ANALYTICS,
                    title='Análise de Dados',
                    description='Dashboards interativos e tratamento de dados para decisões inteligentes.',
                    highlights=['Python & Pandas', 'Dashboards', 'Automação', 'Relatórios'],
                    col={'xs': 12, 'lg': 4},
                ),
            ]
        )

        # --- Formação & Certificações ---
        certifications = ft.ResponsiveRow(
            columns=12,
            spacing=20,
            run_spacing=20,
            controls=[
                CertificationItem(
                    icon=ft.Icons.SCHOOL,
                    title='Análise e Desenvolvimento de Sistemas',
                    institution='Uniritter',
                    year='2021 - 2023',
                    col={'xs': 12, 'md': 6},
                ),
                CertificationItem(
                    title='Digital Transformation Technologies',
                    institution='Dell Technologies',
                    year='2022',
                    url='https://www.unisinos.br/certificados/3088C4DEA2CC861835A0397B2CC44EF6A539C744',
                    col={'xs': 12, 'md': 6},
                ),
                CertificationItem(
                    title='Python Completo',
                    institution='DevMedia',
                    year='2023',
                    col={'xs': 12, 'md': 6},
                ),
                CertificationItem(
                    title='JavaScript Completo',
                    institution='DevMedia',
                    year='2023',
                    col={'xs': 12, 'md': 6},
                ),
                CertificationItem(
                    title='Flet - Introdutório e Avançado',
                    institution='Udemy',
                    year='2024',
                    col={'xs': 12, 'md': 6},
                ),
                CertificationItem(
                    title='React e Firebase',
                    institution='Udemy',
                    year='2024',
                    col={'xs': 12, 'md': 6},
                ),
            ],
        )

        # --- Tech Stack ---
        def tech_badge(name: str, icon: str):
            return ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Icon(name=icon, color=ft.Colors.PRIMARY, size=20),
                        ft.Text(value=name, size=13, weight=ft.FontWeight.W_600),
                    ],
                    spacing=8,
                    tight=True,
                ),
                padding=ft.padding.symmetric(horizontal=16, vertical=10),
                bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                border=ft.border.all(1, ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
                border_radius=20,
            )

        tech_stack = ft.Container(
            padding=ft.padding.symmetric(vertical=30),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Text(
                        value="TECH STACK",
                        size=12,
                        weight=ft.FontWeight.W_700,
                        color=ft.Colors.with_opacity(0.5, ft.Colors.PRIMARY),
                        letter_spacing=2,
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        wrap=True,
                        spacing=12,
                        run_spacing=12,
                        controls=[
                            tech_badge("Python", ft.Icons.CODE),
                            tech_badge("Flutter", ft.Icons.PHONE_ANDROID),
                            tech_badge("Flet", ft.Icons.WIDGETS),
                            tech_badge("PostgreSQL", ft.Icons.STORAGE),
                            tech_badge("MongoDB", ft.Icons.CLOUD),
                            tech_badge("JavaScript", ft.Icons.JAVASCRIPT),
                            tech_badge("React", ft.Icons.WEB),
                            tech_badge("Git", ft.Icons.COMMIT),
                            tech_badge("Docker", ft.Icons.INVENTORY_2),
                            tech_badge("Streamlit", ft.Icons.DASHBOARD),
                        ],
                    ),
                ],
            ),
        )

        # --- Footer ---
        self.scroll_column = ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            spacing=40,
            controls=[
                banner,
                experience,
                section_header(title='Projetos', subtitle='Alguns dos meus trabalhos recentes'),
                projects,
                section_header(title='Serviços', subtitle='Soluções sob medida para o seu projeto'),
                services,
                section_header(title='Formação & Certificações', subtitle='Aprendizado contínuo e qualificação profissional'),
                certifications,
                tech_stack,
                ft.Container(
                    bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                    padding=ft.padding.symmetric(vertical=30, horizontal=30),
                    border=ft.border.only(
                        top=ft.BorderSide(1, ft.Colors.with_opacity(0.15, ft.Colors.PRIMARY)),
                    ),
                    border_radius=ft.border_radius.only(top_left=20, top_right=20),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=15,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.TextButton(
                                        content=ft.Row(
                                            controls=[
                                                ft.Icon(name=ft.Icons.ARROW_UPWARD, size=16, color=ft.Colors.PRIMARY),
                                                ft.Text(value="Voltar ao topo", color=ft.Colors.PRIMARY, size=13),
                                            ],
                                            tight=True,
                                            spacing=5,
                                        ),
                                        on_click=lambda e: self.scroll_column.scroll_to(offset=0, duration=600),
                                    ),
                                ],
                            ),
                            ft.Divider(height=1, color=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY)),
                            ft.ResponsiveRow(
                                columns=12,
                                controls=[
                                    ft.Text(
                                        col={'xs': 12, 'md': 6},
                                        value='© 2025 Todos os direitos reservados.',
                                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                                    ),
                                    ft.Text(
                                        col={'xs': 12, 'md': 6},
                                        spans=[
                                            ft.TextSpan(text='Email: '),
                                            ft.TextSpan(
                                                text='marcelobrys20@gmail.com',
                                                url='mailto:marcelobrys20@gmail.com',
                                                style=ft.TextStyle(color=ft.Colors.PRIMARY),
                                            ),
                                        ],
                                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                                        text_align=ft.TextAlign.END,
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
            ]
        )

        self.content = self.scroll_column
        self.bgcolor = ft.Colors.ON_SURFACE
        self.padding = ft.padding.all(30)
