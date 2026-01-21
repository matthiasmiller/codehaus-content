5.4. Event Record

  


Requirements

*Documented 

  


Add the following new record type (replaces the existing General Meeting record):

  


Overview: The Event record is used to schedule and manage various types of events that Symbiz hosts or puts on.

  


Accessed via: 

  * All Events Report
  * Various Type-specific reports
  * Admin | Event Management | New Industry Forum (opens a new record with Event Type defaulted)
  * Admin | Event Management | New Info Meeting (opens a new record with Event Type defaulted)
  * Admin | Event Management | New Launch Meeting (opens a new record with Event Type defaulted)
  * Admin | Event Management | New Annual Summit (opens a new record with Event Type defaulted)



  


Sections and Fields: See the corresponding sections of this proposal.

  


Data Access: See the Data Access Controls section of the proposal for details.

  


Special Considerations:

  * Copy Record: Prevent copying (note that a "Copy Event" link could be added to the detail screen if desired in the future)
  * Delete Record: Prevent deletion if Status is not Canceled (error message: "This record cannot be deleted because its Status is not Canceled.")
  * Merge Record: Can be merged by Super Admins only.



  


Other Notes:

  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=756089585](https://docs.google.com/spreadsheets/d/1KorfG3q0XrBAdO7fqW9ikcpPGSXx3ohMAIuTGksaTTE/edit#gid=756089585)

  


Ellis Miller 06/20/2024: 

[ ] Lookup record

  


1 hour
