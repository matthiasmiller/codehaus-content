11.1.4. SPE Record

  


Requirements

Overview: A SPE (Special Purpose Entity) is a shell business that provides simplified access for businesses and individual to Pennsylvania's tax credit system.

  


Accessed via: Advanced | Configuration | Configure SPEs

  


Sections and Fields: 

  * SPE section: 
    * Name (required; plain text; defaults to blank; validate against duplicates)
    * Legal Name (optional; plain text; defaults to blank)
    * Legal Address (optional; plain text; defaults to blank)
    * Legal Address Line 2 (no label; optional; plain text; defaults to blank)
    * City (optional; plain text; defaults to blank)
    * State (no label; optional; drop-list of state abbreviations; defaults to PA)
    * Zip (no label; optional; plain text; defaults to blank)
    * EIN (optional; number; auto-formats "xx-xxxxxxx"; defaults to blank; with the following validations: 
      * Error on the field if the EIN is not 9 digits long: "The EIN should be 9 digits long."; 
      * Error on the field if the EIN contains any characters other than digits and dashes: "Invalid EIN.") 
    * Bank Account # (optional; plain text; visible to and editable for users with the "Can view saved sensitive data" Permission; defaults to blank) 
    * Sort Order (optional; number field; used to sort SPEs in the Configure SPE Report; defaults to blank; validation error on the field if the Sort Order number is lower than 0 or higher than 999: "Sort Order must be between 0 and 999.") 
    * Active Date (optional; date; defaults to blank)
    * Inactive (checkbox; when checked, sets the "Inactive Date" to the current date, when unchecked, clears the "Inactive Date") 
    * Inactive Date (no label; date; read-only) 
    * Linked Business (optional; drop-list of all business-type Contacts) 



TODO_TR: Tim Reitz 02/24/2025: Does this include inactive, or just active? 

Austin Priest 02/25/2025: The list includes all business-type contacts including incactive.

  * View SPE Applications (link; opens in new tab, SPE Applications report with the SPE filter set to the current SPE record)  
  * View SPE Members (link, opens in new tab, Members of <SPE> report with the SPE filter set to the current SPE record)



  


Modification History: This contains the following custom features for modification tracking: 

  * Modification History (link to open the report for the record)
  * Note that Bank Account details will be restricted in Activity History as well, based on the "Can view saved sensitive data" permission.



  


Data Access: 

  * TODO_NM: Tim Reitz 02/14/2025: Who can access? 



  


Other Notes: 

  * A future enhancement could be coded to sort drop list of SPE's throughout the Solution by the sorted SPE Names. A SortedSPENames macro is provided.



  


Development Specification

Change Requests:

  * Tim Reitz 09/13/2024: [[[IN10448](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10450&)]] - XFB - SPE record - Add Bank Account and Sort Number fields (prev. SPE deposits - Add banking info)


