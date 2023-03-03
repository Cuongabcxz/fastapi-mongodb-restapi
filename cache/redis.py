import aioredis
from aioredis import ConnectionError
from setting.config import settings
try:
    redis = aioredis.from_url(settings.REDIS_URL, db=settings.REDIS_DB)
    print("CONNECTED TO REDIS!")
except ConnectionError as e:
    print(e)
