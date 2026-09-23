from fastapi import HTTPException, Depends
from utils.security import hash_password,verify_password, create_access_token

users = {}


# def create_user(user):
#     users[user.username]={
#         "age":user.age,
#         "email":user.email
#     }
#     return {
#         "username":user.username,
#         "age":user.age,
#         "email":user.email
#     }

def create_user(user):
    users[user.username] = {
        "age": user.age,
        "email": user.email,
        "password": hash_password(user.password),
        "role": user.role
    }

    return {
        "username": user.username,
        "age": user.age,
        "email": user.email,
        "role": user.role
    }

def get_user(username):
    if username not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return users[username]

def get_all_users():
    return [
        {
            "username":username,
            **user
        }
        for username, user in users.items()
    ]

def update_user(username,user):
    if username not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    users[username]={
        "age":user.age,
        "email":user.email
    }
    return{
        "username": username,
        "age": user.age,
        "email": user.email
    }

def delete_user(username):
    if username not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    deleted_user = users.pop(username)

    return {
        "username": username,
        "age": deleted_user["age"],
        "email": deleted_user["email"]
    }


def admin_page(user):
    return{
        "message": "Admin Page",
        "user": user
    }

def login_user(login_data):
    if login_data.username not in users:
        raise HTTPException(
            status_code = 401,
            detail="Invalid username or password"
        )
    user=users[login_data.username]

    if not verify_password(login_data.password,user["password"]):
        raise HTTPException(
            status_code = 401,
            detail="Invalid username or password"
        )
    
    return{
       "access_token":create_access_token(
        login_data.username,
        user["role"]
       ),
       "token_type":"bearer"
    }

