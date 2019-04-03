import requests
response = requests.get('https://httpbin.org/ip')
print(f"your ip is {response.json().get('origin')}")
