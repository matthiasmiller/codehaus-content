27.14. Expanded Species Record Feature

  


Requirements

Sean Miller 04/29/2025: Moved to [[[IN11432](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11434&)]] - ZGW - Expanded Species Record Feature

  


  


Configuration record & report: The Species list previously was specced as a configuration record + report, to allow deactivation of items. This is now split out as an optional add-on to help give more opportunities to reduce cost.

  


Estimated Cost: Approx. $750 

  


Spec:

  


Part 1: 

  


Overview: The Species record is a custom record, and is used to track various wood species that are used in the Solution.

  


Accessed via: Configure Species Report

  


Sections and Fields: 

  * Species section:
    * Active (checkbox; default to checked; validate against deactivating if one or more non-Closed Delivery Tickets reference the Species record)
    * Name (auto-set and read-only; displays the Short Code and Description in the following format: "<Short Code> \- <Description>"; this is the name used in drop lists throughout the Solution)
    * Short Code (required; plain text field; validate against duplicate Short Codes; cannot contain hyphens)
    * Description (required; plain text field; used to document the full species name; validate against duplicate Descriptions)



  


Data Access: 

  * Visibility: Visible to all users
  * Editability: Editable for users with the "Edit GemWood general configuration records" Permission.
    * Note: A separate "Create GemWood Configuration records" Permission could be added to prevent certain users from creating these, but this is not included in Phase 1 to help keep things simple. 



  


Special Considerations: 

  * Copy Record: N/A (disallowed)
  * Delete Record: Allow deletion until the record has been referenced by another record, then disallow. 
  * Merge Record: N/A (disallowed)



  


Other Notes:

  * All Species records are set up manually in the Solution, by GemWood with assistance from CCI as needed. Following is a standard/default list that can be used as a reference:
    * BE ("Beech")
    * HK ("Hickory")
    * HM ("Hard Maple")
    * POP ("Poplar")
    * RO ("Red Oak")
    * SM ("Soft Maple")
    * WA ("Walnut")
    * WO ("White Oak")
  * Note that this record includes a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup:[https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1387629134#gid=1387629134](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1387629134#gid=1387629134) 

Tim Reitz 12/17/2024: Updated. 

  


  


Ellis Miller 12/16/2024:

[ ] Lookup record (Species, SpeciesName is the list field)

[ ] Add validation against duplicate ShortCode and duplicate Description.

[ ] Add OnChanges to both ShortCode and Description with Concat(" \- "...)

BID: 4 HOURS
