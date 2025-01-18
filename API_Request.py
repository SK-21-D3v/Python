import requests

def fetch_api_data():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]
        print("Name:", user['name']['first'], user['name']['last'])
        print("Gender:", user['gender'])
        print("Email:", user['email'])
    else:
        print("Failed to fetch data. Status code:", response.status_code)

fetch_api_data()
