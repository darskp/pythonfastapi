from fastapi import HTTPException, Depends

users = {}

def create_user(user):
    users[user.username]={
        "age":user.age,
        "email":user.email
    }
    return {
        "username":user.username,
        "age":user.age,
        "email":user.email
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

def get_app_user():
    return {
        "username": "darshan",
        "role": "admin"
    }

def get_profile(user):
    return {
        "message": "Profile loaded",
        "user": user
    }

def get_order(user):
    return {
        "message": "Order loaded",
        "user": user
    }

def admin_page(user):
    return{
        "message": "Admin Page",
        "user": user
    }