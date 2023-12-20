import flet as ft

from qrcodegen.components import (
    MainDataTable,
    MainTextField,
    PasteButton,
    QRCodeField,
    RegisterButton,
)
from qrcodegen.database.db import session

PAGE_TITLE = "QR Code Generator"


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = PAGE_TITLE
    page.window_width = 850
    page.window_height = 800

    qrcode_field = QRCodeField()
    text_box = MainTextField(qrcode_field)

    table = MainDataTable(session)

    paste_btn = PasteButton(text_box, qrcode_field)
    register_btn = RegisterButton(session, table, text_box, qrcode_field)

    # "horizontal_alignment" of ft.Row may not work when the row is inside a ft.Column.
    # Hence, insert empty ft.Card to align items by force.
    buttons_row = ft.Row([paste_btn, ft.Card(width=350), register_btn])

    layout = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Column(
                            [
                                text_box,
                                buttons_row,
                            ],
                        ),
                        ft.Container(
                            qrcode_field,
                            bgcolor=ft.colors.GREY_200,
                            padding=2,
                        ),
                    ]
                ),
                ft.Divider(),
                ft.Column([table], scroll=True, height=500),
            ]
        ),
        padding=10,
    )

    page.add(layout)
    page.update()
