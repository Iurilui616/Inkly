API_KEY = "AIzaSyDjC7bGJzEvrbSpSY7xujBIcRqzwF8nFKg"

import requests

url = f"https://api.exemplo.com/dados?key={API_KEY}"
response = requests.get(url)
print(response.json())
