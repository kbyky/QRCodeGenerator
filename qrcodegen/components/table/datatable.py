import logging

import flet as ft
from sqlalchemy.orm import Session

from qrcodegen.components.buttons import CopyButton, DeleteButton
from qrcodegen.components.table.cells.namecell import NameCell
from qrcodegen.models.url import Url

logger = logging.getLogger(__name__)


class MainDataTable(ft.UserControl):
    def __init__(self, session: Session):
        super().__init__()

        self._session = session

    @property
    def columns(_):
        return [
            ft.DataColumn(ft.Text("Name")),
            ft.DataColumn(ft.Text("QR Code")),
            ft.DataColumn(ft.Text("Text")),
            # Icon field
            ft.DataColumn(
                ft.Text(""),
            ),
        ]

    def get_rows(self):
        return [
            ft.DataRow(
                cells=[
                    ft.DataCell(NameCell(self._session, self, row.name, row.url)),
                    ft.DataCell(ft.Image(src_base64=row.qrcode, width=100)),
                    ft.DataCell(ft.Text(row.url, width=300)),
                    ft.DataCell(
                        ft.Row(
                            [
                                CopyButton(row),
                                DeleteButton(self._session, self, row),
                            ]
                        )
                    ),
                ]
            )
            for row in self._session.query(Url).all()
        ]

    def update_rows(self):
        self._table.rows = self.get_rows()
        self.update()

    def build(self):
        self._table = ft.DataTable(
            data_row_min_height=120,
            data_row_max_height=120,
            columns=self.columns,
            rows=self.get_rows(),
        )

        return self._table
