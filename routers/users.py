from fastapi import APIRouter, HTTPException, status, Depends

from models.user import (
    User,
    UserCreate,
    UserPatch,
    RegisterUser,
    UserUpdate
)

from services.user_service import (
    create_user,
    get_all_users,
    search_users,
    get_user_by_id,
    update_user,
    patch_user,
    delete_user
)


router = APIRouter(prefix="/users")


@router.post("", status_code=status.HTTP_201_CREATED)
def create_user_route(user: UserCreate):
    return create_user(user)


@router.get("/home")
def home():
    return {
        "message": "Hello World"
    }


@router.get("")
def get_users():
    return get_all_users()


@router.get("/search")
def search_users_route(name: str = "hi"):
    return search_users(name)


# Unexpected server error → 500

@router.get("/test")
def test():

    try:
        x = 10 / 0
        return x

    except ZeroDivisionError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Cannot divide by zero"
        )


# Dependency Injection

def get_current_user() -> User:
    return User(
        id=1,
        name="John",
        email="john@example.com",
        age=24,
        is_active=True
    )


@router.get("/profile")
def profile(
    current_user: User = Depends(get_current_user)
):
    return {
        "user": current_user,
        "profile": []
    }


@router.get("/my-settings")
def mysettings(
    current_user: User = Depends(get_current_user)
):
    return {
        "user": current_user,
        "settings": []
    }


@router.post("/register")
def register_user(user: RegisterUser):
    return {
        "message": "User registered successfully",
        "name": user.name
    }


@router.get("/{user_id}")
def userbyid(user_id: int):

    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


@router.put("/{user_id}")
def update_user_route(
    user_id: int,
    user_update_data: UserUpdate
):

    user = update_user(
        user_id,
        user_update_data
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "message": "Updated Successfully",
        "data": user
    }


@router.patch("/{user_id}")
def patch_user_route(
    user_id: int,
    user_data: UserPatch
):

    user = patch_user(
        user_id,
        user_data
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "message": "Updated Successfully",
        "data": user
    }


@router.delete("/{user_id}")
def delete_user_route(user_id: int):

    deleted = delete_user(user_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "message": "User deleted Successfully",
        "id": user_id
    }

