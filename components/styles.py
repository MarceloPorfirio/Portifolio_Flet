import flet as ft


def glassmorphism_container(**kwargs) -> ft.Container:
    defaults = dict(
        bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.ON_SURFACE),
        border=ft.border.all(1, ft.Colors.with_opacity(0.15, ft.Colors.WHITE)),
        border_radius=20,
        blur=ft.Blur(10, 10, ft.BlurTileMode.MIRROR),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=20,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        ),
    )
    defaults.update(kwargs)
    return ft.Container(**defaults)


def section_header(title: str, subtitle: str = "") -> ft.Container:
    controls = [
        ft.Row(
            controls=[
                ft.Container(
                    width=4,
                    height=35,
                    bgcolor=ft.Colors.PRIMARY,
                    border_radius=2,
                ),
                ft.Text(value=title, theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
            ],
            spacing=15,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    ]
    if subtitle:
        controls.append(
            ft.Text(
                value=subtitle,
                size=14,
                color=ft.Colors.with_opacity(0.6, ft.Colors.WHITE),
            )
        )
    controls.append(
        ft.Container(
            width=60,
            height=3,
            bgcolor=ft.Colors.PRIMARY,
            border_radius=2,
            margin=ft.margin.only(top=5),
        )
    )
    return ft.Container(
        padding=ft.padding.symmetric(vertical=20),
        content=ft.Column(controls=controls, spacing=8),
    )


def sidebar_section_label(label: str) -> ft.Container:
    return ft.Container(
        content=ft.Text(
            value=label.upper(),
            size=11,
            weight=ft.FontWeight.W_700,
            color=ft.Colors.with_opacity(0.5, ft.Colors.PRIMARY),
        ),
        margin=ft.margin.only(bottom=10),
    )
