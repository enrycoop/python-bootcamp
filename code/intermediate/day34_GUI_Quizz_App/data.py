import requests

url = "https://opentdb.com/api.php"
params = {
    "amount": 10,
    "category": 17,
    "difficulty": "easy",
    "type": "boolean"
}

response = requests.get(url=url, params=params)
if response.status_code == 200:
    question_data = response.json()["results"]
