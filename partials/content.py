import flet as ft

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
    def build(self):
        return ft.Container(
            bgcolor=ft.colors.ON_SURFACE_VARIANT,
            padding=ft.padding.symmetric(vertical=20,horizontal=50),
            content=ft.Column(
                controls=[
                    ft.Text(value='Pagamento por hora', theme_style=ft.TextThemeStyle.LABEL_LARGE,color='white'),

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
                PriceItem(),
            ]

        )
        testimonials = ft.Container()
        logos = ft.Container()
        footer = ft.Container()


        return ft.Container(
            content=ft.Column(
                controls=[
                    # banner,
                    # experience,
                    # projects,
                    prices,
                    testimonials,
                    logos,
                    footer
                ]
            ),
            bgcolor=ft.colors.ON_BACKGROUND,
            padding=ft.padding.all(30)
        )