8.4.1. Packages

  


Requirements

The Package is a specific category of SKU that specifies the materials and miscellaneous charges used for each specific recipe. For example, apple butter might be produced in 8oz, 12oz, and 16oz jars.

  


Each Package is specific to one Recipe.

  


  * Package section:
    * Recipe (required; drop list of recipes, displayed as "<Recipe ID> \+ <Description>)
    * SKU (automatic & read-only; must be unique; first 3 digits of the Recipe SKU, followed by the last 2 digits of the Container SKU - i.e. first Material item)
    * Description
    * Pounds / Case (number; 2 decimals)
    * Recipe Weight (automatic & read-only; total pounds from recipe, excluding items without a weight)
    * Case Yield (automatic & read-only; this is the number of cases in each batch for this package; i.e. total ingredient weight / pounds/case)
    * Ingredient Cost / Case (automatic & read-only; total ingredient cost / case yield)
    * Daily Basis (i.e. number of cases produced per day)
  * Materials section:
    * Materials; embedded spreadsheet of:
      * SKU (list of SKUs; Categories TBD)
      * Description (automatic)
      * Amount (number; 2 decimals)
      * UOM (list of UOMs for SKU)
      * Cost Unit (automatic & read-only; UOM Cost from SKU)
      * Cost (automatic & read-only; Amount * Cost Unit)
    * Material Subtotal (automatic & read-only; sum of costs)
    * Material Margin (automatic & read-only; Material Subtotal * Material Margin % setting)
    * Material Total (automatic & read-only; Material Subtotal + Material Margin)
    * Note: Include validation to require there to be one item from the Container SKU Category.
  * Miscellaneous section
    * Embedded spreadsheet of:
      * Rate (list of "Per Day" or "Per Case")
      * SKU (list of SKUs; Categories TBD)
      * Amount (number; 2 decimals)
      * UOM (list of UOMs for SKU)
      * Cost Unit (automatic & read-only; calculated from SKU)
      * Case Rate (automatic & read-only; Cost Unit for Per Case; otherwise, Cost Unit / Daily Basis)
    * Miscellaneous Total (sum of all case rates)
  * Price / Case (automatic & read-only; sum of Material Total and Miscellaneous Total)
  * Stacking (wide single-line text)
  * Package Summary (wide single-line text)



  


NOTE:

  * When renumbering a Recipe or Container, all related Packages must be renumbered as well.
  * Even though the documentation mentions a line changeover charge, this is no longer added as a single charge to the invoice. Instead, it is calculated into the price of the package through the Miscellaneous section.
  * Packages can reference other packages, as long as that package doesn't reference additional packages. (This is used to handle situations such as salsa, which share the same base but have additional ingredients to handle mild, medium, or hot.)



  


Development Specification

TODO_IDD: Does "Case-mark" need to be fielded on the Package? And/or how does it get generated?
