import logging

import flet as ft
import pyperclip

logger = logging.getLogger(__name__)


class PasteButton(ft.UserControl):
    def __init__(self, url_box, qr_code_img):
        super().__init__()

        self._url_box = url_box
        self._qr_code_img = qr_code_img

    def build(self):
        def on_click_paste(_):
            text = pyperclip.paste()
            self._url_box.text = text

            self._qr_code_img.src = text

        return ft.ElevatedButton(text="Paste from\nClipboard", on_click=on_click_paste)