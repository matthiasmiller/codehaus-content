3\. Administrative interface overview

  


Requirements

Besides the participant-facing website for work site selection, the software will present an administrative interface to allow CHLDC staff to manage the approval process and understand the current participation situation.

  


  


USER SPECIFICATION

The interface will give options for:

  


Matching   Approve Participant Choices   Participants Without Choice   Matching Results   Participation Rate Graph  
| Participants   Participant Search   View All Participants   Import Participants| Work Sites   View All Work Sites   Sites With No Participants   Full/Overbooked Sites   Import Work Sites  
  
---|---|---  
Geocoding   Geocode Locations  
| Programs   View Programs| Documentation   Wiki  
  
  


These options are covered in the sections below.

  


Each of the reports described below will provide access to the underlying "detail page" of the record, including all fields and information imported from YEPS and entered by the participant in the participant-facing website.

  


Development Specification

Fields to be added:

  


Programs (new record type)

  * Name
  * Active?
  * Notes (memo)



  


Participants (contacts)

  * YEPS ID
  * RG of Programs
    * Each program has first, second, third choice, with date/times for each. Also actual approved work site.
    * Also, date/time of approval, so that we can see how long it took to approve them.
  * Organizations to hide (maybe - if the student says that they no longer want a work site, we could hide it from them in the future. This is probably a bad idea.)
  * Secret ID (random string)
  * GPS coordinates
  * OnChange button to clear choices (admin-only.)



  


Work sites (organizations)

  * YEPS ID
  * RG of Programs
    * Only one active
  * # of slots
    * Job title for each slot - validate against pipes (nuke them on import)
  * Public notes (multi-line text)
  * Category / industry (list)
  * GPS coordinates
  * Exclusive site?
    * List of allowed participants


