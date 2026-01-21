8.10. Work Orders Record

  


Requirements

Work orders are a single batch of a recipe from a sales order.

  


  * Type (required; drop list of Made to Ship, Made to Stock) 
  * Recipe (required; drop list of Recipes)
  * Packages; embedded spreadsheet of:
    * Package ID (list of packages from Recipe)
    * Customer (editable if Recipe's customer is blank; otherwise, automatic & read-only)
    * Label (editable if Package's label is blank; otherwise, automatic & read-only)
  * Ingredients & Materials; embedded spreadsheet of:
    * SKU 
    * Description (automatic and read-only)
    * Amount (automatic and read-only; from recipe)
    * UOM (automatic and read-only; from recipe)
    * Pounds (automatic and read-only)
    * Lot Numbers (list of lots for the ingredient)
    * Qty Used
    * UOM Used (list of UOMs from SKU)
  * Yield (number)
  * Yield UOM (list of UOM)
  * Test Results; embedded spreadsheet of:
    * Test (list of tests)
    * Test Result (number; 0-2 decimals)
    * Expected Range (number; automatic & read-only)
  * Scheduled Production Date (date)
  * Lot Number
  * Completed Production Date (date)



  


Other Notes:

  * The lot number must be unique. It is based on an optional customer-defined value, the 3-digit product number, a single-digit year, a 2-digit month, a 2-digit day, and a batch character (starting with A for the first batch assigned to the day, B for the second, etc.).
  * Validate that the log number is unique across work orders.
  * This will create an inventory adjustment for ingredients and materials when the work order is completed.
  * This should also create an inventory adjustment for the finished good, which will be adjusted by the sales order when Made to Ship items are sold.
  * Kuntry Kettle is planning to use a hand-held device to track lot numbers of all ingredients used for a work order.
  * The work order would have the ability to rescale the recipe based on a single ingredient.
  * If there's more than a 2% discrepancy of Qty Used (based on a system-wide setting for Maximum Ingredient Variation %), have an option to either rescale the recipe or accept the discrepancy.



  


Development Specification

TODO_IDD: Determine details for Made to Stock vs. Made to Ship, such as: 

  * What are the differences in workflow, pricing, tracking, etc.? 
  * Does Made to Stock need a Sales Order? 
  * Is whitelabeling included in one of these, or its own type?



  


TODO_IDD: Consider adding an entry to the work order / spec sheet to flag manually rescaled orders?

  


TODO_IDD: Why do we need multiple packages? Is this only for the salsa, for example?
