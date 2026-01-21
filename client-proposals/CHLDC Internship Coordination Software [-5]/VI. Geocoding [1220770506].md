6\. Geocoding

  


Requirements

Geocoding is the process of looking up an address and getting precise GPS coordinates. All participants and work sites must be geocoded in order to allow displaying distance when picking a work site.

  


USER SPECIFICATION

From the administrative interface there will be a link to geocode both participant and work site addresses. 

  


The geocoding process is primarily an automated process, but must be initiated manually. Further, any addresses that fail to geocode automatically must be picked on a map manually. High quality, error-free address data is essential to allowing students to pick work sites by location.

  


Initial review of geocoding coverage will be performed upon receipt of initial files, if received.

  


Development Specification

Design questions

  * Geocoding process - interactive? What do we do with addresses that Google can't geocode?
    * Let's use an integration for this.
  * How do we notify students? With a batch process with email export?
  * Research Google maps place/point selection API.



  


[https://developers.google.com/maps/documentation/geocoding/intro](https://developers.google.com/maps/documentation/geocoding/intro)

[https://google-developers.appspot.com/maps/documentation/utils/geocoder/](https://google-developers.appspot.com/maps/documentation/utils/geocoder/)

  


  


    * Google has 2500 geocoding requests/day. - [https://developers.google.com/maps/documentation/geocoding/usage-limits](https://developers.google.com/maps/documentation/geocoding/usage-limits)
