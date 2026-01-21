27.15. Expanded Lumber Grade Record Feature

  


Requirements

Sean Miller 04/29/2025: Moved to [[[IN11433](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11435&)]] - ZGW - Expanded Lumber Grade Record Feature

  


  


Configuration record & report: The Lumber Grades list previously was specced as a configuration record + report, to allow deactivation of items. This is now split out as an optional add-on to help give more opportunities to reduce cost.

  


Estimated Cost: Approx. $1,350 

  


Spec:

  


Part 1: 

  


Overview: The Lumber Grade record is a custom record, and is used to track various lumber grades that GemWood and their Buyers use to rate the quality of lumber.

  


Accessed via: Configure Grades Report

  


Sections and Fields: 

  * Lumber Grade section:
    * Active (checkbox; default to checked; validate against deactivating one or more non-Closed Delivery Ticket reference the Lumber Grade record)
    * Grade Name/Code (required; plain text field; validates against duplicate Grade Names)
    * Restricted to Buyers (checkbox + conditionally-visible multi-select drop list; if the checkbox is checked, a multi-select list of all active Buyer-type Contacts is displayed, with at least one selection required; if one or more Buyers are selected, the Grade is only available for those; if no Buyers are selected, the Grade is available for all Buyers) 



  


Data Access: 

  * Visibility: Visible to all users
  * Editability: Editable for users with the "Edit GemWood general configuration records" Permission.
    * Note: A separate "Create GemWood Configuration records" Permission could be added to prevent certain users from creating these, but this is not included in Phase 1 to help keep things simple. 



  


Special Considerations: 

  * Copy Record: N/A (disallowed)
  * Delete Record: Allow deletion until the record has been referenced by another record, then disallow. 
  * Merge Record: N/A (disallowed)



  


Other Notes:

  * All Lumber Grade records are set up manually in the Solution, by GemWood with assistance from CCI as needed. Following is a standard/default list that can be used as a reference:
    * FAS (stands for "First and Second"; a plain sawn grade)
    * F1F (stands for "One Face"; FAS on one side of the board, with the other side of the board being lower quality; usually priced like FAS but some buyers pay less; a plain sawn grade)
    * 1C (stands for "1 Common"; highest grade of "common" lumber; a plain sawn grade) 
    * 2C (stands for "2 Common"; middle grade of "common" lumber; a plain sawn grade) 
    * 3C (stands for "3 Common"; lowest grade of "common" lumber; a plain sawn grade) 
    * Rift (highest-value product on the market)
    * Quartered (priced like FAS most of the time)
    * Rustic (essentially ungraded lumber with knotty character; pays more than what it would grade as): 
    * Veneer (separate grade all by itself): 
  * Other grades could include the following:
    * FAS 8-9 
    * Rift / Quartered
    * Select
  * Lumber Grades are sorted in alphabetical order throughout the Solution. If an alternate sorting sequence is desired at some point, a "Sort Order" field could be added to the Lumber Grade record to give full control to sorting.
  * Note that this record includes a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup:[https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1157580638#gid=1157580638](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1157580638#gid=1157580638)

Tim Reitz 12/17/2024: Updated. 

  


  


Ellis Miller 12/16/2024:

[ ] BD: Lookup record: LumberGrade (GradeName is a list)

[ ] BD: Restricted to Buyers checkbox

[ ] BD: Restricted to Buyers hidden RG with single Contacts field, no validation

[ ] USA: Restricted to Buyers Entry droplist:

[ ] uses a helper list of all active. Use ActiveContactsByTypesNdxConcat.

[ ] Populate the hidden RG with the multi-select. See other examples of multi-select on how to do this. 1 hour

[ ] USA: Add an ActiveLumberGradesForBuyers.ndx with a BinString(BuyerListNum)+BinString(LumberGrade). For records that don't have Buyer Restrictions, use BinString(NA)+BinString(LumberGrade), for other records, Repeat on the RG. You probably need to make this a Repeat For List ndx.

[ ] USA: add an ActiveLumberGradesForBuyer(vBuyer) function that calls ActiveLumberGradesForBuyers(BinString(NA)+...) and ActiveLumberGradesForBuyers(BinString(vBuyer)+"...) and sorts the results.

  


BD: 3 HOURS

USA: 6 HOURS
