import flet as ft
from partials.sidebar import Sidebar
from partials.content import MainContent
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class AppTheme:
    # Temas disponíveis (cores primárias)
    THEMES = {
        'Âmbar': ft.Colors.AMBER,
        'Azul': ft.Colors.BLUE,
        'Roxo': ft.Colors.PURPLE,
        'Verde': ft.Colors.GREEN,
        'Rosa': ft.Colors.PINK,
        'Laranja': ft.Colors.ORANGE,
        'Ciano': ft.Colors.CYAN,
        'Vermelho': ft.Colors.RED,
    }

    # Fundos disponíveis (cor de fundo, cor de superfície, cor de texto)
    BACKGROUNDS = {
        'Escuro': ('#20202a', '#2d2d3a', ft.Colors.WHITE),
        'Cinza': ('#1a1a1a', '#2a2a2a', ft.Colors.WHITE),
        'Azul Escuro': ('#0a1929', '#1a2942', ft.Colors.WHITE),
        'Roxo Escuro': ('#1a0a2e', '#2a1a3e', ft.Colors.WHITE),
        'Verde Escuro': ('#0a1e0a', '#1a2e1a', ft.Colors.WHITE),
        'Claro': ('#f5f5f5', '#ffffff', ft.Colors.BLACK),
        'Branco': ('#ffffff', '#f0f0f0', ft.Colors.BLACK),
        'Azul Claro': ('#e3f2fd', '#bbdefb', ft.Colors.BLACK),
        'Rosa Claro': ('#fce4ec', '#f8bbd0', ft.Colors.BLACK),
        'Verde Claro': ('#e8f5e9', '#c8e6c9', ft.Colors.BLACK),
    }

    @staticmethod
    def create_theme(primary_color=ft.Colors.AMBER, background_colors=('#20202a', '#2d2d3a', ft.Colors.WHITE)):
        text_color = background_colors[2]  # Cor do texto baseada no fundo
        return ft.Theme(
            color_scheme=ft.ColorScheme(
                background=background_colors[0],
                on_surface=background_colors[1],
                on_inverse_surface=background_colors[1],
                primary=primary_color,
            ),
            text_theme=ft.TextTheme(
                body_large=ft.TextStyle(
                    weight=ft.FontWeight.BOLD,
                    color=text_color,
                    size=14,
                ),
                body_medium=ft.TextStyle(
                    weight=ft.FontWeight.NORMAL,
                    color=text_color,
                    size=14,
                ),
                headline_large=ft.TextStyle(
                    weight=ft.FontWeight.W_900,
                    color=text_color,
                    size=50,
                ),
                label_large=ft.TextStyle(
                    weight=ft.FontWeight.W_700,
                    color=text_color,
                    size=16,
                ),
                headline_medium=ft.TextStyle(
                    weight=ft.FontWeight.W_900,
                    color=text_color,
                    size=30,
                ),
            ),
            scrollbar_theme=ft.ScrollbarTheme(
                track_visibility=False,
                thumb_visibility=False,
                track_color={
                    ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,
                },
                thumb_color={
                    ft.ControlState.HOVERED: ft.Colors.TRANSPARENT,
                    ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,
                }
            )
        )

class App:
    def __init__(self, page:ft.Page):
        self.page = page
        self.current_theme = 'Âmbar'
        self.current_background = 'Escuro'
        self.page.theme = AppTheme.create_theme(
            AppTheme.THEMES[self.current_theme],
            AppTheme.BACKGROUNDS[self.current_background]
        )
        self.page.on_resized = self.show_app_bar
        self.page.bgcolor = ft.Colors.BLACK
        self.main()
        self.show_app_bar()
        self.create_settings_button()

    def toggle_sidebar(self, e):
        self.sidebar.col['xs'] = 12 if self.sidebar.col['xs'] == 0 else 0
        self.content.col['xs'] = 0 if self.content.col['xs'] == 12 else 12
        self.page.update()
        


    def show_app_bar(self,e = None):
        if self.page.width < 768:
            self.page.appbar = ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.Icons.MENU,
                    icon_color=ft.Colors.WHITE,
                    on_click=self.toggle_sidebar
                ),
                bgcolor=ft.Colors.ON_SURFACE
            )
            self.layout.spacing = 0
            self.page.bgcolor = ft.Colors.ON_SURFACE
        else:
            self.page.appbar = None
            self.layout.spacing = 10
            self.page.bgcolor = ft.Colors.BLACK
            
        self.page.update()


    def change_theme(self, e):
        # Muda a cor primária
        theme_name = e.control.data
        self.current_theme = theme_name
        self.page.theme = AppTheme.create_theme(
            AppTheme.THEMES[theme_name],
            AppTheme.BACKGROUNDS[self.current_background]
        )
        self.update_settings_dialog()
        self.page.update()

    def change_background(self, e):
        # Muda a cor de fundo
        bg_name = e.control.data
        self.current_background = bg_name
        self.page.theme = AppTheme.create_theme(
            AppTheme.THEMES[self.current_theme],
            AppTheme.BACKGROUNDS[bg_name]
        )
        self.update_settings_dialog()
        self.page.update()

    def update_settings_dialog(self):
        # Atualiza os botões para mostrar a seleção atual
        self.settings_dialog.content = self.create_settings_content()

    def open_settings(self, e):
        # Anima o botão de configurações
        self.settings_button.rotate = ft.Rotate(angle=3.14159)  # 180 graus
        self.settings_dialog.open = True
        self.page.update()

    def close_settings(self, e):
        # Reseta a animação do botão
        self.settings_button.rotate = ft.Rotate(angle=0)
        self.settings_dialog.open = False
        self.page.update()

    def create_settings_content(self):
        # Cria os botões de cor primária
        theme_buttons = []
        for theme_name, theme_color in AppTheme.THEMES.items():
            theme_buttons.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                name=ft.Icons.CIRCLE,
                                color=theme_color,
                                size=30,
                            ),
                            ft.Text(
                                value=theme_name,
                                size=16,
                                weight=ft.FontWeight.BOLD if theme_name == self.current_theme else ft.FontWeight.NORMAL,
                            ),
                            ft.Icon(
                                name=ft.Icons.CHECK_CIRCLE,
                                color=theme_color,
                                size=20,
                            ) if theme_name == self.current_theme else ft.Container()
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    padding=ft.padding.all(15),
                    data=theme_name,
                    on_click=self.change_theme,
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE) if theme_name == self.current_theme else None,
                    border_radius=10,
                    ink=True,
                )
            )

        # Cria os botões de fundo
        background_buttons = []
        for bg_name, bg_colors in AppTheme.BACKGROUNDS.items():
            background_buttons.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                width=30,
                                height=30,
                                bgcolor=bg_colors[0],
                                border_radius=5,
                                border=ft.border.all(2, ft.Colors.WHITE24),
                            ),
                            ft.Text(
                                value=bg_name,
                                size=16,
                                weight=ft.FontWeight.BOLD if bg_name == self.current_background else ft.FontWeight.NORMAL,
                            ),
                            ft.Icon(
                                name=ft.Icons.CHECK_CIRCLE,
                                color=ft.Colors.PRIMARY,
                                size=20,
                            ) if bg_name == self.current_background else ft.Container()
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    padding=ft.padding.all(15),
                    data=bg_name,
                    on_click=self.change_background,
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE) if bg_name == self.current_background else None,
                    border_radius=10,
                    ink=True,
                )
            )

        # Retorna o conteúdo do diálogo
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Cor Primária",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Divider(height=10),
                    *theme_buttons,
                    ft.Divider(height=30),
                    ft.Text(
                        "Cor de Fundo",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Divider(height=10),
                    *background_buttons,
                ],
                tight=True,
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=ft.padding.all(20),
            width=400,
        )

    def create_settings_button(self):
        # Cria o diálogo de configurações
        self.settings_dialog = ft.AlertDialog(
            title=ft.Text("Configurações de Tema", size=22, weight=ft.FontWeight.BOLD),
            content=self.create_settings_content(),
            actions=[
                ft.TextButton(
                    "Fechar",
                    on_click=self.close_settings,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=ft.padding.symmetric(horizontal=20, vertical=10),
                    ),
                ),
            ],
            shape=ft.RoundedRectangleBorder(radius=15),
        )

        # Cria o botão de configurações no overlay com animação
        self.settings_icon = ft.IconButton(
            icon=ft.Icons.SETTINGS,
            icon_color=ft.Colors.WHITE,
            tooltip="Configurações de Tema",
            on_click=self.open_settings,
            bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.BLACK),
            icon_size=24,
        )

        self.settings_button = ft.Container(
            content=self.settings_icon,
            right=10,
            top=10,
            border_radius=30,
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=10,
                color=ft.Colors.with_opacity(0.3, ft.Colors.PRIMARY),
            ),
            animate_rotation=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
        )

        self.page.overlay.append(self.settings_button)
        self.page.overlay.append(self.settings_dialog)
        self.page.update()

    def main(self):
        self.sidebar = Sidebar(col={'xs': 0, 'md':5, 'lg': 4, 'xxl':3})
        self.content = MainContent(col={'xs': 12, 'md':7 ,'lg': 8, 'xxl':9})

        self.layout = ft.ResponsiveRow(
            columns=12,
            controls=[
                self.sidebar,
                self.content,
            ],
            expand=True
        )

        self.page.add(self.layout)

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')