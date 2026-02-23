import requests

api_key = "sk-abc123456"

def get_data():
    r = requests.get("https://api.example.com/data")
    return r.json()

def risky():
    try:
        get_data()
    except:
        pass# triggered
