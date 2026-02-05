8.3.2. Invoice Record

Seth Miller 01/27/2026: TODO_Seth: clean up spec and delegate. [[TA0021082]]

_____________________________________________

Header Section:

  * Standard fields...
  * Accounting Company (list of accounting companies; required) Seth Miller 01/09/2026: Being replaced by Rental Company in [[PC0188542]]



  


Itemization Section:

  * Product (numeric entry macro; when set, sets Product for all rows in the itemization RG) 



TODO_MM: Are we fine with this being just a numeric ID? A helper list of all prod IDs would eventually be much too large. We could add ghost text for the (Multiple Products) to keep it somewhat parallel to the rev acct entry below.

Matthias Miller 12/16/2025: TODO_SETH: Yes, but:

  * Can we copy the product description into the description?
  * And also set the price?
  * I'm very confused on the behavior of SalesFormProductEntry
  * SalesFormCashSaleRevenueAcctEntry should not show multiple accounts for 0 pipe list items :-)


  * Cash Sale Revenue Account (list of all income accounts for the accounting company; entry macro; if there are multiple Cash Sale Revenue Accounts in the RG, displays "(Multiple Accounts)"; when an account is selected, sets account for all rows in the RG)



RG:

Columns:

  * Description (plain text; set to product description when invoice is created from product)
  * Product (number; no decimals; custom field; required; error on save if not a valid product ID; if there is only one Product in the RG, defaults to that Product when the row is created)
  * Taxable (checkbox; defaults to checked ...)
  * Price (number; two decimals)
  * Cash Sale Revenue Account (list of all income accounts for the accounting company; if there is only one account in the RG, defaults to that account when the row is created)



  


  * Subtotal (...)
  * Tax (...)
  * Total Amount (...)



  


  


  * Invoice Matthias Miller 10/09/2025: TODO_SETH - put in spec and delegate Seth Miller 10/09/2025: Nic will code. I need to update the spec yet.
    * needs accounting company field; populate when creating from building
    * populate the first line item description to the product description
    * narrow the description column and add a column to the far right
      * add the Cash Sale Revenue account to the accounting impact and populate it in the row
      * do the same autopopulate if it's the same for all rows. 
    * Product ID should autopopulate if it's the same for all rows. If not, it shouldn't. Move it to the right of description so this works better.



Seth Miller 01/27/2026: This feels out of date.

  


  


  


Overview: The Solution includes the standard Silverloom Invoices Module for invoicing. This includes the standard Invoice record pages and the standard Invoices report (see corresponding section of the proposal). Note that any customizations are noted as such in the spec. 

  


Accessed via: 

  * "View Invoices" report
  * Home | Invoices | New Invoice (opens a new Draft invoice record, with "Invoice Date" set to the current date) 



  


Sections and Fields: 

  * "Header" standard section:
    * Invoice # <#> (located in the section header as the section label; number; auto-set sequentially; read-only; this number is the unique identifier for the record) 
    * Contact (required; drop list of all active Contacts)
    * Address (line 1; plain text; auto-sets to the primary Address for the selected Contact, but remains editable)
    * ... (ellipsis button; opens a choice report to select an address from the selected Contact)
    * Line 2 (plain text; auto-sets to the primary address for the selected Contact)
    * City (plain text; auto-sets to the primary address for the selected Contact)
    * State (no label; drop-list of state abbreviations; auto-sets to the primary address for the selected Contact)
    * Zip (no label; plain text field for zip code; auto-sets to the primary address for the selected Contact)
    * Ship to Separate Address (checkbox; displays a second, identical set of address fields)
    * Invoice Date (required; date; defaults to the current date)
    * Status (required; drop list of "Canceled" / "Draft" / "Invoiced" / "Paid"; with the following details / behaviors: 
      * defaults to "Draft"; 
      * when set to "Paid", "Payment Date" is set to the current date)
    * Payment Date (date; required if "Status" = "Paid"; auto-sets to the current date when Status is set to "Paid"; does not auto-clear) 



  


  * Itemization standard section:
    * Itemization (no label; embedded spreadsheet with the following: 
      * Columns: 
        * Date (optional date field; defaults to blank; visible based on "Invoice Includes Line Item Date" system switch; defaults to hidden) 
        * Quantity (number; no decimals; visible based on "Invoice Includes Line Item Quantity" system switch; defaults to hidden)
        * Code (drop list of "Code" items from Sales Item records; visible based on "Invoice Includes Line Item Code" system switch)
          * If "Invoice use code lookups" system switch is set to "Yes", the following fields are set when Code is set:
            * Description
            * Quantity
            * Price
            * Taxable
        * Description (plain text; width varies according to other included columns) 
        * Taxable (checkbox; visible if "Include Invoice Sales Tax" system switch is "Yes" or system switch is "No" and row already had "Taxable" checked; defaults to checked if visible) 
        * Unit Price (number; two decimals; visible based on "Invoice Includes Line Item Quantity" system switch)
        * Price (number; two decimals; label controlled by "Invoice line item price label" system switch) 
      * Automatically sorted by: "Date" (earliest at the top) N/A 
      * Buttons to add/remove rows (visible if Invoice "Status" = "Draft"): "✚" / "🞭" 
      * Shows 10 rows without scrolling
      * Other Notes: 
        * N/A)
  * To edit line items, the status must be changed back to 'Draft'. (visible if "Status" ≠ "Draft"; on-screen message in gray font) 
  *  Sub Total (read-only macro; displays the sum of all "Price" values for all rows on the Itemization embedded spreadsheet; visible __) 
  * Tax (underlying name is "Tax Rate Entry"; read-only macro; displays __; displays as "<Tax Rate>% of <__> ="; visible __)  
  * Invoice Tax (no label; read-only macro; displays __; visible __) 
  * Total Amount (read-only macro; displays the sum of "Amount" values for all rows in the Itemization embedded spreadsheet)
    * Total Amount (read-only macro; displays the sum of the following: <Sub Total> \- <Sales Discount> \+ <Invoice Tax> \+ <Late Fee>, rounded to the number of decimals specified in the "Invoice max decimals" system switch) 



  


  * Terms (__



  


  * View Invoice standard section:
    * View as PDF (button; opens the invoice as a PDF in a new tab)
    * View in Word (button; opens the invoice as a Word document) 



  


  


  * Notes for Customer standard section:
    * Contact Notes (no label; rich text memo) 



  


  


  * Internal Notes standard section:
    * Internal Notes (no label; rich text memo)



  


  


Modification History: This contains the following standard feature(s) for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access:

  * Visibility: Visible if the the user has the "View Invoices" permission (standard) 
  * Editability: Editable if the user has the "Edit Invoices" permission (standard) 



  


Special Considerations: 

  * Copy Record: allowed with edit permission (standard) 
  * Delete Record: if Status is "Draft" or "Cancelled" (standard) 
  * Merge Record: allowed with edit permission (standard)



  


Other Notes:

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked. 
  * Unless otherwise noted, all fields that become hidden for any reason (based on other fields, user permissions, etc.) retain their values. If they should be cleared, that is noted specifically in the field specs, with a "clear if hidden" or similar note.


