5.2.5. RTO Company

  


Requirements

Each RTO company that BEB works with should have a contact record in the database. The detail screen for a RTO Company contact will include the following custom section and fields:

  


RTO Company Details section:

  * RTO Terms, which is an embedded spreadsheet of:
    * Columns: 
      * Months (required; whole number)
      * Payment Divisor (required; number with up to 2 decimal places)
    * Sort by Months (smallest number at the top) 
  * RTO Security Deposit $, which is an embedded spreadsheet of:
    * Columns: 
      * Building Width (required; whole number)
      * $ Amount (required; whole number)
    * Sort by Building Width (smallest number at the top) 
  * LDW Rate % (required;  number with up to 2 decimal places; stands for "Loss Damage Waiver"; % of the pre-tax payment amount for RTO sales; added onto the taxed payment amount;)
    * This percentage is used on the Sales Quote/Order in RTO sales, and it is printed on the RTO contract (see the corresponding sections of this proposal).
    * This is currently set to 6% of the pre-tax payment amount.
  * EPO % (required; number with up to 2 decimal places; this is the "Early Purchase Option" \- this is used only as a reference in the database and for the printout - it is not used in any calculations)
  * RTO Premium % (required; number field, whole number; this is a percentage of the building price after discounts but before sales tax; charged to the RTO company for all new buildings that they buy)
  * SRB Sales Commission % (required; number field, whole number; this is a percentage of the building price after discounts but before sales tax; charged to the RTO company for all SRB buildings that are sold; currently 8%)
  * SRB Delivery % (required; number field, whole number; this is a percentage of the building price after discounts but before sales tax; charged to the RTO company for all SRB buildings that are sold; currently 5%)
  * RTO Letterhead (button that opens a memo in a child screen; a PDF or Word file of the letterhead can be uploaded here for the RTO-related printouts)
  * RTO Contract Template (button that opens a memo in a child screen; formatted template from the existing BEB Sales Quote; see corresponding section of this proposal) 



  


Other Notes: 

  * Each RTO Company should have a User Login set up in the database, and should have their User Login ID linked with the Contact record.
  * The Contact record should have a warning on Save if an active RTO Comany contact does not have a User ID associated with the contact record. This warning should say, "This RTO Company contact is missing its linked User ID."
  * If an RTO Company ceases to do business with BEB, an admin should deactivate both the Contact and the User Login.
  * The RTO Company contact would always be an Organization. 



  


*Done.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1529895558](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1529895558)

  


There currently are two options for the RTO Terms that they work with: 36 months and 48 months. 

The payment divisor calculates for these are as follows: 

  * 36 months: cash price / 21.6 = monthly payment
  * 48 months: cash price / 24 = monthly payment



Note for CCI: We considered breaking Terms into a separate lookup record.

  


Security Deposit: Currently is $100 for 8ft wide, $200 for 12ft wide, etc. 

  


Example of the LDW Rate % calculations: 

  * Pre-tax Payment: 241.67
  * LDW: 14.50
  * Sales Tax: 24.77
  * Total Payment: 280.94



  


The EPO percentages are as follows: 

  * 36 months: 40%
  * 48 months: 50% 



  


RTO Contract Template: Memo that evaluates on the Sales Order Record. 

  


TODO_JM: copy of RTO letterhead

  


  


  


DONE_CH: See the mockup. Can we have the smaller sections in the left column come up beside the tall RTO details section?

TODO_CCI: Can we have the Invoices/Incidents to the left of the RTO settings, or should we break RTO settings into two columns side-by-side?
