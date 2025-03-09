import requests

url = "http://127.0.0.1:5001/predict"
files = {"file": open("test_image.jpeg", "rb")}

response = requests.post(url, files=files)
print(response.json())
