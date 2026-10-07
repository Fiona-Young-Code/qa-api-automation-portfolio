

from api_client import get_post, create_post, update_post, delete_post

def test_get_post_success():
    response = get_post(1)
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


def test_create_post_success():
    payload = {
        "title": "QA automation test",
        "body": "Reviewing API testing",
        "userID":1
    }
    response = create_post(payload)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userID"] == payload["userID"]
    assert "id" in data


def test_update_post_success():
   payload = {
        "title": "Update QA automation test",
        "body": "Update content",
        "userId":1
    }
   response = update_post(1, payload)
   data = response.json() 
   print(data)

   assert response.status_code == 200
   assert data["id"] == 1
   assert data["title"] == payload["title"]
   assert data["body"] == payload["body"]
   assert data["userId"] == payload["userId"]


def test_delete_post_success():
    response = delete_post(1)

    assert response.status_code == 200