from fastapi import APIRouter, Depends
from services.user_service import create_user, get_user,get_all_users,update_user,delete_user,get_profile,get_app_user,get_order,admin_page,login_user
from models.user import User, UserResponse, LoginRequest, LoginResponse

router = APIRouter()

@router.post("/users", status_code=201,response_model=UserResponse)
def create_user_route(user:User):
    return create_user(user)

@router.get("/users",response_model=list[UserResponse])
def get_all_users_route():
    return get_all_users()

@router.get("/users/{username}")
def get_user_route(username:str):
    return get_user(username)

@router.put("/users/{username}",response_model=UserResponse)
def update_user_route(user:User,username:str,):
    return update_user(username,user)

@router.delete("/users/{username}",response_model=UserResponse)
def delete_user_route(username:str):
    return delete_user(username)

@router.get("/test-500")
def test_500():
    number = 10
    result = number / 0
    return {"result": result}

@router.get("/profile")
def get_user_profile(user = Depends(get_app_user)):
    return get_profile(user)

@router.get("/order")
def get_user_order(user = Depends(get_app_user)):
    return get_order(user)

@router.get("/admin")
def admin_get_page(user=Depends(get_app_user)):
    return admin_page(user)

@router.post("/login",response_model=LoginResponse)
def login(login_data:LoginRequest):
    return login_user(login_data)