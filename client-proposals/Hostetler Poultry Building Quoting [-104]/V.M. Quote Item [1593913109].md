5.13. Quote Item

  


Requirements

Name & Categorization:

  * Name / Description
  * Active: boolean



  


Alternative For (list of Quote Items)

  


Category (read-only for alternative items):

  * Bird Area Equipment -> Chain Feeders -> Chain Feeders for Layer -> Winching



  


Sort Order Within Category (read-only for alternative items)

  


Include on Cover Sheet (checkbox; read-only for alternative items)

  


Cover Sheet Description (visible & editable if included on cover sheet; quote-level string expression; i.e. "60' x 10' x 6" Concrete Approach on End of Barn"; read-only for alternative items)

  


Quote Item Tags (multi-choice list)

  


Quantity & Dimensions

  * Quantity Label (optional; list of Quantity; read-only for alternative items; blank = no quantity adjustment)



  


  * Default Quantity: number expression (Quote-level; read-only for alternative items) Available Macros: * For Quantities: * IndividualQtyForSpecificItem("Other Item") * CombinedQtyForSpecificItem("Other Item") * IndividualQtyForItemOrAlternative("Other Item") * CombinedQtyForItemOrAlternative("Other Item") * For Dimensions: * DimensionForSpecificItem("Other Item", "Sidewall Height") * DimensionForItemOrAlternative("Other Item", "Sidewall Height") * DimensionForParentCategory("Category Name", "Sidewall Height") * For Calculations: * QuoteCalculation("Number of Trusses")



  


  * Dimensions; embedded table of up to 3 dimensions editable by sales; read-only for alternative items
    * Dimension (list of Quote Dimensions)
    * Editable by Sales (checkbox)



  


  * Requirements (embedded table of:
    * Type; list
      * Require If
      * Disallow If
    * Check for (list of: Integrator, Other Tags, Specific Quote Item, Quote Item or Alternative)
    * Operation (list of: includes, does not include)
    * Value (based on "Check for")
      * Integrator (list of Integrator)
      * Other Tag (list of tags)
      * Other Quote Item (list of Quote Items)



  


  * Bill of Materials; embedded table of included items:
    * SKU
    * Qty (quote-level number expression; required)
    * Cost (auto-calculated)
    * Markup % (auto-calculated)
    * Price (auto-calculated)



  


  * Total Material Cost (auto-calculated)



  


  * Total Material Markup % (auto-calculated)



  


  * Total Material Price (auto-calculated)



  


  * Labor $ (quote-level expression)



  


  * Last Updated: timestamp



  


Notes:

  * Quote item names must be unique. This might require some renames from the Excel file.
  * Variations on insulation and garage door options can be handled by different Quote Items.
  * The BOM for the building will be tied out to a "base building" item that will be excluded from the cover sheet.
  * Custom Overhead Doors do not tie out to an inventory item, so we can use subitems to adjust pricing for custom doors (panels, size, windows, etc)
  * Bi Fold Doors in the building section are for framing & trim. Bi Fold Doors in the equipment section are for the actual door & hardware. To support this:
    * The default quantity on the building's Bi Fold door is based on the equipment's Bi Fold door.
    * The building Bi Fold doors will get renamed to "R.O for -----" (i.e. Rough Opening for ------ Bi Fold doors)



  


Development Specification

TODO_IDD - Use it for the pick list
