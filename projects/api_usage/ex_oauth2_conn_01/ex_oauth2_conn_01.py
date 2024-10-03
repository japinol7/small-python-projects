import json
import os
from pathlib import Path

from requests import request

SECRETS_FOLDER = os.path.join(str(Path.home()), '.api_keys', 'ex_oauth2_conn_01_secrets')
SECRETS_FILE = os.path.join(SECRETS_FOLDER, 'ex_oauth2_conn_01_secrets.json')

URL_GET_DATA = "URL_OF_THE_API_YOU_WANT_TO_CONSUME"


def get_credentials():
    with open(SECRETS_FILE, 'r', encoding='utf-8') as in_file:
        return json.loads(in_file.read())


def get_access_token(credentials):
    data = {
        'grant_type': 'client_credentials',
        'scope': credentials['scope'],
        }
    auth = credentials['client_id'], credentials['client_secret']
    response = request('POST', credentials['token_url'], auth=auth, data=data)
    return response


def request_data(token_data):
    headers = {
        'Authorization':
            f"{token_data['token_type']} {token_data['access_token']}",
        'Content-Type': 'application/json',
        }
    response = request('GET', URL_GET_DATA, headers=headers)
    return response


def main():
    credentials = get_credentials()
    token_response = get_access_token(credentials)
    token_data = token_response.json()

    data = request_data(token_data)
    print(data.text)


if __name__ == '__main__':
    main()
