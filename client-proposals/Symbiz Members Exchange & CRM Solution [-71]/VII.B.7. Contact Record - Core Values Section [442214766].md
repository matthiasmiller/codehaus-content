7.2.7. Contact Record - Core Values Section

  


Requirements

  * Core Values custom section (visible if Contact Type = Member; visible to and editable for the corresponding Member and all his uplines): 
    * Core Values Instructions (auto-set and read-only; from AppHosting.zone settings)
    * Embedded spreadsheet with the following:
      * Columns: 
        * Core Values Word (required; smaller plain text field; error message on Save: "Core Values Word is blank.") 
        * Core Values Description (required; longer plain text field; error message on Save: "Core Values Description is blank.") 
      * Automatically sorted by: N/A 
      * Buttons to insert/append/remove rows ("Insert"/"Append"/"Delete")
      * Buttons to move rows up and down (up/down arrows) 
      * Show 6 rows without scrolling
    * Other Notes: 
      * This table is limited to 6 rows, to prevent entering too many words (see validation note below). 
    * Additional Validations:
      * A minimum of one Core Value must be specified: Warning message on Save if none exists: "At least one Core Value is needed."
      * A maximum of 6 Core Values may be specified: Error message on Save if there are more than 6: "No more than 6 Core Values may be set. Remove items as needed to get to a maximum of 6."



  


Development Specification

Change Requests: 

  * Tim Reitz 04/09/2024: [[[IN9565](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9567&)]] - ZSB - Contact Record - Clarify Visibility & Editability
  * 


  


  


BID: 2 HOURS
