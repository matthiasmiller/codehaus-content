8.3. Recipes Record

  


Requirements

The Recipes record is used to track ingredients for customer recipes:

  * ID (numeric; user-entered; must be unique across all recipes)
  * Description (text)
  * Customer (optional; list of customers)
  * Picture of Product (rich text)
  * Intended Use / Market (rich text)
  * Lot Prefix (text, such as "RTG")
  * Ingredients (embedded spreadsheet of:)
    * SKU (list of SKUs; blank for instruction lines)
    * Description (editable if SKU is blank; otherwise, automatic & read-only)
    * Amount (number; 2 decimals)
    * Override Production Amount (checkbox)
    * Production Amount (number; 2 decimals; editable if Override Production Amount is checked; otherwise, blank)
    * UOM (list of UOMs from SKUs)
    * Pounds (automatic & read-only; if SKU has conversion to pounds)
    * Unit
    * Cost Unit (automatic & read-only)
    * Cost (automatic & read-only)
  * QA Tests (embedded spreadsheet of:)
    * QA Test (list of QA Tests)
    * Spec Min (number; 2 decimals)
    * Spec Max (number; 2 decimals)



  


NOTE:

  * The Test is used to determine the pH or the brix after the recipe has been mixed and when it's ready to fill.
  * The Production Amount needs to be overridden to allow changing citric acid levels based on the pH of the blackberries in stock (for example). This allows the printed recipes to update, but it will not affect the price.
  * If the SKU is blank, the Description column will be editable and all other columns will be read-only. These will be used for instructional lines.



  


Development Specification

TODO_IDD: Currently they are using "Lot" and "Batch" almost interchangeably, but there are some differences. We should clarify and standardize.
