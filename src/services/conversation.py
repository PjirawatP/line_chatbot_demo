from src.repositories.conversation import get_recent_conversation_by_user_id, save_conversation_by_user_id


def get_recent_conversation(user_id: str):
    return get_recent_conversation_by_user_id(user_id)


def save_conversation(user_id: str, query_message: str, response_message: str):
    return save_conversation_by_user_id(user_id, query_message, response_message)
