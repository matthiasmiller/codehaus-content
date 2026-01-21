3.5. Configure Locations

  


Requirements

Overview: The database should track the location of a building prior it being delivered to a customer. Sometimes a dealer will have more than one lot on which they keep inventory and sell buildings. To keep track of building inventory by lot, and keep track of building location, Location records can be used. Once the building is on the customer's property, the corresponding address/coordinates would be used. 

  


Accessed via: Locations Report

  


Sections and Fields: 

Location section:

  * Active (checkbox; default to filled)
  * Location Name (required; plain text field; validate against duplicates)
  * Dealer (required; drop list of all active Dealer names) 
  * Address (required)
  * City (required)
  * State (required)
  * Zip Code (required)
  * Coordinates (optional; string field with validation that there are numbers on both sides of a comma; coordinates can be typed in or copied/pasted in)



  


Data Access: Admin Only 

  


Other Notes: 

  * There should be validation against deactivating Locations that have Buildings linked to them. 
  * CCI/CH would take care of importing these/doing the initial setup, based on information provided by BEB.



  


*Done.

  


Development Specification

This is a custom lookup record.

  


Coordinates: Add a macro called GPSCoordinatesError that makes sure the coordinates are in the format of "number,number". We should probably allow for spaces on either side of each of the numbers. 

  


TODO_CH: sql dump, then find out if there's something similar in the old system for importing...

(Per Tim, there is a lot code of some kind.)

Matthias Miller 10/27/2021: Waiting on SQL dump from Jason

Matthias Miller 11/10/2021: [https://github.com/yashsmehta/mysqldump-to-csv](https://github.com/yashsmehta/mysqldump-to-csv)

  


Mockup: 

[https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1770313489](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1770313489)
