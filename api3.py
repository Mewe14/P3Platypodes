import requests

# url = "https://api.data.gov/ed/collegescorecard/v1/schools"
url = "https://developer.nrel.gov/api/collegescorecard/v1/schools"

# querystring = {"page": "5", "includeUniversityDetails": "false", "countryCode": "US", "limit": "50"}

headers = {
    'x-Api-Key': "HiLqtF9KVhmYDv91ckwwPCN2i5jje4n9rBFWO9CG",
    'x-API-Host': "https://developer.nrel.gov"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
list = response.json()

