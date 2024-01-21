import flet as ft

TITLE: str = 'Greeings App'
WIDTH: int = 625
HEIGHT: int = 325


def main(page: ft.Page):
    page.title = TITLE

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.window_width = WIDTH
    page.window_height = HEIGHT

    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT

    def toggle_mode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_button.icon = ft.icons.LIGHT_MODE

        elif page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_button.icon = ft.icons.DARK_MODE

        page.update()

    def say_hello(e):
        first_name_field.current.focus()

        first_name: str = first_name_field.current.value.strip(' ').title()

        if first_name == '':
            return

        first_name_field.current.value = ''

        greeting.value = f"Hello, {first_name}!"
        greeting.update()

        first_name_field.current.update()

    def clear_greeting(e):
        first_name_field.current.focus()

        if greeting.value == '':
            return

        greeting.value = ''
        greeting.update()

    page_title_text: ft.Text = ft.Text(
        value=TITLE, size=36, font_family='arial', weight=600
    )

    theme_button: ft.IconButton = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,
        on_click=toggle_mode
    )

    first_name_field = ft.Ref[ft.TextField(value='')]()

    send_button: ft.ElevatedButton = ft.ElevatedButton(
        text="SEND", width=200, height=60, on_click=say_hello
    )

    clear_button: ft.ElevatedButton = ft.ElevatedButton(
        text='CLEAR', width=200, height=60, on_click=clear_greeting
    )

    greeting: ft.Text = ft.Text(
        font_family='arial',
        size=36,
        weight=800
    )

    page.add(
        ft.Column([
            ft.Row([page_title_text, theme_button]),
            ft.TextField(ref=first_name_field, label='first name'),
            ft.Row([send_button, clear_button]),
            greeting
        ])
    )


ft.app(target=main)
