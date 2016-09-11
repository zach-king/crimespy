import requests, json
from pprint import pprint

url = "https://data.police.uk/api/crimes-street/all-crime"
latitude = 34.7234103
longitude = -92.33604129999999
date = '2016-1'


url += '?lat=52.408056&lng=-1.510556&date=2016-1'

response = requests.get(url)
data = response.json()
    
# parsing the json data
for crime in data:
    # with open('response.json', 'w') as f:
    #     f.write(str(data))
    if crime['category'] != 'shoplifting':
        continue
    print('-' * 100)
    print(crime)
