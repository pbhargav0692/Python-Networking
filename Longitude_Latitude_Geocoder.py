# Google Provider - Geocoding API  - - - - - > Modules: 1) PyGeocoder(V 1.2.5) 2) Geocoder(V 1.7.5)
# finding LONGITUDE and LATITUDE of the physical location - 3939 Monroe Ave, Apt 125, Fremont CA 94536

from pygeocoder import Geocoder
if __name__ == '__main__':
    address = '513 Summit Ave, Apt 375, Arlinton, TX '
    print (Geocoder.geocode(address).coordinates)
