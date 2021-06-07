import requests

# url = "https://api.data.gov/ed/collegescorecard/v1/schools"
# url = "https://developer.nrel.gov/api/collegescorecard/v1/schools"

url = "https://api.data.gov/ed/collegescorecard/v1/schools?_per_page=100&_page={page}&" \
      "api_key=9o9cbIMIYKRe90jn29mhBTS1AZXbCvyLf0EygeES&" \
      "fields=school.name,school.city,school.state,school.zip,school.carnegie_size_setting,school.school_url,school.carnegie_basic,school.locale,school.region_id,school.ownership,school.carnegie_undergrad"

# print(url.replace("{page}", "11"))

for page in range(68):
    print('Reading page #' + str(page))
    response = requests.request("GET", url.replace("{page}", str(page)))
    with open('school-' + str(page) + '.json', 'w') as f:
        print(response.text, file=f)


# with open('page1.json', 'w') as f:
#     print('here goes page 111', file=f)

#
# response = requests.request("GET", url)
# print(response.text)