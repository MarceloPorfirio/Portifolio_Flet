import flet as ft
from typing import List, Dict, Union
import math
from components.carousel import Carousel

class ProjectItem(ft.Container):
    def __init__(self, title: str, description: str, url: str, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.description = description
        self.url = url

        # Configura o próprio container com visual moderno
        self.padding = ft.padding.all(30)
        self.bgcolor = ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE)
        self.border_radius = 15
        self.border = ft.border.all(1, ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY))
        self.animate_scale = ft.Animation(200, ft.AnimationCurve.EASE_OUT)
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        )

        self.content = ft.Column(
            controls=[
                ft.Text(value=self.title, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                ft.Container(height=10),
                ft.Text(value=self.description),
                ft.Container(height=15),
                ft.TextButton(
                    content=ft.Row(
                        controls=[
                            ft.Text(value='VER AO VIVO', theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.Colors.PRIMARY, weight=ft.FontWeight.BOLD),
                            ft.Icon(name=ft.Icons.ARROW_FORWARD, size=18, color=ft.Colors.PRIMARY),
                        ],
                        tight=True,
                    ),
                    url=self.url,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        padding=ft.padding.symmetric(horizontal=20, vertical=12),
                    )
                )
            ]
        )
        self.on_hover = self._on_hover

    def _on_hover(self, e):
        if e.data == "true":
            self.scale = 1.03
            self.shadow = ft.BoxShadow(
                spread_radius=3,
                blur_radius=25,
                color=ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY),
                offset=ft.Offset(0, 8),
            )
        else:
            self.scale = 1.0
            self.shadow = ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, 4),
            )
        self.update()

class PriceItem(ft.Container):
    def __init__(self, price: int, url: str, items_included: List[Dict[str, bool]], **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.url = url
        self.items_included = items_included

        # Configura o próprio container com visual moderno
        self.bgcolor = ft.Colors.with_opacity(0.3, ft.Colors.ON_SURFACE)
        self.padding = ft.padding.symmetric(vertical=30, horizontal=40)
        self.border_radius = 20
        self.border = ft.border.all(2, ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY))
        self.shadow = ft.BoxShadow(
            spread_radius=2,
            blur_radius=20,
            color=ft.Colors.with_opacity(0.15, ft.Colors.BLACK),
            offset=ft.Offset(0, 5),
        )
        self.animate_scale = ft.Animation(200, ft.AnimationCurve.EASE_OUT)

        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            controls=[
                ft.Container(
                    content=ft.Text(value='Pagamento por hora', theme_style=ft.TextThemeStyle.LABEL_LARGE),
                    padding=ft.padding.symmetric(vertical=10, horizontal=20),
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                    border_radius=20,
                ),
                ft.Text(
                    spans=[
                        ft.TextSpan(text='R$', style=ft.TextStyle(size=20)),
                        ft.TextSpan(text=f' {self.price} ', style=ft.TextStyle(color=ft.Colors.PRIMARY, weight=ft.FontWeight.BOLD, size=48)),
                        ft.TextSpan(text='/hora', style=ft.TextStyle(size=16)),
                    ]
                ),
                ft.Divider(height=20, color=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY)),
                ft.Column(
                    spacing=15,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(
                                    name=ft.Icons.CHECK_CIRCLE if item['is_included'] else ft.Icons.CANCEL,
                                    color=ft.Colors.PRIMARY if item['is_included'] else ft.Colors.with_opacity(0.3, ft.Colors.WHITE),
                                    size=22,
                                ),
                                ft.Text(
                                    value=item['title'],
                                    weight=ft.FontWeight.W_500 if item['is_included'] else ft.FontWeight.NORMAL,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.START
                        ) for item in self.items_included
                    ]
                ),
                ft.Container(height=10),
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Text(value='ESCOLHER PLANO', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                            ft.Icon(name=ft.Icons.ARROW_FORWARD, size=18, color=ft.Colors.BLACK)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        tight=True,
                    ),
                    bgcolor=ft.Colors.PRIMARY,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=12),
                        padding=ft.padding.symmetric(horizontal=30, vertical=15),
                    ),
                    url=self.url
                )
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

class PriceItemPopular(ft.Stack):
    def __init__(self, price: int, url: str, items_included: List[Dict[str, bool]], **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.url = url
        self.items_included = items_included

        # Cria o PriceItem
        price_item = PriceItem(
            price=self.price,
            url=self.url,
            items_included=self.items_included
        )

        # Configura o próprio Stack
        self.controls = [
            price_item,
            ft.Container(
                bgcolor=ft.Colors.PRIMARY,
                content=ft.Text(value='Popular', color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                padding=ft.padding.symmetric(vertical=5, horizontal=50),
                right=-40,
                top=15,
                rotate=ft.Rotate(angle=math.radians(40)),
            )
        ]

class TestimonialItem(ft.Container):
    def __init__(self, user: str, job: str, testimonial: str, image_src: str = 'images/testimonial-default.jpg', **kwargs):
        super().__init__(**kwargs)
        self.user = user
        self.job = job
        self.testimonial = testimonial
        self.image_src = image_src

        # Configura o próprio container com visual moderno
        self.bgcolor = ft.Colors.with_opacity(0.4, ft.Colors.ON_SURFACE)
        self.padding = ft.padding.all(35)
        self.margin = ft.margin.only(top=30)
        self.width = 450
        self.border_radius = 20
        self.border = ft.border.all(1, ft.Colors.with_opacity(0.15, ft.Colors.PRIMARY))
        self.shadow = ft.BoxShadow(
            spread_radius=2,
            blur_radius=20,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            offset=ft.Offset(0, 5),
        )

        self.content = ft.Stack(
            controls=[
                ft.Column(
                    spacing=15,
                    controls=[
                        ft.Icon(
                            name=ft.Icons.FORMAT_QUOTE,
                            color=ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY),
                            size=40,
                        ),
                        ft.Text(
                            value=self.testimonial,
                            theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                            size=15,
                            italic=True,
                        ),
                        ft.Container(height=10),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.PRIMARY, size=20),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.PRIMARY, size=20),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.PRIMARY, size=20),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.PRIMARY, size=20),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.PRIMARY, size=20),
                                ],
                                tight=True,
                                spacing=5,
                            ),
                            padding=ft.padding.symmetric(vertical=8, horizontal=15),
                            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PRIMARY),
                            border_radius=25,
                        ),
                        ft.Container(height=5),
                        ft.Text(value=self.user, theme_style=ft.TextThemeStyle.LABEL_LARGE, size=17),
                        ft.Text(
                            value=self.job,
                            theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                            italic=True,
                            color=ft.Colors.with_opacity(0.7, ft.Colors.PRIMARY),
                        ),
                    ]
                ),
                ft.Container(
                    content=ft.Image(
                        src=self.image_src,
                        border_radius=ft.border_radius.all(100),
                        width=90,
                        height=90,
                        fit=ft.ImageFit.COVER,
                    ),
                    border=ft.border.all(4, ft.Colors.PRIMARY),
                    border_radius=100,
                    shadow=ft.BoxShadow(
                        spread_radius=2,
                        blur_radius=10,
                        color=ft.Colors.with_opacity(0.4, ft.Colors.PRIMARY),
                    ),
                    top=-15,
                    right=10,
                )
            ]
        )

class MainContent(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expand = True

        # Configura banner com gradiente moderno
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
                        col={'md':12,'lg':8},
                        padding=ft.padding.all(50),
                        content=ft.Column(
                            controls=[
                                ft.Text(value='Descubra meu Incrível Portifólio', theme_style=ft.TextThemeStyle.HEADLINE_LARGE),
                                ft.Text(
                                    spans=[
                                        ft.TextSpan(text='<', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                        ft.TextSpan(text='code', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                        ft.TextSpan(text='>', style=ft.TextStyle(color=ft.Colors.PRIMARY)),

                                        ft.TextSpan(text='Eu desenvolvo aplicativos iOS e Android, softwares para MacOS, Windows e Linux. Além de Websites Responsivos e Tratamento de Dados.',
                                                    style=ft.TextStyle(size=16)),

                                        ft.TextSpan(text='</', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                        ft.TextSpan(text='code', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                        ft.TextSpan(text='>', style=ft.TextStyle(color=ft.Colors.PRIMARY)),

                                    ],
                                    theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                                ),
                                ft.ElevatedButton(
                                    bgcolor=ft.Colors.PRIMARY,
                                    content=ft.Row(
                                        controls=[
                                            ft.Text(value='Explore agora', color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD, size=16),
                                            ft.Icon(name=ft.Icons.ARROW_FORWARD, color=ft.Colors.BLACK, size=20),
                                        ],
                                        tight=True,
                                        spacing=10,
                                    ),
                                    url='#',
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=25),
                                        padding=ft.padding.symmetric(horizontal=35, vertical=20),
                                        shadow_color=ft.Colors.PRIMARY,
                                        elevation=8,
                                    ),
                                )

                            ],
                            spacing=30,
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ),

                    # ft.Container(
                    #     col={'md':12,'lg':4},
                    #     content=ft.Image(
                    #         # src='images/eu_port.png',
                    #         width=15,
                    #         # scale=ft.Scale(scale=1.8, alignment=ft.alignment.bottom_center)
                    #     )
                    # )
                ]
            )

        )

        # Configura experience
        experience = ft.Container(
            padding=ft.padding.symmetric(vertical=20),
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ft.Text(
                        col={'xs': 6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                            text='3 +',
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                            ft.TextSpan(
                                text=' Anos de \nexperiência',
                                style=ft.TextStyle(
                                    size=16
                                )
                            )
                        ]
                    ),
                    ft.Text(
                        col={'xs': 6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                            text='100 +',
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                            ft.TextSpan(
                                text=' Projetos \nconcluídos',
                                style=ft.TextStyle(
                                    size=16
                                )
                            )
                        ]
                    ),
                    ft.Text(
                        col={'xs': 6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                            text='200 +',
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                            ft.TextSpan(
                                text=' Clientes \nsatisfeitos',
                                style=ft.TextStyle(
                                    size=16
                                )
                            )
                        ]
                    ),
                    ft.Text(
                        col={'xs': 6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                            text='5 +',
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                            ft.TextSpan(
                                text=' Linguagens de \ndomínio',
                                style=ft.TextStyle(
                                    size=16
                                )
                            )
                        ]
                    ),
                ]
            )
        )

        # Configura projects
        projects = ft.Container(
            padding=ft.padding.symmetric(horizontal=20, vertical=20),  # Adiciona padding ao redor do ResponsiveRow
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ProjectItem(
                        title='Site Lavanderia',
                        description='Site completo de uma lavanderia, com informações sobre o negócio, exposição de serviços e contato.',
                        url='https://allcleancb.netlify.app/',
                        col={'xs':12, 'md': 6, 'lg': 4},
                    ),
                    ProjectItem(
                        title='Sistema de Agendamento',
                        description='Sistema desenvolvido para fins de agendamento de serviços estéticos.',
                        url='https://github.com/MarceloPorfirio/Navigation_Flet/blob/main/agenda.py',
                        col={'xs':12, 'md': 6, 'lg': 4},
                    ),
                    ProjectItem(
                        title='Layout Clone Instagram',
                        description='Layout desenvolvido com a poderosa framework do python, Flet - baseado em Flutter.',
                        url='https://github.com/MarceloPorfirio/Clone_insta',
                        col={'xs':12, 'md': 6, 'lg': 4},
                    ),
                    ProjectItem(
                        title='DashBoard Supermarket',
                        description='Modelo de analise de dados detalhada de um dashboard fictício de supermercados.',
                        url='https://dashsupermarket-brm4ykhyagv7egfofsv7yr.streamlit.app/',
                        col={'xs':12, 'md': 6, 'lg': 4},
                    ),
                    ProjectItem(
                        title='ToDo App',
                        description='App completo para cadastro de tarefas, incluindo banco de dados.\n',
                        url='https://github.com/MarceloPorfirio/Full_ToDo_App',
                        col={'xs':12, 'md': 6, 'lg': 4},
                    ),
                    ProjectItem(
                        title='Card Ecommerce',
                        description='Um card interativo para utilização em diversas páginas de web e desktop.\n',
                        url='https://github.com/MarceloPorfirio/Card_Ecommerce',
                        col={'xs':12, 'md': 6, 'lg': 4},
                    ),
                ],
                spacing=30,
                run_spacing=30,
            ),
        )

        # Configura prices
        prices = ft.ResponsiveRow(
            columns=12,
            spacing=30,
            run_spacing=30,
            controls=[
                PriceItem(
                    price=20,
                    url='',
                    items_included=[
                        {'title': 'Prototipagem','is_included': True},
                        {'title': 'Desenvolvimento Web','is_included': True},
                        {'title': 'App multiplataforma','is_included': False},
                        {'title': 'Manutenção Mensal','is_included': False},
                    ],
                    col={'xs': 12, 'lg': 4},
                ),
                PriceItemPopular(
                    price=100,
                    url='',
                    items_included=[
                        {'title': 'Prototipagem','is_included': True},
                        {'title': 'Desenvolvimento Web','is_included': True},
                        {'title': 'App multiplataforma','is_included': True},
                        {'title': 'Manutenção Mensal','is_included': False},
                    ],
                    col={'xs': 12, 'lg': 4},
                ),
                PriceItem(
                    price=200,
                    url='',
                    items_included=[
                        {'title': 'Prototipagem','is_included': True},
                        {'title': 'Desenvolvimento Web','is_included': True},
                        {'title': 'App multiplataforma','is_included': True},
                        {'title': 'Manutenção Mensal','is_included': True},
                    ],
                    col={'xs': 12, 'lg': 4},
                ),
            ]

        )

        # Configura testimonials
        testimonials = Carousel(
            controls=[
                TestimonialItem(
                    user='Paula Rocha',
                    job='Desenvolvedora Júnior',
                    testimonial = 'O trabalho do Marcelo é realmente incrivel. Tudo ficou mais fácil e interativo.'
                ),
                TestimonialItem(
                    user='Vera Lúcia',
                    job='Analista Contábil',
                    testimonial = 'O trabalho do Marcelo é realmente incrivel. Tudo ficou mais fácil e interativo.',
                    image_src = 'images/testimonial-1-280x280.jpg',
                ),
                TestimonialItem(
                    user='Vera Lúcia',
                    job='Analista Contábil',
                    testimonial = 'O trabalho do Marcelo é realmente incrivel. Tudo ficou mais fácil e interativo.',
                    image_src = 'images/testimonial-1-280x280.jpg',
                ),
                TestimonialItem(
                    user='Vera Lúcia',
                    job='Analista Contábil',
                    testimonial = 'O trabalho do Marcelo é realmente incrivel. Tudo ficou mais fácil e interativo.',
                    image_src = 'images/testimonial-1-280x280.jpg',
                ),

            ]
        )

        # Configura logos
        logos = ft.Container(
            padding=ft.padding.all(30),
            opacity=0.6,
            content=ft.ResponsiveRow(
                controls=[
                    ft.Image(
                        src='images/brand-1-464x512.png',
                        col={'xs': 6 , 'lg': 3 , 'xl':2}
                    ),
                    ft.Image(
                        src='images/brand-2-458x512.png',
                        col={'xs': 6 , 'lg': 3 , 'xl':2}
                    ),
                    ft.Image(
                        src='images/brand-3-456x512.png',
                        col={'xs': 6 , 'lg': 3 , 'xl':2}
                    ),
                    ft.Image(
                        src='images/brand-1-464x512.png',
                        col={'xs': 6 , 'lg': 3 , 'xl':2}
                    ),

                ],
                spacing=30,
                run_spacing=30,
            )
        )

        # Configura footer
        footer = ft.Container(
            bgcolor='#2d2d3a',  # Cor customizada para substituir ON_SURFACE_VARIANT
            padding=ft.padding.all(30),
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ft.Text(
                        col={'xs': 12, 'md': 6},
                        value='₢ 2024 Todos os direitos reservados.',
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,

                    ),
                    ft.Text(
                        col={'xs': 12, 'md': 6},
                        spans=[
                            ft.TextSpan(text='Email:'),
                            ft.TextSpan(
                                text='marcelobrys20@gmail.com',
                                url='mailto:marcelobrys20@gmail.com',

                            )
                        ],
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                        text_align=ft.TextAlign.END
                    ),

                ]
            )
        )

        # Função auxiliar para títulos de seções
        def sections_title(title: str):
            return ft.Container(
                padding=ft.padding.symmetric(vertical=20),
                content=ft.Text(value=title, theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)
            )

        # Configura o próprio container (MainContent)
        self.content = ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            spacing=40,
            controls=[
                banner,
                experience,
                sections_title(title='Projetos'),
                projects,
                sections_title(title='Preços'),
                prices,
                sections_title(title='Recomendações'),
                testimonials,
                logos,
                footer
            ]
        )
        self.bgcolor = ft.Colors.ON_SURFACE
        self.padding = ft.padding.all(30)
