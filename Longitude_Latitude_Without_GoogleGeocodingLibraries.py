# If google provider API library is not available, We can fetch JSON document from the google Geocoding API

import requests
def geocode(address):
    parameters = {'address': address}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print (answer['results'][0]['geometry']['location'])  # with [0] being the first object in the array (the result)
if __name__ == '__main__':
    geocode('513 Summit Ave, Apt 375, Arlington, TX')

