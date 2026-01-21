4.8.1.4. Sales Item Record

  


Requirements

Overview: The Solution uses a customized version of the the standard AppHosting Sales Items record. Data for most of these records will be imported from Classic Accounting items. 

  


Accessed via: The Manage Sales Items report

  


Sections and Fields: See the sections below in the proposal.

  


Data Access:

  * All Categories except for Device Models:
    * Can be viewed by Standard users
    * Can be viewed and edited by Admin and Manager users
  * Device Models: TODO_JM



  


Special Considerations: 

  * Copy Record: N/A
  * Delete Record: Prevent deletion if the record is referenced anywhere in the Solution: "This record cannot be deleted because it is referenced by another record in the database."
  * Merge Record: N/A



  


Other Notes:

  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=670310422](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=670310422)

  


  


TODO_EM: Tim Reitz 09/12/2023: What do we need to think through regarding linking of invoices with: Sales Item Records, Device Records, Agreement Records? 

  


  


HL Est: 4 hours
