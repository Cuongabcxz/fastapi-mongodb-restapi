import string
import uuid
from pydantic import BaseModel, Field, validator, EmailStr


def generate_uuid():
    return str(uuid.uuid4())


class User(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    name: str = Field(...)
    email: EmailStr
    password: str

    @validator("name", pre=True)
    def username_is_valid(cls, name: str) -> str:
        allowed = string.ascii_letters + string.digits + "-" + "_"
        assert all(char in allowed for char in name), "Invalid characters in username."
        assert len(name) >= 3, "Username must be 3 characters or more."
        return name




