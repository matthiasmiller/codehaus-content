7.1.8. Development Resource Media Type Record

  


Requirements

Overview: Development Resource Media Types will be configured on the Development Resource Media Type record and viewed on a Development Resource Media Types report. These are used to track the various media types that are used for Development Resources.

  


Accessed via: Configure Development Resource Media Types Report

  


Sections and Fields: 

  * Active (checkbox; defaults to filled)
  * Media Type Name (required; plain text; validate against duplicates)
  * Sort Order (number field; allows 0 and higher; validate against duplicates) 
  * Include Downloads Section (checkbox; defaults to cleared; if filled, the Development Resource Record will display the Downloads section for this Media Type)
  * Include Purchase Options (checkbox; defaults to cleared; if filled, the Development Resource Record will display the Purchase Options section for this Media Type)



  


Data Access: See the Data Access Controls section of the proposal for details.

  


Special Considerations:

  * Copy Record: N/A
  * Delete Record: Prevent deletion if the record is referenced anywhere in the Solution: "This Media Type cannot be deleted because it is referenced by another record in the database."
  * Merge Record: N/A



  


Other Notes:

  * These items are to be set up by Symbiz, with help from CCI/CH as needed.
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1996321838](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=1996321838)
