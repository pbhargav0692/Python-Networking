# Making a raw HTTP connection to Google API
    # 1) http.client
    # 2) json
    # 3) urllib
    # 4) quote_plus

import httplib
import json
from urllib import quote_plus
base = '/maps/api/geocode/json'


def geocode(address):
    path = '{}address = {}'.format(base, quote_plus(address))
    connection = httplib.HTTPConnection('maps.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.load(rawreply.decode('utf-8'))              # json.load - - > file like object containing json doc
                                                              # json.loads - - > string instance containing JSON document
    print(reply['results'][0]['geometry']['location'])


if __name__ == '__main__':
    geocode('513 Summit Ave, Arlington, TX')