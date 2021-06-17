import requests

url = "https://universities-and-colleges.p.rapidapi.com/universities"

querystring = {"page": "1", "includeUniversityDetails": "true", "countryCode": "US", "limit": "50", "state": "true",
               "website": "true"}

headers = {
    'x-RapidAPI-Key': "7060fafea1mshc1031ccdb460c56p1e6e83jsnc95eba373c88",
    'x-RapidAPI-Host': "universities-and-colleges.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
list = response.json()

for item in list:
    print(item["name"], item["countryCode"], item["state"], item["website"])
