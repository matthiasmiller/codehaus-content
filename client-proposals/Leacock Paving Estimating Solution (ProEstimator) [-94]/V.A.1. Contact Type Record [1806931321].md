5.1.1. Contact Type Record

  


Requirements

Overview: Contact Types are configured on Contact Type records and viewed on a Contact Types report (both Silverloom standard features). Note that any customizations are noted as such in the spec.  

  


Accessed via: Configure Contact Types Report

  


Sections and Fields: 

  * Active (checkbox; defaults to checked; a Contact Types cannot be deactivated if it is being used by an active Contact)
  * Type (required; plain text field; validates against duplicate Type names) 
  * Supported Entity Types (checkboxes; at least one of the first two is required to be filled:)
    * Individual (checkbox; defaults to checked)
    * Organization (checkbox)
    * Default to Organization (checkbox; editable if "Organization" is selected) 



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access:

  * Visibility: Visible to all users
  * Editability: Editable for users with the "Edit the Contact Type lookup record" Permission.



  


Custom: The Solution includes the following "Silverloom-supplied" Contact Types, which are hard-coded and included in the Solution automatically as read-only record (requiring coding work to edit): 

  * Customer (individual or organization, defaulting to individual)
  * Other Individual (individual)
  * Other Organization (organization) 
  * Employee (individual; note that this is used for all internal Leacock Paving users) 



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * Contact records may have certain custom sections and fields that are conditionally visible depending on their Contact Type (see corresponding sections in this proposal). 
  * If any non-Customer contact (e.g. Sales Rep, etc.) makes a purchase, they should have a separate Customer-type Contact record created to handle that.



  


Development Specification

TODO_VA: Tim Reitz 11/21/2025: Use "Silverloom-supplied" terminology, here and in Snippet

  


Mockup: N/A 

  


  


Ellis Miller 06/10/2025: 

[ ] Ship the above items.

2 Hours
