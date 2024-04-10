# import requests
# from app.core.config import settings
import time
import random


def generate_openai_prompt(prompt: str) -> str:
    """
    Simple client for OpenAi Api request
    """
    # massages = [
    #     {
    #         'role': 'user',
    #         'content': prompt,
    #     }
    # ]
    # with requests.Session() as session:
    #     response = session.post(
    #         url=settings.OPENAI_URL,
    #         json={
    #             'model': 'gpt-4',
    #             'messages': massages,
    #         },
    #         headers={'Authorization': f'Bearer {settings.OPENAI_TOKEN}'},
    #         timeout=15 * 60,
    #     )
    #     result = response.json()

    # return result['choices'][0]['message']['content']

    time.sleep(10)
    return f"answer: {random.randint(0, 10)}"

