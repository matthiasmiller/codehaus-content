3.6.1. Base Building SKUs

  


Requirements

A Base Building is just the basic building details with its standard options, as applicable. This is referred to as the "Item" in the old system. Base Building SKUs are used to determine the basic features of various building models and are used as a starting point for creating lot or customer buildings. Base Building SKUs are composed of Materials (the "Building Assembly"), Options, and labor (the "Tasks"), with some other custom fields.

  


Building Item Code/SKU Code: The Item Code for Base Building SKUs should be automatically entered and auto-updated in the standard SKU code field at the top of the record using the following format: Type Code (if applicable) + 2 digit width + 2 digit length + Style Code; e.g. "M1416VS". 

The SKU code field would be editable, but with a warning on Save if the code is out of sync with the building details: "The Item Code does not match the criteria of the building details."

  


Base Building SKU records should have the following custom sections and fields:

"Base Building SKU Details" section:

  * Building Style (required; drop list of Building Styles)
  * Style Code (auto-filled and read-only; based on the Building Style Code) 
  * Length (required; number field; whole number)
  * Width (required; number field; whole number)
  * Building Square Feet (auto-filled and read-only; Length*Width; includes the porch as the porch is set within the footprint of the building) 
  * Piece Work Base Price (required; number field to 2 decimals; abbreviated elsewhere as "PWBP"; used for member payments; changes to the PWBP should be updated on all current and future Buildings and Sales Orders EXCEPT for those with a status of Built/Sold and beyond)
  * Building Price/Sq Ft (auto-filled and read-only; Building Base Price/Square Feet) 
  * Porch Location (leave blank if no porch; drop list of the following:)
    * End (adds the porch to the left end/short side of the diagram, inset into the building footprint)
    * Side (adds the porch to the bottom left [of the long side] of the diagram, inset into the building footprint; can be moved to the bottom right on the diagram for the Base Building)
  * Porch Depth (visible and required if any porch location is selected; number field for feet; no decimals)
  * Porch Width (visible and required if Front Left or Front Right is selected; number field for feet; no decimals) 



  


"Standard Options" section:

  * Standard Options (embedded spreadsheet with the following:)
    * Columns:
      * Option (drop list of all Option SKUs)
      * Qty (required; number field; up to 2 decimal places) 
      * UOM (auto-filled and read-only)
    * Sort by: Option name
    * Show at least 5 rows without scrolling 
    * Buttons to add/remove rows ("+" and "-") 
  * New Option (link that opens a blank new Option SKU in a new tab; after creating and saving that SKU should appear on the Option list above)



  


"Layout Diagram" section:

  * Edit Layout Diagram (link to layout editor; must save SKU record before opening)
    * This would open the layout editor with the basic shape for the building and porch auto-generated from the entered information, and the standard options shapes - same as on a building record...
  * Layout Diagram (read-only memo that displays the layout diagram)



  


"Building Tasks" section:

  * Embedded spreadsheet exactly like the one for the "Options Tasks". It is used to track all Tasks to be completed for the construction of the building.



Note that Tasks for selected Standard Options will NOT show on this spreadsheet on the Base Building SKU, as those pertain specifically to the Options SKUs. However, all Tasks for a Building and its Options WILL show on the Tasks list on the Work Order for the Building record itself.

  * New Task Type (link that opens a new blank Task Type record in a new tab; after the new Task Type is saved, it should appear on the Name list) 



  


"Building Assembly" section:

  * Embedded spreadsheet exactly like the one for the "Options Assembly" that is used to track all the materials that are used in the building.



Note that materials for selected Standard Options will NOT show on this spreadsheet on the Base Building SKU, as those pertain specifically to the Options SKUs. However, all materials for a Building and its Options WILL show up on the Assembly list for the Work Order for the Building record itself.

  


Data Access: Fully editable for Admins; Salespeople can create & edit SKUs of the "Fully Custom Building" style. 

  


Other Notes: 

  * If the Building Style = Fully Custom Building, Salespeople will be able to edit the SKU details.
    * When a new Base Building SKU is created from a Building Record, if the user is only a Salesperson (not an admin), the Building Style drop list will only show the Fully Custom Building option. 
  * Notes about porches:
    * If a porch is automatically added on a building (included on the Base Building), the salesman would be able to drag the porch around when designing the building. 
    * If porch is moved from left to right, there is no charge; if moved from an end to the center, it's an upgrade fee. All of these should be done on a custom Option on the building record.
    * If a porch is resized, the customer is charged the base price for the 4' porch, with the additional being charged as an upgrade fee. This should be done on a custom Option on the building record.



  


*Done.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=113862918](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=113862918)

  


Models

  * Each model has a base price
  * And then to adjust that price, you have to add a line item option to adjust that price
  * 12x16 Side Lofted Barn (two windows, side entry door)  1216SLB item code -- will automatically pull the price for that base
    * If they want to add a radiant barrier (foil-backed roof decking and siding), add that as a separate side item
    * Add separate windows
  * Have a table in the background...
  * 12x16 High __ Barn



Some of these models have a higher sf price than others.
