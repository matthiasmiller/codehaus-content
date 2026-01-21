12.1. Sage

Sage will be imported from a csv that includes the following headers:

  


  * SONumber: Sales order number, a 5-digit integer (e.g., 78542).
  * OrderDate: Date the order was placed, in the format YYYY-MM-DD HH:MM:SS.000 (e.g., 2025-02-10 00:00:00.000), with millisecond precision.
  * DueDate: Date the order is due, in the same format as OrderDate (e.g., 2025-03-03 00:00:00.000).
  * OrderStatus: A single-character code indicating the status of the order (e.g., O for "Open").
  * ItemCode: A code for the item, alphanumeric and variable length (e.g., AHF-1).
  * ItemCodeDesc: Description of the item, a text string that may include measurements and codes (e.g., 37-1/2 x 26-1/2 #234300).
  * CustomerName: Name of the customer, a text string (e.g., AHF Products).
  * QuantityOrdered: Amount ordered, a decimal number with 6 decimal places (e.g., 160.000000).
  * UnitPrice: Price per unit, a decimal number with 6 decimal places (e.g., 10.140000).
  * QtySold: Quantity sold, a decimal number with 6 decimal places (e.g., 2920.000000).
  * TimesSold: Number of times the item was sold, an integer (e.g., 12).
  * SalesOrderHeaderUpdatedDate: Date the sales order header was last updated, in the format YYYY-MM-DD HH:MM:SS.000 (e.g., 2025-02-10 00:00:00.000).
  * SalesOrderHeaderUpdatedTime: Time of the last sales order header update, a decimal number representing hours with precision to 5 decimal places (e.g., 12.77538, likely hours and fractions of an hour).
  * InventoryItemUpdatedDate: Date the inventory item was last updated, in the format YYYY-MM-DD HH:MM:SS.000 (e.g., 2025-01-31 00:00:00.000).
  * InventoryItemUpdatedTime: Time of the last inventory item update, a decimal number with precision to 5 decimal places (e.g., 9.42318, likely hours and fractions of an hour).



  


Columns will be matched by header name.
