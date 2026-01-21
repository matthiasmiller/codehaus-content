5.1.4. Builder Region Record

  


Requirements

Overview: This is a custom record type, used to track Builder Regions. This records helps to group pickup locations (like Indiana, Lancaster PA, New Wilmington) to apply consistent markup rules based on where furniture is collected. Each region has a standard markup percentage plus optional overrides for specific customer regions—for example, Indiana pickups shipping east get an additional 2% upcharge.

  


Accessed via: Configure Builder Regions report

  


Sections and Fields: 

  * Active (checkbox)
  * Name (plain text field)
  * Standard Markup % (number field)
  * Regional Markup (embedded spreadsheet with the following:
    * Columns:
      * Customer Region (drop list)
      * Markup Override % (number field)
    * Buttons to add/remove rows: "✚" / "🞭"
    * Shows TBD rows without scrolling
    * Other Notes: N/A)



  


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

Mockup: [https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=2145064356#gid=2145064356](https://docs.google.com/spreadsheets/d/1Eo-qztGoXmt5e6q_S9lNygvSc33VJAABb9K33xWXpvQ/edit?gid=2145064356#gid=2145064356)
