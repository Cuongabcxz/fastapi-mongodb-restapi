from fastapi import FastAPI
from view.view_user import view_user

app = FastAPI()

app.include_router(view_user)
