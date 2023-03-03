import json
from cache.redis import redis
from redis.exceptions import ResponseError


# Lưu giá trị vào redis
async def save_hash(key: str, data: dict):
    try:
        await redis.hset(name=key, mapping=data)
    except ResponseError as e:
        print(e)


# Lấy ra giá trị từ redis
async def get_hash(key: str):
    try:
        return await redis.hgetall(name=key)
    except ResponseError as e:
        print(e)


# Xóa giá trị từ redis
def delete_hash(key: str, keys: list):
    try:
        redis.hdel(key, *keys)
    except ResponseError as e:
        print(e)




