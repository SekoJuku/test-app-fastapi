from pymongo import MongoClient
from app.settings import settings

client = MongoClient(settings.DATABASE_URL)

db = client[settings.MONGO_INITDB_DATABASE]