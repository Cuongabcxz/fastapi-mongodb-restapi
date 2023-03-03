from fastapi import APIRouter, status, Response
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from models.model_user import User
from database.mongodb import conn
from utils.service_user import add_new_user, update_user_id, get_user_id, all_user

view_user = APIRouter()

fake_db = []


@view_user.get('/users', response_model=list[User], tags=["users"])
async def find_all_users():
    try:
        # print(list(conn.local.user.find()))
        result = all_user()
        return result
    except Exception as e:
        return e


@view_user.post('/users', response_model=User, tags=["users"])
async def create_user(user: User):
    try:
        result = await add_new_user(user)
        return result
    except Exception as e:
        return e


@view_user.get('/users/{id}')
async def find_user(id: str):
    try:
        result = await get_user_id(id)
        return result
    except Exception as e:
        return e


@view_user.put("/users/{id}", response_model=User, tags=["users"])
async def update_user(id: str, user: User):
    try:
        result = await update_user_id(id, user)
        return result
    except Exception as e:
        return e


@view_user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    conn.local.user.find_one({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)
