import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
	
	'''Enter location:  Universitas Gadjah Mada
Retrieving http://py4e-data.dr-chuck.net/json?address=Universitas+Gadjah+Mada&key=42
Retrieved 2319 characters
{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "Bulaksumur",
                    "short_name": "Bulaksumur",
                    "types": [
                        "route"
                    ]
                },
                {
                    "long_name": "Caturtunggal",
                    "short_name": "Caturtunggal",
                    "types": [
                        "administrative_area_level_4",
                        "political"
                    ]
                },
                {
                    "long_name": "Kecamatan Depok",
                    "short_name": "Kec. Depok",
                    "types": [
                        "administrative_area_level_3",
                        "political"
                    ]
                },
                {
                    "long_name": "Kabupaten Sleman",
                    "short_name": "Kabupaten Sleman",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                },
                {
                    "long_name": "Daerah Istimewa Yogyakarta",
                    "short_name": "Jogja",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "Indonesia",
                    "short_name": "ID",
                    "types": [
                        "country",
                        "political"
                    ]
                },
                {
                    "long_name": "55281",
                    "short_name": "55281",
                    "types": [
                        "postal_code"
                    ]
                }
            ],
            "formatted_address": "Bulaksumur, Caturtunggal, Kec. Depok, Kabupaten Sleman, Daerah Istimewa Yogyakarta 55281, Indonesia",
            "geometry": {
                "location": {
                    "lat": -7.7713847,
                    "lng": 110.3774998
                },
                "location_type": "GEOMETRIC_CENTER",
                "viewport": {
                    "northeast": {
                        "lat": -7.770035719708497,
                        "lng": 110.3788487802915
                    },
                    "southwest": {
                        "lat": -7.772733680291502,
                        "lng": 110.3761508197085
                    }
                }
            },
            "place_id": "ChIJKZdy1LJZei4R5Pg0z197Taw",
            "plus_code": {
                "compound_code": "69HG+CX Caturtunggal, Sleman Regency, Special Region of Yogyakarta, Indonesia",
                "global_code": "6P4G69HG+CX"
            },
            "types": [
                "establishment",
                "point_of_interest",
                "university"
            ]
        }
    ],
    "status": "OK"
}
lat -7.7713847 lng 110.3774998
Bulaksumur, Caturtunggal, Kec. Depok, Kabupaten Sleman, Daerah Istimewa Yogyakarta 55281, Indonesia'''
