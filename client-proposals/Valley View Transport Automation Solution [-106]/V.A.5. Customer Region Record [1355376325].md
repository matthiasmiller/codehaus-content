5.1.5. Customer Region Record

  


Requirements

Overview: This is a custom record type, used to track Customer Regions. This record defines delivery zones that mirror VVT's published delivery routes (10 regions covering the eastern U.S.), each with its own base rate percentage and minimum charge. These regions determine the foundation of pricing before builder-specific and product-specific markups are applied.

  


Accessed via: Configure Customer Regions report

  


Sections and Fields: 

  * Active (checkbox)
  * Name (plain text field; 
    * custom: read-only for shipped items)
  * Route # (number field without decimals; validate against duplicate Type Route #'s)
  * Description (required; plain text field)
  * Base Rate % (number field)
  * Minimum Charge (number field allowing 2 decimals)



  


  * Record History section: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: TBD
  * Editability: TBD



  


Special Considerations: 

  * Copy Record: TBD
  * Delete Record: TBD
  * Merge Record: TBD



  


Other Notes: 

  * Custom: The following Customer Regions are hard-coded and included in the system automatically ("shipped"):
    * North East Route
    * North East Route Ext.
    * South East Route
    * West Route
    * South West Route
    * South West Route Ext.
    * South Route
    * Florida Route
    * Florida Route Ext.
    * West Route Ext.
  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  
  * Unless otherwise noted, all fields that become hidden for any reason (based on other fields, user permissions, etc.) retain their values. If they should be cleared, that is noted specifically in the field specs, with a "clear if hidden" or similar note.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=149233144#gid=149233144](https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=149233144#gid=149233144)
