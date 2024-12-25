import flet as ft
from typing import List, Dict, Union
import math
from components.carousel import Carousel

class ProjectItem(ft.UserControl):
    def __init__(self, title: str, description: str, url: str, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.description = description
        self.url = url

    def build(self):
        return ft.Container(
            padding=ft.padding.all(30),
            bgcolor=ft.colors.ON_SURFACE_VARIANT,
            content=ft.Column(
                controls=[
                    ft.Text(value=self.title,theme_style=ft.TextThemeStyle.LABEL_LARGE,color='white'),
                    ft.Text(value=self.description,color='white'),
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Text(value='VER AO VIVO',theme_style=ft.TextThemeStyle.BODY_LARGE,color=ft.colors.PRIMARY),
                                ft.Icon(name=ft.icons.ARROW_FORWARD_IOS,size=14,color=ft.colors.PRIMARY),
                            ],
                            tight=True,
                        ),
                        url=self.url,
                    )

                ]
            )
        )
    
class PriceItem(ft.UserControl):
    def __init__(self,price: int, url: str, items_included: List[Dict[str,bool]], **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.url = url
        self.items_included = items_included

    def build(self):
        return ft.Container(
            bgcolor=ft.colors.ON_SURFACE_VARIANT,
            padding=ft.padding.symmetric(vertical=20,horizontal=50),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30,
                controls=[
                    ft.Text(value='Pagamento por hora', theme_style=ft.TextThemeStyle.LABEL_LARGE,color='white'),
                    ft.Text(
                        spans=[
                            ft.TextSpan(text='R$', style=ft.TextStyle(color=ft.colors.WHITE)),
                            ft.TextSpan(text=f' {self.price} ',style=ft.TextStyle(color=ft.colors.PRIMARY,weight=ft.FontWeight.BOLD,size=40)),
                            ft.TextSpan(text='/hora',style=ft.TextStyle(color=ft.colors.WHITE)),
                        ]
                    ),
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(
                                      name=ft.icons.CHECK if item['is_included'] else ft.icons.CLOSE,
                                      color=ft.colors.PRIMARY,   
                                    ),
                                    ft.Text(value=item['title'],color='white') 
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ) for item in self.items_included
                                                  ]
                    ),
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Text(value='QUERO ESTE', theme_style=ft.TextThemeStyle.BODY_LARGE,color=ft.colors.PRIMARY),
                                ft.Icon(name=ft.icons.ARROW_FORWARD_IOS,size=14,color=ft.colors.PRIMARY)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        url=self.url
                    )

                ]
            )
        )   

class PriceItemPopular(PriceItem):
    def build(self):
        price_item = super().build()
        return ft.Stack(
            controls=[
                price_item,
                ft.Container(
                    bgcolor=ft.colors.PRIMARY,
                    content=ft.Text(value='Popular',color=ft.colors.BLACK,weight=ft.FontWeight.BOLD),
                    padding=ft.padding.symmetric(vertical=5,horizontal=50),
                    right=-40,
                    top=15,
                    rotate=ft.Rotate(angle=math.radians(40)),
                )
            ]
        )
    
class TestimonialItem(ft.UserControl):
    def __init__(self,user: str, job: str, testimonial: str,image_src: str = 'images/testimonial-default.jpg', **kwargs):
        super().__init__(**kwargs)
        self.user = user
        self.job = job
        self.testimonial = testimonial
        self.image_src = image_src

    def build(self):
        return ft.Container(
            bgcolor=ft.colors.ON_SURFACE_VARIANT,
            padding=ft.padding.all(30),
            margin=ft.margin.only(top=20),
            width=400,
            content=ft.Stack(
                controls=[
                    ft.Column(
                        spacing=0,
                        controls=[
                            ft.Text(value=self.user,theme_style=ft.TextThemeStyle.LABEL_LARGE,color='white'),
                            ft.Text(value=self.job,theme_style=ft.TextThemeStyle.BODY_MEDIUM,color='white',italic=True),

                            ft.Container(height=20),
                            ft.Text(
                                value=self.testimonial,
                                theme_style=ft.TextThemeStyle.BODY_MEDIUM,color=ft.colors.WHITE,
                            ),

                            ft.Container(height=20),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.icons.STAR,color=ft.colors.PRIMARY),
                                        ft.Icon(name=ft.icons.STAR,color=ft.colors.PRIMARY),
                                        ft.Icon(name=ft.icons.STAR,color=ft.colors.PRIMARY),
                                        ft.Icon(name=ft.icons.STAR,color=ft.colors.PRIMARY),
                                        ft.Icon(name=ft.icons.STAR,color=ft.colors.PRIMARY),
                                    ],
                                    tight=True
                                ),
                                bgcolor=ft.colors.ON_BACKGROUND,
                                padding=ft.padding.symmetric(vertical=5,horizontal=10),
                                border_radius=ft.border_radius.all(50),
                            )
                        ]
                ),

                ft.Image(
                    src= self.image_src,
                    border_radius=ft.border_radius.all(100),
                    width=100,
                    top=0,
                    right=0,
                    offset=ft.Offset(x=0,y=-0.5)
                )
                ]
            )
        )

class MainContent(ft.UserControl):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        self.expand=True

    def build(self):
        banner = ft.Container(
            shadow=ft.BoxShadow(
                color=ft.colors.WHITE60,
                offset=ft.Offset(x=0,y=-60), # definir o tamanho da sombra como 60
                spread_radius=-30, # cortar para metade para dar o efeito.
            ),
            image_src='images/bg.jpg',
            image_fit=ft.ImageFit.COVER,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
            image_opacity=0.5,
            bgcolor=ft.colors.ON_BACKGROUND,
            margin=ft.margin.only(top=30), # deslocar para baixo para usar o boxShadow
            content=ft.ResponsiveRow(
                columns=12,
                vertical_alignment=ft.CrossAxisAlignment.END,
                controls=[
                    ft.Container(
                        col={'md':12,'lg':8},
                        padding=ft.padding.all(50),
                        content=ft.Column(
                            controls=[
                                ft.Text(value='Descubra meu Incrível Portifólio',theme_style=ft.TextThemeStyle.HEADLINE_LARGE,color='white'),
                                ft.Text(
                                    spans=[
                                        ft.TextSpan(text='<',style=ft.TextStyle(color=ft.colors.PRIMARY)),
                                        ft.TextSpan(text='code',style=ft.TextStyle(color=ft.colors.PRIMARY)),
                                        ft.TextSpan(text='>',style=ft.TextStyle(color=ft.colors.PRIMARY)),

                                        ft.TextSpan(text='Eu desenvolvo aplicativos iOS e Android, softwares para MacOS, Windows e Linux. Além de Websites Responsivos e Tratamento de Dados.',
                                                    style=ft.TextStyle(color=ft.colors.WHITE)),

                                        ft.TextSpan(text='</',style=ft.TextStyle(color=ft.colors.PRIMARY)),
                                        ft.TextSpan(text='code',style=ft.TextStyle(color=ft.colors.PRIMARY)),
                                        ft.TextSpan(text='>',style=ft.TextStyle(color=ft.colors.PRIMARY)),            

                                    ],
                                    theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                                ),
                                ft.ElevatedButton(
                                    bgcolor=ft.colors.PRIMARY,
                                    content=ft.Text(value='Explore agora',color=ft.colors.BLACK,weight=ft.FontWeight.BOLD),
                                    url='#',
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                                )
                                
                            ],
                            spacing=30,
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ),

                    ft.Container(
                        col={'md':12,'lg':4},
                        content=ft.Image(
                            src='images/eu_port.png',
                            width=15,
                            # scale=ft.Scale(scale=1.8, alignment=ft.alignment.bottom_center)
                        )
                    )
                ]
            )

        )
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
                                color=ft.colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                            ft.TextSpan(
                                text=' Anos de experiência',
                                style=ft.TextStyle(
                                    color=ft.colors.WHITE,
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
                                color=ft.colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                            ft.TextSpan(
                                text=' Projetos concluídos',
                                style=ft.TextStyle(
                                    color=ft.colors.WHITE,
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
                                color=ft.colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                            ft.TextSpan(
                                text=' Clientes Satisfeitos',
                                style=ft.TextStyle(
                                    color=ft.colors.WHITE,
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
                                color=ft.colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                            ft.TextSpan(
                                text=' Linguagens de domínio',
                                style=ft.TextStyle(
                                    color=ft.colors.WHITE,
                                    size=16
                                )
                            )
                        ]
                    ),
                ]
            )
        )
        projects = ft.ResponsiveRow(
            columns=12,
            controls=[
                ProjectItem(
                    title='Calculadora Iphone', 
                    description='Calculadora com o mesmo visual do App Calculadora para iOS.',
                    url='VER AO VIVO',
                    col={'xs':12, 'md': 6, 'lg': 4},
                ),
                 ProjectItem(
                    title='Calculadora Iphone', 
                    description='Calculadora com o mesmo visual do App Calculadora para iOS.',
                    url='VER AO VIVO',
                    col={'xs':12, 'md': 6, 'lg': 4},
                ),
                 ProjectItem(
                    title='Calculadora Iphone', 
                    description='Calculadora com o mesmo visual do App Calculadora para iOS.',
                    url='VER AO VIVO',
                    col={'xs':12, 'md': 6, 'lg': 4},
                ),
                 ProjectItem(
                    title='DashBoard Supermarket', 
                    description='Modelo de analise de dados detalhada de um dashboard fictício de supermercados. ',
                    url='https://dashsupermarket-brm4ykhyagv7egfofsv7yr.streamlit.app/',
                    col={'xs':12, 'md': 6, 'lg': 4},
                ),
                 ProjectItem(
                    title='ToDo App', 
                    description='App completo para cadastro de tarefas, incluindo banco de dados.',
                    url='https://github.com/MarceloPorfirio/Full_ToDo_App',
                    col={'xs':12, 'md': 6, 'lg': 4},
                ),
                 ProjectItem(
                    title='Card Ecommerce', 
                    description='Um card interativo para utilização em diversas páginas de web e desktop.',
                    url='https://github.com/MarceloPorfirio/Card_Ecommerce',
                    col={'xs':12, 'md': 6, 'lg': 4},
                ),
            ],
            spacing=30,
            run_spacing=30,
        )
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
                        {'title': 'Aplicativo multiplataforma','is_included': False},
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
                        {'title': 'Aplicativo multiplataforma','is_included': True},
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
                        {'title': 'Aplicativo multiplataforma','is_included': True},
                        {'title': 'Manutenção Mensal','is_included': True}, 
                    ],
                    col={'xs': 12, 'lg': 4},
                ),
            ]

        )
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
        footer = ft.Container(
            bgcolor=ft.colors.ON_SURFACE_VARIANT,
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

        def sections_title(title: str):
            return ft.Container(
                padding=ft.padding.symmetric(vertical=20),
                content=ft.Text(value=title,theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,color='white')
            )


        return ft.Container(
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
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
            ),
            bgcolor=ft.colors.ON_BACKGROUND,
            padding=ft.padding.all(30)
        )