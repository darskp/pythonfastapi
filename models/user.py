from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(min_length=3, max_length=500)
    age: int = Field(gt=0, le=120)
    email: str | None = None
    password:str
    role:str="user"

class LoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    age: int
    email: str | None = None
    role: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str