from services.ai_agent import generate_suggestions
from config.db import chats_collection


def chat_with_agent(user_id, message, resume_text=None, job_description=None):
    # fetch previous chats
    history = list(chats_collection.find({"user_id": user_id}))

    conversation = ""
    for chat in history:
        conversation += f"{chat['role']}: {chat['content']}\n"

    context = ""
    if resume_text:
        context += f"\nResume:\n{resume_text}\n"
    if job_description:
        context += f"\nJob Description:\n{job_description}\n"

    prompt = f"""
    You are a career assistant AI.

    Context:
    {context}

    Conversation:
    {conversation}

    User: {message}
    """

    response = generate_suggestions(prompt, job_description or "")

    # save chat
    chats_collection.insert_many([
        {"user_id": user_id, "role": "user", "content": message},
        {"user_id": user_id, "role": "assistant", "content": response}
    ])

    return response