import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_user(user_id):
    url = f"{BASE_URL}/users/{user_id}"

    response = requests.get(url)

    return response


def get_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"

    response = requests.get(url)

    return response


def create_post(payload):
    url = f"{BASE_URL}/posts"

    response = requests.post(
        url,
        json=payload
    )

    return response

def update_post(post_id, payload):
    url = f"{BASE_URL}/posts/{post_id}" 

    response = requests.put(url, json =payload)

    return response


def delete_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}"

    response = requests.delete(url)

    return response