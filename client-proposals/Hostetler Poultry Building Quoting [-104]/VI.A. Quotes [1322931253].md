6.1. Quotes

Information:

  * Id: number
  * Contract ID -- if specified, the Cover Sheet is generated using all quotes with this contract ID (used to stitch together multiple buildings of different lengths, egg rooms of different lengths, etc)
    * WARN if the integrator/sales person/etc do not match the Contract ID
    * Include a link to view quotes tied to this contract
  * Quote Number: string (auto-generated)
  * Revision (number)
  * Customer: list (Active Contacts where Contact Type = "customer")
  * Salesperson: list (Active Contacts where Contact Type = "salesperson")
  * Integrator: list (Active Contacts where Contact Type = "integrator")
  * Project Name: string
  * Status: string (draft/submitted/approved/rejected/expired)
    * TODO - flesh out
  * Total: decimal (auto-calculated)
  * Location Address, City, State, Zip
  * Location Distance (Miles)
  * Freight Zone (auto-calculated based on location distance)



  


Settings:

  * Include Labor (checkbox)
  * GC Fees NOTE: Calculated from Materials + Labor (if the quote includes labor). Otherwise, it's calculated from Materials Only
    * Type (read-only)
      * Kit
      * Turnkey Table of:
    * Category
    * Default GC % (calculated based on kit/partial/full)
    * GC % Override (editable by special permission only)



  


TODO_IDD - GC Fees should only look at equipment.

  


Labor Upcharges:

  * By Default, add the first 3 rows, but allow manually adding more:



  


Category| Labor Upcharge %| Notes  
---|---|---  
Building|  16%| Equipment Rental  
  
  


TODO_IDD - Export from SmartBuild -> Silverloom, which would have a building total included in the export. And then the software we're building would create the payment schedule based on the grand total

  


Payment Schedule (embedded table; with the following:

  * Type (choices of Securement, Downpayment, Progress Payment, Final Payment)
  * Due Date (if known)
    * Securement - NA
    * Downpayment - 25 weeks prior to final date
    * Progress Payment - NA and/or manually filled in
    * Final Payment - NA and/or manually filled
  * Payment Date (when payment is received)
  * Payment % (number; 0 decimals)
  * Payment $ (auto-calculated)



  


Sample/Defaults Payment Schedule:

  * Securement Date & Payment
  * Down (20% minus securement amount)
  * Progress Payment (due on completion of roof; 75%)
  * Final Payment (5% due on project completion) *Requires approval for changes; custom dates & %'s *



  


Notes:

  * Allow individuals with certain permissions to add/remove/modify payment rows, including additional payments
  * Validate that all payment %'s add up to 100%



  


Items:

  * Filter To (list of categories & subcategories to quickly filter down Items)
  * Items (virtual embedded table);
    * Name
      * This is the name of the category or Item.
      * Categories have a background color (and font size if possible) based on depth.
      * Items are sorted to the top of a category. Subcategories are sorted within them.
      * Both items and subcategories are sorted based on sort order + name.
    * Include (checkbox)
      * Checking this box shows all child items/sections
      * Unchecking this box zeroes out all quantity overrides and hides the child items/categories.
    * Default Qty
    * Qty Override
    * Dimension 1 Label (1st dimension editable by salesperson)
    * Dimension 1 Value (blank/read-only if fewer than 1 dimensions)
    * Dimension 2 Label (2nd dimension editable by salesperson)
    * Dimension 2 Value (blank/read-only if fewer than 2 dimensions)
    * Dimension 3 Label (3rd dimension editable by salesperson)
    * Dimension 3 Value (blank/read-only if fewer than 3 dimensions)
    * Item Base Price (read-only)
    * Item Discount % (only available for items)
    * Item Price (read-only; auto-calculated via Discount %)
    * Customer Supplied Materials (editable if Quote Item allows it)
    * Salesperson Notes
    * Integrator Notes



  


Notes:

  * Hiding a parent category removes/hides all child categories & quote items.



  


Additional Materials:

  * Quote Category (must be included in quote)
  * Cover Sheet Description (string)
  * SKU (list of SKUs)
  * Qty (number)
  * Length (TODO_IDD - need to know how this works w/ SKUs)
  * Part Number (read-only; auto-calculated from SKU; TODO - This might be the SKU itself)
  * Price (read-only; Qty * SKU Price including markup)



  


Additional Items:

  * Quote Category (must be included)
  * Include on Cover Sheet (checkbox)
  * Cover Sheet Description
  * Material $
  * Labor $
  * Amount (positive or negative)



  


Internal Structures:

  * Hidden Table - Lines NOTE: Category or Quote Item must be set, but not both.
    * Category (list of Categories)
    * Quote Item (list of Quote Items)
    * Show (checkbox)
    * Qty Override (number)
    * Salesperson Notes
    * Integrator Notes
  * Hidden Table - Dimensions NOTE: Category or Quote Item must be set, but not both.
    * Category
    * Category (list of Categories)
    * Quote Item (list of Quote Items)
    * Dimension (list of Dimensions)
    * Value (number)
  * Hidden Table - BOM
    * SKU
    * Qty
    * Cost
    * Markup %
    * Markup $



  


Notes:

  * BOM Generation should exclude/note customer-supplied materials in the BOM generation
  * All categories MUST share the same dimensions. For example, you cannot have 2 buildings of different sizes, or 2 bird areas with different lengths. To generate a quote for differing size buildings or bird areas, you need to generates 2 quotes with the same Contract ID for a shared printout.
  * Sidewall selection will be 1 of 3 choices (Solid, Curtain, Bypass). The specific labor will be tied to that selection. This selection can drive the visibility of other items (such as curtain-specific questions).
  * Concrete for kits can be excluded using a default quantity expression



  


TODO:

  * Have an internal report that shows itemized pricing; cover sheet does NOT include itemized pricing
  * Need a way to freeze pricing at a certain point (and update if needed on a quote)
    * Could we freeze Qty & Price, and then just have a way to warn if default qty and ric
  * Handle package discounts



  


Note:  Any Ft/In dimensions are stored as whole inches but displayed as two separate fields (feet and inches)

  


TODO - consider how to handle. Do we need a "Dimension Type" with text/number conversions

  


TODO:

  * Discuss Change Orders and Change Order Fees



  


TODO:

  * Loads Pricing
    * Matthias Miller 11/13/2025: Just calculate freight as a factor of barn length & based on whetyher there's a packer included + mileage
    * # of loads calculated by length of barn
      * Calculated using Ranges... 
      * 500ft -> 5.5 load
      * 620ft -> 6.5
      * 740ft -> 7.5
    * mileage factor - based how many miles from wareless
      * Teirs - based on their feed delivery chart (they don't maintain, have a database with miles & the freight charge) -- generated based on fuel cost -- and if they don't access it, need to figure out what that calculation looks like
      * Spreadsheet that they have that is maintained by logistcs...



  


TODO - Earl will chase down whether outside access is needed for the spec sheet
