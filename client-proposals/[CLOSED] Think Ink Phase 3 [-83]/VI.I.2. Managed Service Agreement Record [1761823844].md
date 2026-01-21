6.9.2. Managed Service Agreement Record

  


Requirements

Overview: The Managed Service Agreement record is used to track one or more Managed Devices (the Agreement's "Billing Group") for a Customer. This Agreement record is primarily used for billing purposes. Note that one Customer may have multiple Agreement records (for example, if it is a business with multiple locations, or if the customer wishes to bill devices separately). 

  


Accessed via: 

  * Managed Service Agreements Reports
  * Linking on Managed Devices
  * Home | Manged Service Agreements | New Agreement (opens a blank new record) 



  


Sections and Fields: See following sections

  


Data Access: All users can view and edit

  


Special Considerations: 

  * Copy Record: N/A
  * Delete Record: Prevent deletion if:
    * The Agreement Status = Active
    * There are unpaid Invoices linked to the Agreement
  * Merge Record: Disallow merging 



  


Other Notes:

  * One invoice is generated per Agreement per billing. If a customer has multiple devices that should be invoiced separately, there should be a separate Agreement for each desired invoice.
  * Printers grouped under an Agreement can have page counts collected either combined or separately, meaning that all printers under an Agreement would be either combined or separate (not mixing under the same agreement). Note that the majority of the time they would be separate.
  *  Close-out procedure: 
    * Deactivate or unlink all Devices 
    * Deactivate the Agreement
    * Finalize billing
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2136959849](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=2136959849)

  


  


  


HL Est: 8 Hours
