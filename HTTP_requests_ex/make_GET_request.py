from requests import get

url = "https://icanhazdadjoke.com"

response = get(url, headers={"Accept": "application/json"})

dad_text = response.text

dad_json = response.json()

# print(response.text)
# print(response.json())

print(dad_json)
