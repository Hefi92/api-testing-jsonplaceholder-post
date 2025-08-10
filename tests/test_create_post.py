import pytest
import requests

url = "https://jsonplaceholder.typicode.com/posts"

def test_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    