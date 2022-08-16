import requests

url = "https://face-detector-app123.herokuapp.com/myapi/"

payload={'Description': 'Gariel'}
files=[
  ('Picture',('photo-1494790108377-be9c29b29330.png',open('/Users/anindasharmaanik/Downloads/photo-1494790108377-be9c29b29330.png','rb'),'image/png'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)