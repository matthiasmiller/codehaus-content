7\. Number HRD Fees on Invoices

  


Requirements

It would be nice to note on the invoices which number the invoiced HRD fee is (1 of 3, 2 of 3, or 3 of 3) so that the client receiving the invoice can have more information about the fee. 

  


Design: 

  * On the HRD Fees section of the Contact page: 
    * Add a "Description" column (editable for admin)
    * The fee description should show the fee number and the original date that the fee was assessed (something like "Fee 1 of 3 starting on mm/dd/yyyy") 
    * The numbering (1-3) would start over each time a new set of HRD fees is assessed for a client  
    * If a fee is deleted, the admin can edit the other rows' descriptions to fix the numbers (e.g. change "1 of 3" to "1 of 2", etc.)
    * If a driver is assessed more than one set of HRD fees, the admin can edit the descriptions as desired (e.g. change the new fees from "1 of 3" to "4 of 6", etc.). 
  * On the Invoice screen: 
    * For the "Description" column, show the driver's name and the description from the HRD fee (e.g. "Martin, James - Fee 1 of 3 starting on mm/dd/yyyy") 
  * On the Statement / printout: 
    * Change the "Vehicle" column to be "Driver / Vehicle"
    * In that column, show the driver's name for HRD fees
    * In the "Description" column, show the description for HRD fees (e.g. "Fee 1 of 3 starting on mm/dd/yyyy") 
  * Make sure the description is transferred if the fee is transferred from a parent to child, etc.  



  


T&M Estimate: $500-1,000 (if preferred, this could also be done as a fixed bid instead of T&M)

  


Development Specification

See (in MYS): [[[IN4984](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-4986&)]] - ZWA - Number HRD Fees on Invoices
