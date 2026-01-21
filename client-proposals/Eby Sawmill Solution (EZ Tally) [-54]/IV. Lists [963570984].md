4\. Lists

  


Requirements

The EZ Tally Solution will include the following lists:

  


  * Counties (all counties from the states of PA, MD, VA, WV; non-editable simple list) 
  * Pulpwood Locations (user-editable simple list)
  * Flat Payment Subtype (non-editable simple list of the following:)
    * Date-Based
    * Start of Harvest
    * Mid Harvest
    * End of Harvest



  


Development Specification

Mockup: N/A

  


Counties Work

Assign to Niccolas to work with Ellis.

  * Get all of the county names from [https://www.wikidata.org/wiki/Wikidata:Lists/US_counties](https://www.wikidata.org/wiki/Wikidata:Lists/US_counties) or similar
  * Set up input file with columns for "Reno County, KS"   "Reno"   "KS"  
  * Create an "Std Import Counties.x30" in std components to import these to create the shipped lookup records.
  * Move all of the counties from "Counties - PA.txt" to a "Counties.txt"



BID: 4 hours

  


  * Add a LimitCountyStates list that can be populated with "PA" to limit to only PA counties, etc.
  * Add a restricted data rule to respect LimitCountyStates list. If this list is blank, we allow all counties.



BID: 2 Hours

  


  * Change the FB catalog(s) to limit to PA. This should be tested in a separate job. 
  * TO DO before coding: Ask FB If they need ability to add to counties. If so, we can change the list to user-changable in their system.
  * Document in a Counties living spec how to configure counties and how to import these if needed.



BID: 4 hours

  


PulpwoodLocations

Free.
