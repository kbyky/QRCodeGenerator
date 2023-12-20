import logging

import flet as ft

from qrcodegen.utils.images import generate_qr_code, to_b64

logger = logging.getLogger(__name__)


class QRCodeField(ft.UserControl):
    @property
    def src(self):
        return self._qrcode_field.src_base64

    @src.setter
    def src(self, text):
        self._qrcode_field.src_base64 = to_b64(generate_qr_code(text))
        self.update()

    def build(self):
        self._qrcode_field = ft.Image(src_base64=to_b64(b" "), width=200, height=200)

        return self._qrcode_field
