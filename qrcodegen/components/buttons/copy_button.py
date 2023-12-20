import logging

import flet as ft
import pyperclip

logger = logging.getLogger(__name__)


class CopyButton(ft.UserControl):
    def __init__(self, row):
        super().__init__()

        self._row = row

    def build(self):
        def on_click_copy_contents(e: ft.ControlEvent):
            target_url = e.control.data
            pyperclip.copy(target_url)

        button = ft.IconButton(
            icon=ft.icons.CONTENT_COPY,
            data=self._row.url,
            on_click=on_click_copy_contents,
            # width=0,
        )

        return button
