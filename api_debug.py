import requests

url = "https://jsonplaceholder.typicode.com/invalid"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 404:
    print("Error: API endpoint not found")
else:
    print("API Request Successful")
