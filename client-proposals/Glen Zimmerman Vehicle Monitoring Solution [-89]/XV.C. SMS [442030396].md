14.3. SMS

  


Requirements

TODO_VA: Tim Reitz 01/17/2026: We need to look at this. Will we simply rely on Traccar to send the SMS messages? 

  


_GZ: Tim Reitz 01/17/2026: What are the text messages that you want to send? 

TODO_VA: Tim Reitz 01/23/2026: Discussed with Glen today. He said that until we know for sure that Traccar can send all the texts that they way, let's hold off on adding things to Silverloom. He'd prefer to not duplicate things.

Probably hold off on this until Phase 2 or beyond. 

  


HLD notes: 

Add a "LOCATE" keyword that:

  * Lists all vehicles with the latest reverse-geocoded address and speed



  


It would send back a text message along the lines of:

  


1\. White 2023 Dodge RAM - 123 Main Street, Philadelphia, PA - 43 MPH - as of 12:44 PM

  


2\. Red 1976 Ford Mustang - Elk Garden, WV - 83 MPH - as of 3:10 PM

  


This requires additional design during our in-depth design process to ensure that we have appropriate cost/benefit.

  


Development Specification

TODO_VA: - We need to figure out if the cost/benefit is actually worth it here. We'll have to have a way to request a geocode of locations

  


Two approaches:

  * Have a WSGI handling the inbound SMS. This is probably the easiest.
  * If we wanted to avoid reverse geocoding, we could give a general direction (i.e. X miles n/ne/e/se/s/sw/w/nw of CITY NAME, ST). This would use "as the crow flies" calculations to determine the closest town, then calculate rough direction using an angle calculation (i.e. -22.5 to +22.5 = north, +22.5 to +67.5 = northeast, +67.5 to +112.5 = east, etc).


