import logging

import flet as ft

from qrcodegen.models.url import Url

logger = logging.getLogger(__name__)


class NameCell(ft.UserControl):
    def __init__(self, session, table, name, text):
        super().__init__()

        self._session = session
        self._table = table
        self._name = name
        self._text = text

    def build(self):
        def on_blur(_):
            if textfield.value:
                target = (
                    self._session.query(Url)
                    .filter_by(name=self._name, url=self._text)
                    .first()
                )
                target.name = textfield.value

                self._session.commit()
                self._name = textfield.value
                self.page.update()

        textfield = ft.TextField(
            value=self._name,
            on_blur=on_blur,
            text_size=12,
            border_color=ft.colors.WHITE,
            focused_border_color=ft.colors.BLUE_400,
            max_lines=3,
            shift_enter=True,
        )

        return ft.Container(textfield, width=120)
