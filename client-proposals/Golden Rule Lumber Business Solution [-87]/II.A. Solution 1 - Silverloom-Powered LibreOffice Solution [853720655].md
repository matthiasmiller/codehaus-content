2.1. Solution 1 - Silverloom-Powered LibreOffice Solution

This solution would use the Silverloom software, accessible via customized LibreOffice spreadsheets that are synchronized through a Raspberry Pi.

  


Example File Structure:

  * Contacts.ods - a spreadsheet with a row per contact, with columns for things like contact type, name, billing address, mailing address, shipping address, phone numbers, etc.



  


  * Items.ods - a spreadsheet with a row per item, with columns for things like item type, code, name/description, Vendor 1 Name + Cost, Vendor 2 Name + Cost, etc



  


  * Purchase Orders - a folder with spreadsheets that include columns for things like vendor, item code, description, quantity, price, etc. Include checkboxes to print, email, or fax.
    * Purchase Order Template.ods - used to create new POs.
    * 0001 - 2024-02-01 - Vendor 1.ods
    * 0002 - 2024-02-04 - Vendor 2.ods
    * 0003 - 2024-02-14 - Vendor 1.ods
    * etc



  


  * Quote Request, Estimate, Sales Order, Invoice - folders with spreadsheets that are formatted very similarly to Purchase Orders



  


  * Payments.ods - a spreadsheet with multiple rows per payment with columns for customer, date, invoice #, amount, deposit date, etc.



  


  * Deposits.ods - a spreadsheet with multiple rows per deposit with columns for customer, payment ID, etc.



  


  * Point of Sale
    * The Point of Sale would use an Invoice template that could be prefilled. To scan items, simply use a Zebra scanner and enable the Enter key after the barcode. The cashier would fill in the customer information. The spreadsheet could be programmed to show a list of customers in the main list, as well as do a lookup from another sheet for item information. It could do calculations for local sales tax information as well.



  


  * Check Printing
    * Check printing would be handled via auto-generated PDFs that would be dropped in the correct folder to be printed manually, OR the Raspberry Pi would have a printer connection to automatically print these.



  


  * Reports
    * User A
      * Request.ods - a spreadsheet with a list of all available reports, along with special criteria, and a "Request" checkbox. Saving the file would trigger a request to Silverloom for the report, which would be placed in the user's folder. It would clear the "Request" checkbox in Request.ods. Example reports include Sales by Customer over a time period, plus all standard accounting reports including Income Statement / Profit & Loss, and Balance Sheet.
    * User B
    * User C



  


Major Considerations:

  


  * Error Handling. The Silverloom platform has error handling for invalid inputs into the software. This solution needs to appropriately handle this information. Invalid information cannot be stored in Silverloom. For example, if we could track the user correctly, we could use this to notify that user of validation errors. Alternatively, we could have a spot in the spreadsheet for Errors + a summary document of all items with validation errors.



  


  * ID Assignment. The Silverloom platform assigns IDs to all new records. One approach is to require users to close the document before it gets pushed to the server. This would allow the Raspberry Pi to temporarily mark it as read-only, assign a temporary ID, push it to the server, and save the changes back to LibreOffice.



  


  * Permissions. It would be ideal to have a standard permissioning structure, similar to what is used by Classic Accounting. This could be approached a few different ways. For example, these users could be configured in Silverloom. All changes would be tracked via LibreOffice metadata. Alternatively, the entire folder structure could be cloned for each user, with SMB authentication to lock down access to folders. The Raspberry Pi could also potentially sync view/edit file permissions based on permissions configured in Silverloom. Push comes to shove, it might mean simply enforcing area-specific passwords locally in the Golden Rule Lumber office. However, this requires passwords to be shared among multiple people and may inadvertently result in the wrong people getting access to the wrong permission.



  


Additional Considerations:

  * Check Printing (see above)
  * Purchase Orders (currently only used to make it easy to generate & print)
  * SKU UOMs (not used currently but would be nice for the future)
  * Bank Reconciliation
  * Accounting Classes (not used currently but would love to use them)
  * Accrual Based accounting (invoice is finalized when item leaves the yard)



  


Non-Issues

  * SKU Price Calculations (not used currently)
  * Asset Management (tracked externally now)
  * Recurring / Automatic / Memorized Transactions (CA does not support)
  * Credit Card Payments (done separately now)



  


Pros:

  * It could be expanded to include additional features, such as scheduling, etc.
  * It could leverage all of the existing accounting & inventory framework that exists in Silverloom
  * Accountants can have easy access to the Silverloom cloud solution



  


Cons:

  * It requires special thought on how to enforce permissions.



  


Cost:

  * Upfront Investment: Estimated $200k - $300k over 1-2 yrs (requires additional design to increase certainty)
  * Ongoing Maintenance & Support: $30k - $45k per year


