import flet as ft

TITLE: str = 'Greeings App'


def main(page: ft.Page):
    page.title = TITLE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def say_hello(e):
        print("Hello, world!")

    # TITLE
    page_title_text: ft.Text = ft.Text(
        value=TITLE, size=36, font_family='arial', weight=600
    )

    # NAME
    first_name_field: ft.TextField = ft.TextField(
        hint_text='First name',
        width=600
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
        value="Hello [first_name] [last_name]",
        font_family='arial',
        size=36,
        weight=800
    )

    page.add(
        ft.Column([
            ft.Row([page_title_text], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([first_name_field], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([last_name_field], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([send_button], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([greeting], alignment=ft.MainAxisAlignment.CENTER)
        ])
    )


ft.app(target=main)
