11.2.5. Contact - Related Contacts Section

  


Requirements

Related Contacts section (visible for all Contact Types):

  * Related Contacts (no label; embedded spreadsheet (RG) with the following: 
    * Columns:
      * Name (required; drop-list of active Individual-type Contacts; no validation against the same Contact being selected multiple times on the same RG) 



TODO_NM: Tim Reitz 09/11/2024: Is it correct to have no validation against duplicate Contacts here? 

  * Default Name (checkbox; defaults to checked if the selected Contact has a "Preferred Name" set, otherwise defaults to not checked; if unchecked and the entered Preferred Name in the RG is the same as the "Preferred Name" on the selected Contact's record, it is rechecked on Save) 
  * Preferred Name (plain text; if the "Default Name" checkbox is checked, displays the selected Contact's "Preferred Name" if there is one, otherwise displays the Contact's First Name; editable if Default Name is unchecked)



 TODO_NM: Tim Reitz 09/11/2024: Could we have more explanation here? I.e., how does this interact with the "Preferred Name" field on the Contact record? It appears that setting a name here does not update the corresponding field on the Contact record. Is that correct? 

  * Role (required; drop-list of the "Related Contact Roles" list items - see corresponding section of the living spec - and an option to add a new item) 



TODO_NM: Tim Reitz 09/11/2024: There is no validation against duplicating the same Role on the RG. Is this correct? (we could have multiple Primary Contacts). 

  * Title (visible & optional if the "EITC" checkbox in the Contact Details section is checked; drop-list of the "Person Titles" list items - see corresponding section of the living spec - and an option to add a new item)
  * CEO (visible if the "EITC" checkbox in the Contact Details section is checked; checkbox; defaults to not checked)
  * Phone (drop-list of all phone numbers listed on the selected Contact's record)
  * Default Email (checkbox; defaults to checked)
  * Email (plain text or drop-list:
    * if Default Email is checked: this is a semicolon-delimited list of primary email addresses from the selected Contact's record;



TODO_NM: Tim Reitz 09/11/2024: Actually, this displays non-primary addresses as well. Which is the intended behavior?

TODO_NM: Tim Reitz 09/11/2024: Also note that if the Contact has a Login Email specified, that is displayed unless the "Override Email" checkbox is checked, in which case it is excluded. Is that correct?

  * if Default Email is not checked; this is a drop-list of all primary email addresses from the selected Contact's record)



TODO_NM: Tim Reitz 09/11/2024: Same as above.

  * Link (displays as "View"; link that opens the selected Contact's record)
  * Automatically sorted by: N/A (no sorting) 


  * Buttons:
    * "+" (insert row)
    * "-" (delete selected row)
  * Show 5 rows without scrolling 
  * Additional validation(s): 
  * Additional notes: 



  


Validation:

  * Error: if more than one row in the RG has CEO checked.



TODO_NM: Tim Reitz 11/18/2025: FYI that we've been speccing validations with the corresponding column/field specs. If there's a validation that doesn't belong under one of those, I'll add another bullet point under the RG spec for "Additional validation(s)" \-- see above. I'm leaving this as-is for now so you can see the note. You can update it or delegate.

  


Additional behaviors:

  * If there is a related contact with "Role" set to "Primary Contact" that has an email addresses, their email address(es) will be used in all email communications to the contact.
  * Any related contacts with "Role" set to "Secondary Contact" will be carbon copied to email communications.



TODO_NM: Tim Reitz 11/18/2025: Also an FYI that I've been adding another bullet point under the RG spec for "Additional notes" \- see above. I'm leaving this as-is for now so you can see the note. You can update it or delegate.

  


Development Specification

TODO_NM:

Consider changing 'Link' column header to 'Open Contact'.

Tim Reitz 09/11/2024: Good thought. "View" or "View Contact would also be an option.

  


  


Change Requests:

  * Ben Reitz 05/01/2025: [[[IN11079](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11081&)]] - XFB - Contact record - Move "Link" column on Related Contact RG


