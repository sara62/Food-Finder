import requests, json
from urllib import urlencode

APIKey = ''

DISTANCE_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'

def calcDistance(origins, destinations, **args):
    args.update  ({
        'origins' : origins,
        'destinations' : destinations,
        'key' : APIKey
    })

    url = DISTANCE_URL + '?' +  urlencode(args)
    response = requests.get(url)
    data = json.loads(response.text)
    print(data['rows'][0]['elements'][0]['distance']['value'])
