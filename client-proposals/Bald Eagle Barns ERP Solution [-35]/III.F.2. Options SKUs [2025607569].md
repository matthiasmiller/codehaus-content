3.6.2. Options SKUs

  


Requirements

Option SKUs are used to track the various "options", or add-on features, for the buildings. Option SKUs are composed of materials (the "Option Assembly") and labor (the "Option Tasks"), with some other custom fields as well. Options can be added to a Building Style SKU or to a Building record. 

  


Options SKU records should have the following custom sections and fields:

Options SKU Details section:

  * Option Code for Serial # (optional; must be a single letter; used for building Serial Number)
  * Piece Work Base Price (required; number field to 2 decimals; abbreviated to "PWBP"; used for member payments; changes to the PWBP should be updated on all current and future Buildings and Sales Orders EXCEPT for those with a status of Sold or beyond) 
  * Diagram Shape (optional; drop list of Shape Names from the shape catalog; would be left blank for items that are not included in the building diagram; see the corresponding section of this proposal)
  * Taxable (checkbox OR Yes/No droplist) 
  * Default to Building Size (checkbox; visible if UOM = Sq Ft; if filled, the Qty for the option should default accordingly when added to the options on a Base Building SKU or a Building Record)



  


Option Tasks section: This is used to track all Tasks to be completed for the completion of the Option: 

  * Tasks (embedded spreadsheet with the following:)
    * Columns:
      * Task (required; drop list of all Task Types; filters down as you type)
      * Manufacturing Dept. (auto-fill and read-only)
      * Sequence # (auto-fill and read-only)
    * Sort by: Manufacturing Dept, then Sequence #
    * Show at least 5 rows without scrolling
    * Buttons to add/remove rows ("+" and "-")
  * New Task Type (link that opens a new blank Task Type record in a new tab; after the new Task Type is saved, it should appear on the Name list) 



  


Option Assembly section: This is used to track all Materials that should be included for the completion of the Option: 

  * Option Assembly (embedded spreadsheet with the following:)
    * Columns: 
      * Item (required; drop list of Materials SKUs; filters down as you type) 
      * Unit of Measure (auto-fill and read-only) 
      * Qty (required; number to 2 decimal places)  
      * Special Order? (checkbox; auto-fill and read-only) 
    * Sort by: Item 
    * Buttons to add/remove rows ("+" and "-")
  * Message: Note: The Qty is for each Square Foot of the Option. (if Option UOM = Square Foot) 



  


Other Notes: 

  * There should be a pre-set "Custom" Option, for which a Salesperson can customize the description and the price on a Building. Note that Diagram Shapes, Tasks, and Assembly cannot be associated with "Custom" Options.
  * For Options that have Sq Ft as their UOM, the Qty of the Assembly will be per square foot of the Option.
    * Example for a shelf or workbench: 

Item| Unit of Measure| Qty| Special Order?  
---|---|---|---  
AdvanTech | Square Feet | 1|   
  
2x4 | Piece | 0.143|   
  
  
  


  


*Done.

  


Development Specification

Example for a window Option: 

  * Option code: 3640DH 
  * Diagram Shape: Window Rectangle 
  * Requires Special Order: True
  * Tasks: 
    * Frame window
    * Install window
    * Install window trim
    * Paint window trim
  * Assembly:  
    * Window unit
    * Trim
    * Caulk
    * Paint
    * Screws



  


NOTE: The "Custom" Option would be the same idea as the Add New/CUSTOM feature for Lumber and Metal items in ZTD.

  


Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=396316424](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=396316424)
