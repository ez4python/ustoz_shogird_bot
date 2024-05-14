from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

load_dotenv()
Base = declarative_base()


class Config:
    DB_NAME = getenv('DB_NAME')
    DB_USER = getenv('DB_USER')
    DB_PASSWORD = getenv('DB_PASSWORD')
    DB_HOST = getenv('DB_HOST')
    DB_CONFIG = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


engine = create_engine(Config().DB_CONFIG)
session = Session(engine)
