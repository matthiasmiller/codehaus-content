24.7. Devices: Improvements for Managing SIM Cards

  


Requirements

*Done. 

  


The following items could be done as enhancements to the way <Service Name> interacts with Hologram: 

  


  * Consider whether the "Manage SIM Card" link can pass through the "ICCID" for the current Device when a user clicks the link. 



  


  * Consider direct integration between Silverloom and Hologram via API. This could allow SIM cards to be managed more completely from Silverloom, without the need to log into the Hologram account as frequently. This could involve setting all of the necessary details for SIM card management from Silverloom.



  


Development Specification

Tim Reitz 12/16/2025: There is an API for Hologram: [https://docs.hologram.io/api/v1](https://docs.hologram.io/api/v1). How easy does it look like it would be to manage SIMs from Silverloom? (this likely would be a Phase 2 or later item) 

Tim Reitz 12/18/2025: If we do this, we'd want to add fielding in Silverloom for the Hologram "Organization", etc. 

  


Tim Reitz 01/13/2026: Also for API integration: 

  * Monthly Limit (MB) (required; number; 1 decimal place; Hologram gives the option of having a limit on how much data is sent per month)



_BR: Tim Reitz 12/15/2025: Is this MB or GB?

_VA: Tim Reitz 12/16/2025: Can be set to KB, MB, or GB. Probably just go with MB? Or have a UOM field to make a choice here in Silverloom??

Tim Reitz 01/13/2026: Just going with MB for now.
