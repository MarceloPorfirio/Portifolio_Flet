import flet as ft
from typing import List, Dict, Union
import math

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
                                ft.Text(value=self.url,theme_style=ft.TextThemeStyle.BODY_LARGE,color=ft.colors.PRIMARY),
                                ft.Icon(name=ft.icons.ARROW_FORWARD_IOS,size=14,color=ft.colors.PRIMARY),
                            ],
                            tight=True,
                        ),
                        url='#',
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
                            ft.TextSpan(text=f' {self.price} ',style=ft.TextStyle(color=ft.colors.PRIMARY,weight=ft.FontWeight.BOLD,size=50)),
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
    def build(self):
        return ft.Container(
            bgcolor=ft.colors.ON_SURFACE_VARIANT,
            padding=ft.padding.all(30),
            margin=ft.margin.only(top=20),
            width=400,
            content=ft.Stack(
                controls=[
                    ft.Column(
                    controls=[
                        ft.Text(value='Paula Rocha',theme_style=ft.TextThemeStyle.LABEL_LARGE,color='white'),
                        ft.Text(value='Desenvolvedora Júnior',theme_style=ft.TextThemeStyle.BODY_MEDIUM,color='white',italic=True)
                    ]
                )
                ]
            )
        )

class MainContent(ft.UserControl):
    def __init__(self):
        super().__init__()
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
                            src='images/face-2.png',
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
        testimonials = ft.Row(
            controls=[
                TestimonialItem(),

            ]
        )
        logos = ft.Container()
        footer = ft.Container()


        return ft.Container(
            content=ft.Column(
                controls=[
                    # banner,
                    # experience,
                    # projects,
                    # prices,
                    testimonials,
                    logos,
                    footer
                ]
            ),
            bgcolor=ft.colors.ON_BACKGROUND,
            padding=ft.padding.all(30)
        )