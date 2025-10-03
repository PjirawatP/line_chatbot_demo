from ollama import chat, ChatResponse

from src.services.conversation import get_recent_conversation


def chatbot_response(user_id, user_message):
    recent_conversation = get_recent_conversation(user_id)

    system_prompt = """
        You are a helpful AI assistant. Your job is to continue conversations naturally, stay consistent with the context, and respond in the same language as the user. 
        - If the user asks a direct question → answer clearly.
        - If they continue a previous topic → respond with context.
        - If there is no conversation history → treat it as a new conversation.
        - Keep responses concise unless the user requests detail.
    """

    user_prompt = f"""
        ### Conversation History:
        {recent_conversation}

        ### New User Message:
        {user_message}
    """

    response: ChatResponse = chat(model="llama3.2", messages = [
        {
            "role": "system",
            "content": system_prompt 
        },
        {
            "role": "user",
            "content": user_prompt 
        }
    ])

    return response["message"]["content"]