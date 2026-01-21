3.4.3. Customer Discounts Category

  


Requirements

Each Multiple Run Discount and Special Discount item would have a separate Sales Item detail page in the Customer Discounts category where its specific details would be configured. This will allow for linking to invoices and for sales reporting.

  


The Customer Discounts detail screen will have the following sections and fields:

  


Sales Items Section:

  * Code (required; text field; validate that the Publication Code is included at the end; validate against using the same base Code+suffix more than once in the system)
  * Is Active (checkbox, default to filled; when deactivating, validate that the Sales Item is not being used)
  * Description (required; text field; validate against using the same description more than once in the same publication; the percentage amount should be included here for reference)
  * Category (required; list of Ad Sizes, Discounts, Other)
  * Show in Sales Report (optional; checkbox; default to cleared)
  * Default Quantity (optional; default to blank)



  


Publication Details Section:

  * Publication (required; for Publication Admin, default to assigned publication and read-only; for Full Admin, list of publications, defaulting to blank, with validation against changing if the item is being used)
  * Publication Code (read-only; auto-filled based on Publication; display after the Code)



  


Discount Details Section:

  * Discount % (required; number field; to 2 decimal places)



  


Development Specification

Price Fields: Tim Reitz 02/17/2021: Our proposal is to use a custom field on the Sales Item for the the Discount % and not allow a standard price. If invoicing manually, price will be blank (enter manually). 

Tim Reitz 02/17/2021: We should probably think through this more. Maybe add a Discount Column to the Invoice (either the Code or %)?
