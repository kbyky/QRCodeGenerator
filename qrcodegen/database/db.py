import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

engine = create_engine(f"sqlite:///{os.getcwd()}/.QRCodeGenerator/data.db")
session = Session(autocommit=False, bind=engine)
