from sqlalchemy import Column, String
from sqlalchemy.schema import PrimaryKeyConstraint

from qrcodegen.database.db import Base


class Url(Base):
    __tablename__ = "url"

    name = Column(String)
    url = Column(String)
    qrcode = Column(String)

    __tableargs__ = (PrimaryKeyConstraint(url),)
