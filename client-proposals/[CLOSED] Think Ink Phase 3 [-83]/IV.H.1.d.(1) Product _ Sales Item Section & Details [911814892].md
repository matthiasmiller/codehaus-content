4.8.1.4.1. Product / Sales Item Section & Details

All Sales Items, regardless of Category, will include the standard "Product / Sales Item" section, with some customizations. This tracks details about the Sales Item.  

  


  * Product / Sales Item section (standard section with standard and custom fields): 
    * Standard fields: 
      * Code (required; plain text field; validate against duplicates) 
      * Is Active (checkbox; defaults to checked) 
      * Description (plain text field) 
        * Customized for Think Ink:
          * required (to be used as the description for all sales items)
      * Category (drop list of Sales Items Categories)
        * Customized for Think Ink:
          * required
      * Unit Price (number; defaults to blank)
        * Customized for Think Ink:
          * required (to be used as the pricing for all sales items)
          * note that eventually this possibly could be auto-calculated based on the average cost of sales items purchased from vendors
      * Default Quantity (number; defaults to 1; if a decimal is entered, this automatically round to the nearest whole number)
      * Show in Sales Report (checkbox; defaults to checked)
      * Taxable (checkbox; defaults to checked)
      * Notes (memo; can be used for storing notes, images, documents, and links)
        * Note that if images are too large to display properly, they should be resized manually before pasting them into the memo. An online tool such as [https://express.adobe.com/tools/image-resize](https://express.adobe.com/tools/image-resize) can be used for this.
      * Income Account (optional; drop list of Accounts; ellipsis button to create/edit)



  


  * Custom fields: 
    * Inventory Group (drop list of Inventory Group list items)



TODO_JM: Tim Reitz 09/21/2023: are you good with this? should it be only for Supply items?

  * Inventory Item (checkbox; defaults to unchecked)



TODO_JM: are you good with this for tracking inventory vs. non-inventory? should it be only on Supply type items?

  * Vendor Part Number (
  * Cost (
  * Markup Formula (
  * UOM (



TODO_IDD: Tim Reitz 09/19/2023: user-editable list

TODO_EM: Tim Reitz 09/19/2023: Thoughts on allowing multiple UOMs for the same item? (i.e. paper sold by the case or by the ream) Or would it make more sense to simply have separate sales items for these since we're not tracking inventory? 

  * Subcategory (required; drop list of Sales Item Subcategories with the option to add a new one; defaults to blank) 



TODO_JM: Tim Reitz 09/21/2023: For all Sales Item types/categories, or just supplies?

  


TODO_EM: Tim Reitz 09/19/2023: There's also a scenario where the manufacturer offers a discounted price for MPS Business customers (not homeowners). There are 2 different prices for the same item, depending on the customer. This then ties into TI's Purchase Orders back to the manufacturer. Thoughts on how to handle this? 

This ties into accounting - we need to discuss this as well (does AHZ handle PO's?).

  


Supply: 

  *   * Attachments (custom RG to include images, PDFs, and other files) 



TODO_EM: Tim Reitz 09/21/2023:  should this be an RG with S3 integration? or a field for a link to Google Drive? Let's discuss this again later.
