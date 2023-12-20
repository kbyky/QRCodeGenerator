import logging
from datetime import datetime

import flet as ft

from qrcodegen.models.url import Url

logger = logging.getLogger(__name__)


class RegisterButton(ft.UserControl):
    def __init__(self, session, table, text_field, qrcode_field):
        super().__init__()

        self._session = session
        self._table = table
        self._text_field = text_field
        self._qrcode_field = qrcode_field

    def build(self):
        def on_click_register(_):
            if not self._text_field.text:
                # url_box.focus()
                return

            target = (
                self._session.query(Url).filter_by(url=self._text_field.text).first()
            )
            if target:
                return

            self._session.merge(
                Url(
                    name=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    url=self._text_field.text,
                    qrcode=self._qrcode_field.src,
                )
            )
            self._session.commit()

            self._table.update_rows()

        return ft.ElevatedButton(text="Register", on_click=on_click_register)
