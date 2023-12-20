import logging

import flet as ft

from qrcodegen.models.url import Url

logger = logging.getLogger(__name__)


class DeleteButton(ft.UserControl):
    def __init__(self, session, table, row):
        super().__init__()

        self._session = session
        self._table = table
        self._row = row

    def build(self):
        def on_click_delete_record(e: ft.ControlEvent):
            target_url = e.control.data
            target = self._session.query(Url).filter_by(url=target_url).first()
            self._session.delete(target)
            self._session.commit()

            self._table.update_rows()

        button = ft.IconButton(
            icon=ft.icons.DELETE,
            data=self._row.url,
            on_click=on_click_delete_record,
        )

        return button
