3.7.1. Sales Tax Code Record

  


Requirements

Overview: The Sales Tax settings data will be stored on a "Sales Tax Code" record.  

  


Accessed via: The Sales Tax Codes Report

  


Sections and Fields: 

Sales Tax Code section: 

  * Active (checkbox) 
  * Type (required; list of the following:) 
    * Sales Tax Item
    * Sales Tax Group 
  * Name (required; text field) 
  * Description (required; text field) 
  * Rate % (required and visible if Type = Sales Tax Item; number field to 3 decimal places)
  * Included Rates (visible and required if Type = Sales Tax Group; embedded spreadsheet of the following:)
    * Columns:
      * Code (list of active non-group Codes)
      * Rate % (number field to 3 decimal places; auto-filled from the selected Rate in the first column; sum must equal the Rate % for the Sales Tax Group)
    * Show 4 rows without scrolling



  


Data Access: Admin Only

  


Other Notes: 

  * When in edit mode the detail screen will display a message in red: "Any changes will be overridden with the next sync from QB". 



  


*Done.

  


Development Specification

This is a lookup record.

  


We'll want to have an internal list field called TaxCodeQBID for linking and syncing. 

  


If a Code is deleted in QB, simply deactivate the equivalent code in the database. 

  


Note that "Codes" are the names; "Rates" are the amounts.

  


There are approximately 815 sales tax codes in the provided list from BEB.

File: [[File:Sales Tax Items (from BEB on 8-10-21).xlsx]] / Link to Drive: [https://docs.google.com/spreadsheets/d/1JrYRLtbHlFMXzoUTiUMW68QaA4-LN_8S/edit#gid=1217332919](https://docs.google.com/spreadsheets/d/1JrYRLtbHlFMXzoUTiUMW68QaA4-LN_8S/edit#gid=1217332919)

NOTE: Most of the columns in this file are not needed. Only the ones that correspond to the fields in the Requirements are needed.

  


Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1523374688](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1523374688)
