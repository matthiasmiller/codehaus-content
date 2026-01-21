4\. Snippet Record

Overview: This is a standard record type, used to track the information for a specific Snippet.

  


Accessed via: Snippets Report

  


Sections and Fields: 

  * Snippet section: 
    * Name (plain text field; error on the field if the name is a duplicate of an existing Snippet record: "Duplicate Snippet names are not allowed: <Name>")
    * Type (drop list of Snippet Types)
    * Visibility (expression field; visible if "Type" is not blank and is not "Wiki")



  


  * Contents section:
    * Insert Name and Date Prefix (checkbox; when checked, includes the current user's Name and Date Prefix when the Snippet is selected on another record)
    * Name and Date Prefix Preview (unlabeled and read-only field; visible if the "Insert Name and Date Prefix" checkbox is checked; displays the current user's Name and Date Prefix)
    * Contents (unlabeled memo; information entered here is what is displayed when the Snippet is selected on another record)



  


  * Record History section: 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users
  * Editability: Editable for all users



  


Special Considerations: 

  * Copy Record: Allow (clear Name field on new record)
  * Delete Record: Allow 
  * Merge Record: Allow 



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  
  * Unless otherwise noted, all fields that become hidden for any reason (based on other fields, user permissions, etc.) retain their values. If they should be cleared, that is noted specifically in the field specs, with a "clear if hidden" or similar note.


