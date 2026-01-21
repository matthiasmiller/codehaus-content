7.1.11. Wiki Category Record

  


Requirements

Overview: The Solution includes the standard AppHosting Wiki Categories feature for categorizing Wiki pages. This includes both the standard Wiki Category record pages and the standard Wiki Categories report (see corresponding section of the proposal). 

  


Accessed via: Configure Wiki Categories Report

  


Sections and Fields: 

  * Category Name (required; plain text field; validation error message: "A Wiki Category name cannot be blank."; defaults to blank) 
  * Parent (drop list of Wiki Categories, to allow the user to create hierarchies or "Wiki trees") 



  


Data Access: See the Data Access Controls section of the proposal for details.

  


Special Considerations: 

  * Copy Record: Clears the ID.
  * Delete Record: No restrictions.
  * Merge Record: No restrictions.



  


Other Notes:

  * Note that this record includes a link to access Modification History (standard).



  


Development Specification

Change Requests: 

  * Tim Reitz 03/29/2024: [[[IN9469](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9471&)]] - ZSB - Add Wiki module


