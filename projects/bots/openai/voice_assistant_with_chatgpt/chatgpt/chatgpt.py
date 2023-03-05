import requests
import json


class ChatgptError(Exception):
    pass


def get_chatgpt_answer(message, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        'Authorization': f"Bearer {api_key}",
        'Content-Type': 'application/json'
        }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'user', 'content': message}
            ]
        }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_json = response.json()
        answer = response_json['choices'][0]['message']['content']
    except Exception as e:
        raise ChatgptError(f"Error processing chatgpt answer! Msg: {e}")

    return answer


if __name__ == '__main__':
    from config.config import OPENAI_API_KEY_FILE
    from tools.utils import utils

    res = get_chatgpt_answer("Please, print the first 15 prime numbers "
                             "and a Python program to generate them.",
                             api_key=utils.read_file_as_string(OPENAI_API_KEY_FILE))
    print(res)
