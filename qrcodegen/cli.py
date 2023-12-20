import logging
import os

import flet as ft
from sqlalchemy import inspect

from qrcodegen.components.page import main
from qrcodegen.database.db import Base, engine

logger = logging.getLogger(__name__)

DATABASE_DIR = ".QRCodeGenerator"

if __name__ == "__main__":
    # QRCodeGenerator automatically creates sqlite database in users home directory.
    db_dir = f"{os.getcwd()}/{DATABASE_DIR}"
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    if not inspect(engine).get_table_names():
        Base.metadata.create_all(bind=engine)

    ft.app(target=main)
