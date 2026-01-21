3.4.5. Other Category

  


Requirements

The "Other" category of Sales Items would be used mainly for the Special Placement Charge at this point. This charge would have a Sales Item detail page where its specific details would be configured. This will allow for linking to invoices and for sales reporting.

  


The Other Items detail screen will have the following sections and fields:

  


Sales Items Section:

  


  * Code (required; text field; validate that the Publication Code is included at the end; validate against using the same base Code+suffix more than once in the system)
  * Is Active (checkbox, default to filled; when deactivating, validate that the Sales Item is not being used)
  * Description (required; text field; validate against using the same description more than once in the same publication)
  * Category (required; list of Ad Sizes, Discounts, Other)
  * Unit Price (required; number field to 2 decimal places)
  * Show in Sales Report (optional; checkbox; default to cleared)
  * Default Quantity (optional; default to blank) 



  


Publication Details Section:

  * Publication (required; for Publication Admin, default to assigned publication and read-only; for Full Admin, list of publications, defaulting to blank, with validation against changing if the item is being used)
  * Publication Code (read-only; auto-filled based on Publication; display after the Code)



  


Development Specification

Tim Reitz 02/17/2021: Note that we are using the Unit Price field for this category.

  


Note that the Special Placement Charges do not get any of the regular discounts applied to it. However, the 2% discount applied if the customer pays within 10 days does apply to the Special Placement Charges.
