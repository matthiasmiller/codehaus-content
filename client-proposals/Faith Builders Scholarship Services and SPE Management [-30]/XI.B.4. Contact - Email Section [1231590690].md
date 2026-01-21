11.2.4. Contact - Email Section

  


Requirements

Email section (standard): 

  


Email (standard field & embedded spreadsheet; can track multiple email addresses, and one or more can be designated as "Primary")

  


Additional behaviors:

  * Hidden if there is a primary related contact.
  * If there are rows in the RG and no row is marked as primary, the first row will be automatically marked as primary upon save.



  


Development Specification

TODO_NM: CustomContacts_ValidateMissingEmail warning is redundant now that we auto-set Primary if there are no primary rows.
