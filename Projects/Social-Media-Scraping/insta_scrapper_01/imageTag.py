import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": "Bearer hf_XXXXXXXXXX"}

def query(filename):
	with open(filename, "rb") as f:
		data = f.read()
	response = requests.post(API_URL, headers=headers, data=data)
	return response.json()