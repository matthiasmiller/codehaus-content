12.3.7. Bill Record

  


Requirements

Overview: This is a custom record type, used to track information for Bills.

  


Accessed via: Bills report

  


Sections and Fields: 

  * Bill Section
    * Type 
      * uneditable
      * list of the Bill Types (Bill and Sales Tax Liability)
      * defaults to Bill
      * type of Sales Tax Liability will only be set in the sales tax payment workflow
    * Rental Company (drop list of active rental companies; defaults if there is only one active rental company in the system)
    * Payee (must be Sales Tax Vendor if Type = Sales Tax Liability otherwise any non customer contact)
    * Date
    * Due Date (date field; sets the date that the Bill is due to be payed)
    * Reference (string field;)
    * Description (string field;)
    * Itemization RG (RG; no label. Visible when type is NOT Sales Tax Liability) with the following columns:
      * Entry Type (required; list with options of Product Expense, Product Purchase, Product Premium, and Other)
      * Product ID (hidden; set by Product)
      * Product (editable macro; drop list of Product Descriptions; when a Product is selected, displays only the Primary ID; editable and required for all 3 product entry types)
      * Financial Account (drop list of Financial Accounts; editable and required for Other and Product Expense; automatically pulled from the accounting company for Product Purchase and Product Premium)
      * Amount (number field; displays with comas and 2 decimals)
      * Notes (string field))
    * Period End Date (date field; visible and required if Type = Sales Tax Liability)
    * Total (read-only macro; auto-calculated)
    * Balance (read-only macro; Total - Manual Payments - Check Payments)



  


  * Payments (section) 
    * Latest Payment Date (latest date from manual payments and check payments)
    * Manual Payments (RG) 
      * Date (required)
      * Amount (required)
      * Account (list of financial accounts; required)
      * Ref No (string)
      * Notes (string)
    * Check Payments (virtual RG) 
      * Check Date
      * Check Number
      * Check Total
      * Bill Payment Amount
      * View



  


  * Attachments
    * Attachments; embedded spreadsheet (S3)



  


  * Record History section: 
    * Modification History (link to open the report for the record)



  


Data Access:  Sean Miller 11/03/2025:  TODO_PERMISSIONS 

  * Visibility:
  * Editability:



  


Special Considerations: TODO_IDD

  * Copy Record: __ (think: does it make sense to allow copies? what fields are retained / cleared on copy?) 
  * Delete Record: __ (think: allow deletion? under what circumstances?)
  * Merge Record: __ (think: does it make sense for this record to be merged since the initiating one is deleted completely?; if we disallow deletion across the board, probably disallow merging)



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.  
  * Unless otherwise noted, all fields that become hidden for any reason (based on other fields, user permissions, etc.) retain their values. If they should be cleared, that is noted specifically in the field specs, with a "clear if hidden" or similar note.



  


Development Specification

Top RG:

NA         Sales Tax Liabilities        $15,543.12

  


Bottom RG:

Items that add up to $15,543.12
