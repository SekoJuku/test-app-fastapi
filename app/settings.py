import os

from pydantic import BaseSettings


class Settings:
    MONGO_URL: str
    MONGO_INITDB_DATABASE: str

    def __init__(self):
        self.MONGO_URL = os.getenv('MONGO_URL')
        self.MONGO_INITDB_DATABASE = os.getenv('MONGO_INITDB_DATABASE')


settings = Settings()
