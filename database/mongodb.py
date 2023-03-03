from pymongo import MongoClient
from setting.config import settings

try:
    conn = MongoClient(settings.APP_DB_MONGO_URI)
    print("CONNECTED TO MONGO!")
except ConnectionError as e:
    print(e)
