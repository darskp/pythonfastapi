from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel,Field
from typing import Optional
from routers.users import router

app=FastAPI()
app.include_router(router)

class User(BaseModel):
    id:int=Field(gt=0)
    name:str
    email:str
    age:int
    is_active:bool

class UserCreate(BaseModel):
    name:str
    email:str
    age:int
    is_active:bool

class UserUpdate(BaseModel):
    name: str
    email: str
    age: int
    is_active: bool

class UserPatch(BaseModel):
    name: str | None=None
    email: str | None=None
    age: int | None=None
    is_active: bool | None=None

users=[]

@app.post("/users",status_code=201)
def create_user(user:UserCreate):
    new_user = User(
        id=len(users) + 1,
        name=user.name,
        email=user.email,
        age=user.age,
        is_active=user.is_active
    )

    users.append(new_user)

    return new_user

@app.get("/home",status_code=200)
def home():
    return {
        "message":"Hello World"
    }

@app.get("/users",status_code=200)
def get_users():
    return users

@app.get("/users/search")
def search_users(name:str="hi"):
    result=[]
    for user in users:
        if user.name.lower() == name.lower():
            result.append(user)
    return result


@app.get("/users/{user_id}",status_code=200)
def userbyid(user_id:int):
    for user in users:
        if user.id == user_id:
            return user
# Not found → 404
    raise HTTPException(
        status_code=404,
        detail="not found"
    )

@app.put("/users/{user_id}",status_code=200)
def update_user(user_id: int, user_update_data: UserUpdate):

    for user in users:
        if user.id == user_id:
            user.name = user_update_data.name
            user.email = user_update_data.email
            user.age = user_update_data.age
            user.is_active = user_update_data.is_active

            return {
                "message": "Updated Successfully",
                "data": user
            }

    # more filed to update then 
    # for user in users:
    #     if user.id == user_id:

    #         for field, value in user_update_data.model_dump().items():
    #             setattr(user, field, value)

    #         return {
    #             "message": "Updated Successfully",
    #             "data": user
    #         }
    # Not found → 404
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

@app.patch("/users/{user_id}",status_code=200)
async def patch_user(user_id:int,user_data:UserPatch):
    for user in users:
        if user_id == user.id:
            for field,value in user_data.model_dump(exclude_unset=True).items():
                setattr(user, field, value)
            return {
                "message": "Updated Successfully",
                "data": user
            }
    # Not found → 404
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
            

@app.delete("/users/{user_id}",status_code=200)
async def delete_user(user_id:int):
    for index,user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {
                "message": "User deleted Successfully",
                "id": user_id
            }

# Not found → 404
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
            
# Unexpected server error → 500
@app.get("/test")
def test():
    try:
        x=10/0
        return 0
    except ZeroDivisionError:
        raise HTTPException(
            status_code=500,
            detail="Cannot divide by zero"
        )




