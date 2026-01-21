3\. Add Choice to Cancel Collision Coverage During Transfer

  


Requirements

In the vehicle transfer process, there should be a way to say whether or not the buyer wants to have Collision coverage or not. 

  


Design: 

  * In the gray space of the Transfer in-screen prompt, add a new prompt above "New Collision Coverage" called "Collision Coverage for New Owner?" (Yes/No drop list; default to blank) 
  * Default "New Collision Coverage" to blank.  
  * Use OnChanges to blank out the "New Collision Coverage" amount on No, or default to prior amount on Yes, or blank when "Collision Coverage for New Owner?" is blank. 
  * "New Collision Coverage" amount should be read-only if "Collision Coverage for New Owner?" is No or blank. 
  * All fields should reset with "Cancel Transfer". 



  


T&M Estimate: $200-300

  


Development Specification

See (in MYS): [[[IN5156](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-5158&)]] - ZWA - Add Choice to Cancel Collision Coverage During Transfer (T&M)
