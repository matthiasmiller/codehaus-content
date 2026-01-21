5.1.1. Contact Type Record

  


Requirements

Overview: This is a custom record type, used to track Contact Types. These types categorizes contacts as Builders (pickup locations like furniture manufacturers) or Customers (delivery destinations like retail stores). Ships with these two primary types but allows flexibility to add additional contact categories as VVT's business needs evolve.

  


Accessed via: Configure Contact Types report

  


Sections and Fields: 

  * Active (checkbox)
  * Type (plain text field; 
    * custom: Read-only for shipped items)



  


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

  * Custom: The following Contact Types are hard-coded and included in the system automatically ("shipped"):
    * Builders
    * Customers
  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  
  * Unless otherwise noted, all fields that become hidden for any reason (based on other fields, user permissions, etc.) retain their values. If they should be cleared, that is noted specifically in the field specs, with a "clear if hidden" or similar note.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=1191468497#gid=1191468497](https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=1191468497#gid=1191468497)
