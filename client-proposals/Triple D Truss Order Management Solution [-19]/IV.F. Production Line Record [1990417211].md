4.6. Production Line Record

  


Requirements

TODO_AP: Ben Reitz 11/14/2025: Standardize this spec as needed.

  


Overview: This record is used to track Production Lines, as well as their capacities and available amounts.

  


Accessed via: 

  * "Truss Date" report



  


Sections and Fields: 

  * Production Line (unique identifier for the record; required; plain text field; editable only by Users with the "Manage truss date" permission; validate against duplicates)
  * Capacity (required; number field; editable only by Users with the "Manage truss date" permission; validate against numbers less than or equal to zero)
  * Truss Date (required; date field; editable only by Users with the "Manage truss date" permission; "Available Board Feet" automatically updates to match "Capacity" when "Truss Date" is updated (either manually or automatically))
    * note that the weekday of the currently set "Truss Date" field is displayed in gray text beside said field.
  * Available Board Feet (number field; manually editable only by Users with the "Manage truss date" permission; validate against numbers less than zero; automatically updated as "Enter Board Feet Sold" numbers are entered; with the following behaviors:
    * if a number is entered in "Enter Board Feet Sold" that is equal to or greater than the number in this field, use the remaining Available Board Feet for the current Truss Date and subtract the remaining amount from the next Truss Date)
  * Enter Board Feet Sold (number field; editable; on Save, the following fields are affected in this order:
    * "Last Board Feet Adjustment" is set to the number entered in "Enter Board Feet Sold";
    * "Available Board Feet" is reduced by "Enter Board Feet Sold";
    * "Truss Date" is updated to the next day that is not Saturday or Sunday if "Available Board Feet" = "0";
    * "Enter Board Feet Sold" is cleared;
    * note that negative numbers can be entered to add to Available Board Feet or move to prior days;
    * note that if a large enough amount is entered, "Truss Date" will move forward multiple days)
  * "Available Board Feet will be adjusted on save." (message in gray text)
  * Last Board Feet Adjustment (hidden numeric field to store the last number entered in "Enter Board Feet Sold"; used so that we have activity history on adjustment)
  * Notes (memo; editable only by Users with the "Manage truss date" permission)
  * Last Modified (auto-set and read-only; displays the date and time that the record was last modified)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visible to all Users
  * Editability restricted based on permissions



  


Special Considerations:

  * Copy Record: N/A 
  * Delete Record: N/A
  * Merge Record: N/A



  


Other Notes: 

  * N/A



  


Development Specification

Sean Miller 03/24/2025: Mockups:

  * Truss Date Report 



[https://docs.google.com/spreadsheets/d/1oQST0RH6jVoVkhYr8bBhs0a2RpgnToDuj5ERlxiow30/edit?gid=636927807#gid=636927807](https://docs.google.com/spreadsheets/d/1oQST0RH6jVoVkhYr8bBhs0a2RpgnToDuj5ERlxiow30/edit?gid=636927807#gid=636927807)

  * Production Line Record 



[https://docs.google.com/spreadsheets/d/1oQST0RH6jVoVkhYr8bBhs0a2RpgnToDuj5ERlxiow30/edit?gid=1018632650#gid=1018632650](https://docs.google.com/spreadsheets/d/1oQST0RH6jVoVkhYr8bBhs0a2RpgnToDuj5ERlxiow30/edit?gid=1018632650#gid=1018632650)
