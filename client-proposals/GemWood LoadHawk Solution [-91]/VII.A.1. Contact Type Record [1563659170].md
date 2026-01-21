7.1.1. Contact Type Record

  


Requirements

Overview: Contact Types are configured on Contact Type records and viewed on a Contact Types report (both Silverloom standard features). Note that any customizations are noted as such in the spec.  

  


Accessed via: Configure Contact Types report

  


Sections and Fields: 

  * Active (checkbox; defaults to checked; a Contact Types cannot be deactivated if it is being used by an active Contact)
  * Type (required; plain text field; validates against duplicate Type names; 
    * custom: Read-only for shipped items) 
  * Supported Entity Types (checkboxes; at least one of the first two is required to be filled:)
    * Individual (checkbox; defaults to checked; 
      * custom: Read-only for shipped items)
    * Organization (checkbox; 
      * custom: Read-only for shipped items)
    * Default to Organization (checkbox; editable if "Organization" is selected; 
      * custom: Read-only for shipped items)



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access:

  * Visibility: Visible to all users
  * Editability: Editable for users with the "Edit the Contact Type lookup record" Permission.



  


Other Notes: 

  * Custom: The following Contact Types in bold font are hard-coded and included in the system automatically ("shipped"):
    * Buyer (organization) 
    * Internal (individual or organization; defaults to individual)
    * Member (organization)
    * Other Individual (individual)
    * Other Organization (organization)
  * Contact records may have certain custom sections and fields, visible depending on their Contact Type (see corresponding sections in this proposal). 
  * If any non-Buyer contact (e.g. Member or Internal, etc.) makes a purchase, they should have a separate Buyer-type Contact record created to handle that.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1191468497#gid=1191468497](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1191468497#gid=1191468497)

  


Ellis Miller 12/16/2024: Nothing to do
