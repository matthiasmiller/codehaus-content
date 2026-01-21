4.1.5. Sales Tax Rate Record

  


Requirements

Overview: This record is used to track the current sales tax rate for a specific state where the client is registered.

  


Accessed via: Sales Tax Rates Report

  


Sections and Fields: 

  * State (required; drop list of all US states; error on save if the state is blank: "The delivery state is not specified.")
  * Current Rate (required; editable number field supporting up to two decimals; error on save if blank: "There is no tax rate specified.")



  


Data Access: All users

  


Special Considerations: 

  * Copy Record: N/A
  * Delete Record: 
  * Merge Record: N/A



  


Other Notes:

  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).
  * Sales Tax will not be interfaced in Order reports, since tax reporting is done from QuickBooks.



  


Development Specification

Change Requests: 

  * Tim Reitz 07/20/2024: [[[IN7935](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7937&)]] - ZTD - Sales tax in multiple states


