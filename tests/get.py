import pytest 
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
assert response.status_code == 200