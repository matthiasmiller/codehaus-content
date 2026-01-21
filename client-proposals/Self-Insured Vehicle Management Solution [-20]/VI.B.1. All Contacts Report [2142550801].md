6.2.1. All Contacts Report

TODO_VA: Tim Reitz 09/02/2025: Follow up on various items.  

TODO_VA: Tim Reitz 09/02/2025: Update the Snippet with standard stuff. 

  


Overview: This is a custom report of Contact records, with various filters.

  


Accessed from:

  * Home | Contacts | Contact Search (opens a filter / search screen, displaying the filters listed below) 
  * Home | Contacts | My Clients (opens the report directly, bypassing the filter screen; includes all Clients for the current logged-in Agent, with "Agent (Blank = all)" is defaulted to the current user) 
  * Home | Contacts | All Clients (opens the report directly, bypassing the filter screen; includes all Clients)  
  * Home | Contacts | All Contacts (opens the report directly, bypassing the filter screen) 
  * Admin | Admin Searches | Client Search (opens a filter / search screen, displaying the filters listed below) 



  


Title: 

  * "All Contacts": If opened from the following: 
    * Home | Contacts | Contact Search 
    * Home | Contacts | All Contacts
  * "All Clients": If opened from the following: 
    *  Home | Contacts | All Clients 
    * Admin | Admin Searches | Client Search
  * "My Clients": If opened from the following:
    * Home | Contacts | My Clients



  


Preface: N/A

  


Columns: 

  * Name (link to record)
  * Phone



 Murshid Rahman 09/01/2025: I don't know if we should add this is living spec, this has some special coding.

  * Displays the top phone number from the Phone RG when Phone Number ask is blank.
  * Displays the matched phone number from the Phone RG when Phone Number ask is not blank.
  * Blank if contact has only Fax type of numbers and Phone Number ask is blank
  * Displays the next non-Fax number if Fax is the top row and Phone Number ask is blank


  * Phone Type



Murshid Rahman 09/01/2025: This displays the corresponding Phone Type that was displayed in "Phone" column.

  * Email



Murshid Rahman 09/01/2025: Returns ";" separated list of all primary emails

  * City



Murshid Rahman 09/01/2025: Returns <City, State>. Returns city of primary address or matched city if the contact has multiple addresses.

  * Congregation
  * Type
  * Agent



  


Grouped by: Active, Snoozed, Inactive

  


Sorted by: Name

  


Filters: 

  * Name (plain text; defaults to blank = all) 
  * Client Code (plain text; defaults to blank = all) 



 Murshid Rahman 09/01/2025: This is the Contact ID in square brackets on the Contact heading of the record.

  * Phone Number (defaults to blank = all)
  * City (plain text; defaults to blank = all) 
  * State (drop-list; defaults to blank = all)
  * Zip (defaults to blank = all)
  * Status (multi-select list of "Client Status" list items and "All"; defaults to "Active")
  * Agent (drop list of "In-State Agent"-type Contacts; defaults to blank = all)



 Murshid Rahman 09/01/2025: List of Active In-state Agent with Funds.

  * Type (multi-select list of Contact Types and blank = all; defaults to blank) 



Murshid Rahman 09/01/2025: Active types only.

  


Buttons: 

  * New Contact (opens the "New Contact" report prompt screen - see the corresponding section of the proposal)



  


Menu Visibility: 

  * All Users



  


Other Notes:

  * N/A



  


_CCI: Tim Reitz 07/31/2025: Could you review this spec and make sure it looks good to you? Thanks!

Murshid Rahman 09/01/2025: I have added my comments above. Please discard the suggestions if you think details are not needed in living spec. Other than that the spec looks good to me. Thanks.

TODO_VA: Tim Reitz 09/01/2025: Follow up on these.
