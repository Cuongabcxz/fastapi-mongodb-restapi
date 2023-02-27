from fastapi import FastAPI

app = FastAPI()


app.include_router(user, prefix="/user")
