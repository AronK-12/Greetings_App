import flet as ft

TITLE: str = 'Greeings App'
WIDTH: int = 625
HEIGHT: int = 400


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
        first_name: str = first_name_field.value
        last_name: str = last_name_field.value

        first_name = first_name.strip(' ').title()
        last_name = last_name.strip(' ').title()

        if first_name == '' or last_name == '':
            return

        first_name_field.value = ''
        last_name_field.value = ''

        greeting.value = f"Hello, {first_name} {last_name}!"
        greeting.update()

        last_name_field.update()

        first_name_field.update()
        first_name_field.focus()

    # TITLE
    page_title_text: ft.Text = ft.Text(
        value=TITLE, size=36, font_family='arial', weight=600
    )

    theme_button: ft.IconButton = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,
        on_click=toggle_mode
    )

    # NAME
    first_name_field: ft.TextField = ft.TextField(
        hint_text='First name',
        width=600,
        autofocus=True
    )
    last_name_field: ft.TextField = ft.TextField(
        hint_text='Last name',
        width=600
    )

    # SEND
    send_button: ft.ElevatedButton = ft.ElevatedButton(
        text="SEND", width=200, height=60, on_click=say_hello
    )

    # ON SEND REVEAL
    greeting: ft.Text = ft.Text(
        font_family='arial',
        size=36,
        weight=800
    )

    page.add(
        ft.Column([
            ft.Row([page_title_text, theme_button]),
            first_name_field,
            last_name_field,
            send_button,
            greeting
        ])
    )


ft.app(target=main)
