import requests,json

image_url = 'https://masterkrasok.ru/upload/content/204/857da63ef2ad3f5c22104dccecd706984841058c.jpg'

response = requests.get(image_url)

with open('test.lpg', 'wb') as file:
    file.write(response.content)