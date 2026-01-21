7.1.1. Contact Type Record

  


Requirements

*Done. 

  


Overview: Contact Types are configured on Contact Type records and viewed on a Contact Types report (both Silverloom standard features). Note that any customizations are noted as such in the spec.  

  


Accessed via: Configure Contact Types report

  


Sections and Fields: 

  * Contact Type section (standard): 
    * Type (required; plain text field; validates against duplicate Type names)
    * Active (checkbox; defaults to checked; a Contact Types cannot be deactivated if it is being used by an active Contact)
    * Supported Entity Types (checkboxes; at least one of the first two is required to be filled:)
      * Individual (checkbox; defaults to checked)
      * Organization (checkbox; defaults to not checked)
      * Default to Organization (checkbox; editable if "Organization" is selected; defaults to not checked)



  


  * Record History section (standard section; custom visibility: visible only to users with the "Edit the Contact Type Lookup Record" Permission): 
    * Created: (User ID, date, and time stamp) 
    * Last Modified: (User ID, date, and time stamp)
    * Modification History (link to open the report for the record)



  


Data Access:

  * Visibility: Visible to all users (standard)
  * Editability: Editable for users with the "Edit the Contact Type Lookup Record" Permission (standard)



  


  


Special Considerations: 

  * Copy Record: Allowed; no fields are cleared on copy (standard). 
  * Delete Record: Allowed until the record has been referenced by another record, at which point deletion is disallowed (standard). 
  * Merge Record: Allowed without restrictions; the record from which the merge is initiated is completely replaced by the other (deleting all data for the first record) (standard).  



  


Custom: The Solution includes the following hard-coded "Silverloom Supplied" Contact Types, which are included in the Solution automatically as read-only records (requiring coding work to edit):

  * "Individual" (individual-only)
  * "Organization" (organization-only; defaults to organization)



  


  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * Contact records may have certain custom sections and fields, visible depending on their Contact Type (see corresponding sections in this proposal).
  * Heading color: This record type uses the standard Silverloom blue color for section headings.



  


Development Specification

Mockup:[https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=641906559#gid=641906559](https://docs.google.com/spreadsheets/d/1bpeWh2j2MO5nVWChdcagYduhD2adVJ4S3S2q9I5_SwQ/edit?gid=641906559#gid=641906559)

  


_NM: Tim Reitz 01/17/2026: For invidividual vs. organization, should we specify throughout the spec that the code should be looking at the "Is Organization" checkbox, rather than the "Contact Type" when we're distinguishing between the two?

TODO_VA: Tim Reitz 01/20/2026: Nic thinks that using "individual" and "organization" (lower case) should be sufficient. And include a note here in the main spec to make it clear.
