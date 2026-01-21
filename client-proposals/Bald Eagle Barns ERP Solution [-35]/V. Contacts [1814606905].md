5\. Contacts

  


Requirements

The AppHosting Contacts module will be used, along with Contact Types. 

  


All Contact records, regardless of type, will track the following information:

  * Contact (standard section)
  * Address (standard section)
  * Phone (standard section)
  * Email (standard section)
  * Notes (standard section)



  


All Contact records will also have the following custom field(s): 

  * Referred Customers (link to the Customer Referrals Report report, filtered to only show customers referred by this Contact) 
  * 


  


The existing database and QuickBooks are using the Last Name, First Name format for contact names (not using or displaying middle name/initials); this should be maintained in the new system, so the new system will not use Middle Names.

  


Like the existing database and Quickbooks, the standard AppHosting Contacts module does not handle duplicate names. In these use cases, if a user wants to enter a contact with a name that has already been used, the user would manually a differentiator to one of the Name fields. However, this development will include a feature to automatically add a number to each name to allow for duplicate names. When printing documents for customers, the system will automatically remove the differentiator.

  


Data Access (applies to all contacts and contacts reports): 

  * Customer Type contacts: Can be viewed and edited by all users. 
  * All other Type contacts: Each user can view (but not edit) all; Admins can view and edit all.



  


*Done.

  


Development Specification

In their current database they enter a "1" or some other differentiator into the First Name field, then have to manually remove the "1", etc. that they would add to a duplicate name to make it distinct. We're planning to handle this automatically. See [[PC0132714]] - Contacts: Add System Switch for Numbering the Name

  


TODO_CCI: For the "Referred Customers" link, can that simply go in an existing section (like Notes) or should we have a custom "Contact Details" section to hold that? 

  


Note: Our client would like the reports to load in 30 seconds or less. Once we have done the initial import, let's see how fast the Contacts report is loading and optimize if necessary. 

  


Note: We currently don't need the following from the Standard Contacts for BEB: 

  * Middle Name
  * Invoices section



  


TODO_TR: any more custom fields for all contact records?
