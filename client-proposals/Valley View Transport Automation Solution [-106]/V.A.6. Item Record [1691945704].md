5.1.6. Item Record

  


Requirements

Overview: This is a custom record type, used to track Items. This record defines furniture pieces (dressers, beds, tables) with pre-configured cubic footage that auto-populates when adding items to orders. Replaces the dispatcher's mental "cheat sheet" and enables anyone to accurately calculate truck capacity without years of experience.

  


Accessed via: Configure Items report

  


Sections and Fields: 

  * Name (plain text field)
  * Default Cubes (number field allowing 3 decimals)



  


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

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  
  * Unless otherwise noted, all fields that become hidden for any reason (based on other fields, user permissions, etc.) retain their values. If they should be cleared, that is noted specifically in the field specs, with a "clear if hidden" or similar note.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=87294605#gid=87294605](https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=87294605#gid=87294605)

  


TODO_: Tim Reitz 10/22/2025: Consider using the standard Sales Items feature? (for potential future expansion, etc.) What are pros & cons? 

Tim Reitz 10/22/2025: These aren't specifically sales items for VVT. That would be one reason for a custom record.
