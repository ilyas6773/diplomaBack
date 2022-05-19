from urllib import response
import requests
import json

BASE = "http://127.0.0.1:5000"

response = requests.get(BASE + "/house/1")
print(response.json())
