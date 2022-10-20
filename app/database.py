from pymongo import MongoClient
from app.settings import settings

client = MongoClient(settings.MONGO_URL)

db = client['test-app']
