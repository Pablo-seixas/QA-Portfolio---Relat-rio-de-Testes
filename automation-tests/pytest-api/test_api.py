import requests

def test_jsonplaceholder():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert r.status_code == 200

def test_africa_countries():
    r = requests.get("https://restcountries.com/v3.1/region/africa")
    assert r.status_code == 200

def test_worldbank():
    r = requests.get("https://api.worldbank.org/v2/country/NGA?format=json")
    assert r.status_code == 200
