4.3.7. NG Order Record

  


Requirements

Overview: This record is a read-only copy of the data from the NexGen Order record.

  


This is a custom record. 

  


Read-Only NG Field:

  * Silverloom Internal ID (automatic number)
  * Order Number
  * Order ID
  * Order Line ID
  * Customer ID
  * Formula ID
  * Ordered Quantity
  * Loaded Quantity
  * Loaded Date
  * Location ID
  * Ingredients; embedded spreadsheet of:
    * Ingredient Item ID
    * Incredient Qty (pounds)



  


Development Specification

NOTE: The EAI (for NG) does not provide ingredients for items. However, it does include them on orders.
