import requests

response_API = requests.get(
    "https://webhook.site/a891e4dc-4056-4d80-8e9a-88e06d98ecd9/"
)
print(response_API.status_code)

url = "https://webhook.site/a891e4dc-4056-4d80-8e9a-88e06d98ecd9/data/"

payload = "{'5','-5','4','3','7','2'}"
response = requests.request("PUT", url, data=payload)

print(response.text)

'''"'5','-5','4','3','7','2'"'''
