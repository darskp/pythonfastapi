from models.user import User, UserCreate, UserPatch, UserUpdate

users = []


def create_user(user: UserCreate):
    new_user = User(
        id=len(users) + 1,
        name=user.name,
        email=user.email,
        age=user.age,
        is_active=user.is_active
    )

    users.append(new_user)

    return new_user


def get_all_users():
    return users


def search_users(name: str):
    result = []

    for user in users:
        if user.name.lower() == name.lower():
            result.append(user)

    return result


def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user

    return None


def update_user(user_id: int, user_update_data: UserUpdate):

    for user in users:
        if user.id == user_id:

            user.name = user_update_data.name
            user.email = user_update_data.email
            user.age = user_update_data.age
            user.is_active = user_update_data.is_active

            return user

    return None


def patch_user(user_id: int, user_data: UserPatch):

    for user in users:
        if user.id == user_id:

            for field, value in user_data.model_dump(
                exclude_unset=True
            ).items():
                setattr(user, field, value)

            return user

    return None


def delete_user(user_id: int):

    for index, user in enumerate(users):

        if user.id == user_id:
            users.pop(index)
            return True

    return False