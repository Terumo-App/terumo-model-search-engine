import requests
import base64




url = "http://localhost:5003/attribute-query"

data = {"data": 1 }

headers = {"Content-Type": "application/json"}
print("Sending request for model...")
print(f"Data: {data}")
r = requests.post(url, json=data, headers=headers)
print(f"Response: {r.text}")
print(f"Response: {r.status_code}")
