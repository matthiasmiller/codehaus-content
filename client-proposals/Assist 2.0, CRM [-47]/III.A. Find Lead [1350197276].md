3.1. Find Lead

  


Requirements

This is a report of leads for walkins/phone calls.

  


This would be accessed from the Leads menu 

  


Title: Find Lead

  


Left Pane:

Columns: 

  * Name
  * Phone
  * Full Address
  * Email
  * Salesperson



  


Grouped by: 

  * Unclaimed
  * Your Contacts
  * Other Contacts



  


Sorted by: 

  * Most Recent Communication from Opportunity



  


Right Pane:

Columns: 

  * Opportunity Name
  * Status
  * Origination Date
  * Followup Date
  * Closed Date
  * Closed Reason



  


Grouped by:

  * Status



  


Sorted by: 

  * Followup Date (descending)
  * Origination Date (descending)



  


Filters: 

  * Name
  * Phone Number
  * Lead Opportunities (blank = all; default to all)
    * Open
    * Closed
    * Abandoned



  


Buttons:

  * The "New Contact" button opens a new contact and prefills the name and phone number. Once the contact has a name and is saved, allow creating a new opportunity for that contact.



  


Other Notes:

  * If Lead Opportunities is set to "Open", show all leads with open opportunities. If "Closed", show all leads with closed opportunities. If it's set to "Abandoned", show all opportunites with a last activity date and followup date that is at least X days in the past (based on the Abandoned Leads setting).



  


Development Specification

I think all we need for now is a subset that gives us the contacts, as well as a comparable subset that gives opportunities for those contacts.
