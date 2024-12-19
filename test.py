import requests

url = "http://127.0.0.1:5000/upload"
file_path = "C:\\Users\\namit\\Desktop\\ocr.py"


with open(file_path, 'rb') as file:
    response = requests.post(url, files={'file': file})

print(response.json())  
