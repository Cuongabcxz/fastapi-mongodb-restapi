from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

from models.model_user import User
from database.mongodb import conn
from schemas.schema_user import userEntity, usersEntity
from cache.crud import get_hash, delete_hash, save_hash
from utils.valid_password import password_check

fake_db = []


async def all_user():
    return usersEntity(conn.local.user.find())


async def add_new_user(user: User):
    # OPERATION DB
    new_user = dict(user)  # Lấy object dưới dạng json
    fake_db.append(new_user)

    data_cache = get_hash(new_user["id"])
    bool_pass = password_check(new_user["password"])
    if data_cache is not None:
        if bool_pass is False:
            print('Save in Redis')
            # OPERATION CACHE
            await save_hash(key=new_user["id"], data=new_user)  # Lưu data vao redis
        else:
            del new_user["id"]
            print("Save in Mongo")
            new_user["password"] = sha256_crypt.encrypt(new_user["password"])
            id = conn.local.user.insert_one(new_user).inserted_id  # Lưu data vào mongo
            user = conn.local.user.find_one({"_id": id})
    return user


async def update_user_id(id: str, user: User):
    conn.local.user.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(user)
    })
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


def get_user_id(id: str):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))
