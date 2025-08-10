import pytest 
import requests

def tests_api_status_code():
  url = "https://jsonplaceholder.typicode.com/posts"
  
  response = requests.get(url)
  assert response.status_code == 200
