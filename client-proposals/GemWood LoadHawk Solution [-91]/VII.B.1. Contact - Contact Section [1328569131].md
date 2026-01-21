7.2.1. Contact - Contact Section

  * Contact section (standard section, may include custom fields):
    * Active Contact (checkbox; defaults to filled; includes the following validations:
      * N/A (no special validations)) 
    * This contact is inactive as of [   ] (standard; visible if "Active Contact" is not checked; on-screen message in gray font + editable date field; date toggles with "Active Contact" checkbox, defaulting to the current date when the checkbox is unchecked) 
    * Contact Type (required; drop list of Contact Types; standard field;
      * custom behavior: warning on Save if "Member ID" is not blank and "Contact Type" is not "Member": "Consider making this Contact inactive and creating a new Contact rather than changing the Contact Type.") 
    * Is Organization (standard field; label displays as just "Organization"; checkbox; defaults to not checked; used to specify whether the the Contact is an organization or an individual) 
    * First Name (standard field; visible if the Contact is an individual; required; cleared if "Contact Type" is changed to one that is an organization) 
    * Middle (standard field; visible if the Contact is an individual; optional; cleared if "Contact Type" is changed to one that is an organization) 
    * Last Name (standard field; visible if the Contact is an individual; required; cleared if "Contact Type" is changed to one that is an organization) 



  


  * Display Name (visible if the Contact is an individual; macro; with the following details / behaviors: 
    * if "Override Name" checkbox is not checked: read-only, displaying the contents of the "Contact Name" hidden field; 
    * if "Override Name" checkbox is checked: editable; sets & displays the contents of the "Contact Name" hidden field) 
  * Short Display Name (hidden read-only macro; with the following details / behaviors:
    * dynamically displays the following:
      * if "Organization" checkbox is checked: displays the following: "<Organization Name>";
      * if "Organization" checkbox is not checked: displays the following: "<First Name> <Last Name>";
    * to be used on printouts and as the Job Contact on Proposals where "(Use Customer as Job Contact)" is selected)
  * Contact Name (standard field; hidden; with the following details / behaviors: 
    * must be unique, as this is the unique identifier for the record; 
    * by default, 
      * if the Contact is an individual: auto-sets from "First Name", "Middle", and "Last Name", in the "Name Format" selected on the Silverloom Settings page; 
      * if the Contact is an organization: auto-sets from "Organization Name"; 
    * if "Override Name" checkbox is checked, sets from the "Display Name" editable macro; 
    * cleared if "Contact Type" is changed to one that is an organization) 



  


  * Override Name (standard field; visible if the Contact is an individual; checkbox; defaults to not checked; checking this makes "Display Name" editable) 
  * Organization Name (standard; visible if the Contact is an organization; plain text field; required; cleared if "Contact Type" is changed to one that is an individual) 
  * Summary (standard field; optional; plain text field) 
  * Organization (standard field; visible if the Contact is an individual; embedded spreadsheet with the following; this allows the Contact to be linked to multiple organizations/businesses: 
    * Columns: 
      * Name (optional; drop list of all Contacts for which the "Is Organization" checkbox is checked; validates against the same organization being selected more than once for the same Contact - error on Save: "<Organization Name> is included multiple times in the linked organizations.") 
    * Automatically sorted by: N/A (none) 
    * Buttons to add/remove rows: "✚" / "🞭"
    * Shows 4 rows without scrolling 
    * Other Notes: 
      * This embedded spreadsheet includes a "ghost row" to enable the user to easily add a new Organization)


