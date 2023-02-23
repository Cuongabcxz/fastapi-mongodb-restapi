import string
import uuid
from typing import Optional
from pydantic import BaseModel, Field, validator, EmailStr, SecretStr


class User(BaseModel):
    id: Optional[str] = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    email: EmailStr
    password: SecretStr

    @validator("name", pre=True)
    def username_is_valid(cls, name: str) -> str:
        allowed = string.ascii_letters + string.digits + "-" + "_"
        assert all(char in allowed for char in name), "Invalid characters in username."
        assert len(name) >= 3, "Username must be 3 characters or more."
        return name

    @validator('password', always=True)
    def validate_password(cls, value):
        spec = "!@#$%&_="
        password = value.get_secret_value()

        min_length = 8
        if len(password) < min_length:
            raise ValueError('Password must be at least 8 characters long.')
        elif not any(password in spec for char in password):
            raise ValueError(f"Password must contain a special character of {spec}")

        return value

