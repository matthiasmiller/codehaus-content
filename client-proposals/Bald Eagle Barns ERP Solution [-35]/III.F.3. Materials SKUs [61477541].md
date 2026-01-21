3.6.3. Materials SKUs

  


Requirements

Materials SKUs are the most basic/foundational of the SKUs/SKU categories. Materials are used to construct Options and Buildings. Examples of Materials are things like 2x4s, plywood, screws, etc.

  


Phase 1 of this project does not include tracking inventory quantity for materials, but is does include tracking costs and prices. 

  


Options SKU records should have the following custom sections and fields:

Materials SKU Details section: 

  * Requires Special Order (checkbox) 
  * Board Feet



The Materials SKU will show number fields for Thickness (in.), Width (in.), and Length (ft.). This will have a button beside it called "Update UOMs". It will replace any existing UOMs for the SKU to the following UOMs and multipliers:

  * PCS with a multiplier calculated from Thickness (in.) * Width (in.) * Length (ft.) 
  * BFT with a multiplier of 12
  * MFT with a multiplier of 12,000



  


For example, a 2x4x8 would use the following multipliers:

  * PCS = 64
  * BFT = 12
  * MFT = 12,000



  


If priced at $1000/MFT, this would be converted using:

  * MFT Price / MFT Multiplier * PCS Multiplier
  * $1000 / 12,000 * 64 = $5.33/pc



  


These would be rounded to 2 decimal places at the final step of the calculation. The pricing can be entered on the Sales Lot record using any unit of measure. This allow us to convert both the materials from MBF to pieces and the price from $/MBF to $/piece. 

  


Materials SKUs should have the "Inventory" section with the "Sales Lots" link. For now only one Sales Lot would be used per Materials SKU. 

  


Materials SKUs also should have the "Alternate UOMs" button and child screen.  

  


Other Notes: 

  * If an Option SKU or Building Style SKU includes one or more Materials SKUs that requires Special Order, then the flag should throw on the Work Order (see corresponding section of the proposal). 
  * Explanation about "Requires Special Order": Some materials aren't stocked (kept in inventory), and those SKUs should be marked as "Requires Special Order". If an Option or Building Style includes one or more Materials SKUs requiring Special Order, selecting that Option or Building Style on an order will throw a flag on the Work Order when it is created (see Work Order Record section of this proposal), showing that something needs special order. This notifies the Purchaser (see Special Order Email for Purchaser section). When the Purchaser orders the item, he marks it as Ordered. When it comes in, either the Shop Manager or Purchaser marks it as arrived and the flag is cleared.



  


*Done.

  


Development Specification

Mockup: 

Materials SKU: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=451049632](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=451049632)

Alternate UOM Child Screen: [https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1311478707](https://docs.google.com/spreadsheets/d/1QDfhJsb9R2t3m7P-jnaljWfYJbscNJiLwyZCiXcOXV0/edit#gid=1311478707)

  


  


TODO_CCI: should we give them an editable report similar to the Edit Inventory report for ZTD, for easier price editing?
