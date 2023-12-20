import logging

import flet as ft

logger = logging.getLogger(__name__)


class MainTextField(ft.UserControl):
    def __init__(self, qrcode_field):
        super().__init__()

        self._qrcode_field = qrcode_field

    def focus(self):
        self.focus()

    @property
    def text(self):
        return self._textfield.value

    @text.setter
    def text(self, text):
        self._textfield.value = text
        self.update()

    def build(self):
        def on_change(e: ft.ControlEvent):
            self._qrcode_field.src = e.data

        self._textfield = ft.TextField(
            label="Input text to generate QR code",
            hint_text="https://www...",
            on_change=on_change,
            width=600,
            autofocus=True,
            height=120,
            multiline=True,
            min_lines=4,
            max_lines=4,
        )

        return self._textfield
