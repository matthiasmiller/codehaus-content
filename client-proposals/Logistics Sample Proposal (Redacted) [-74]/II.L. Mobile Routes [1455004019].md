2.12. Mobile Routes

  


Requirements

We will have a mobile-friendly interface for the routes. This was previously called "GPS" in the prior system.

  


The first screen will show a list of routes and the number of stops for the current day. For example:

  * Route A (12 stops)
  * Route B (0 stops)



  


When selecting a route, it will automatically jump to the first unfulfilled stop. It will show a link to go to the Previous Stop, Return to the Routes Screen, and the Next Stop.

  


When viewing a stop, it will show an interface such as:

  


STOP 1 of 1 \- Wednesday 1 - Test

  


Fred (Single-Family Home)

420 Main St, Anytown, ST 81212

  


Requested date: Aug. 19, 2020

Stop Length: 7 minutes

  


Items:

Recliner

  


Instructions:

Doorbell doesn't work; watch out for dog

  


Status: [Unfulfilled] [Save]

  


The "Unfulfilled" is a drop list for Status. Updating the status will automatically move to the next stop.

  


If there are no remaining stops for the current route, show a message that "This route has no more remaining stops." Show a link back to the Route's Warehouse address.

  


Development Specification

THIS WHOLE SECTION IS MATTHIAS

[ ] This will be a WSGI w/ OAuth

[ ] Probably just impersonate them

[ ] When updating the status, just go to the first unfulfilled stop again.
