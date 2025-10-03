from src.repositories.user import get_user_by_id, create_user

def get_user(user_id: str):
    user = get_user_by_id(user_id)

    if not user:
        create_user(user_id)

        user = get_user_by_id(user_id)

    return user
