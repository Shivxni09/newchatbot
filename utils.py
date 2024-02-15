import openai
from openai import OpenAI
import os


def get_initial_message():
    messages = [
        {"role": "system", "content": "You are a helpful AI Tutor. Who anwers brief questions about AI."},
        {"role": "user", "content": "I want to learn AI"},
        {"role": "assistant", "content": "Thats awesome, what do you want to know aboout AI"}
    ]
    return messages


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content


def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
