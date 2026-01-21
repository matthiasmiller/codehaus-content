22.3.5. Classic Accounting UOM Record (Read-Only)

  


Requirements

_EM: Tim Reitz 07/25/2023: Do we want to keep pursuing this as part of Phase 3 if we're looking at switching to apphosting accounting soon? 

DONE_IDD: Tim Reitz 07/25/2023: Not needed at this point. 

  


TODO_JM: how does CA do UOM? 

  


TODO_JM - do they only use multiply method for inventory units?

  


  


  


TODO_CH - for mapping

  * UOM = the base UOM; same as "Main Unit" in Classic Accounting
  * Alternate UOMs = other UOMs; the ones that are not the "Main Unit"
  * Display UOM = the Default Selling UOM



  


Sections and Fields: (all are auto-set and read-only):

  * ID (number)
  * Active (checkbox)
  * Create Date (date)
  * Default Selling (checkbox)
  * Main Unit (checkbox)
  * Mod Date (date)
  * Quantity (number, 4 decimals)
  * Unit Name (text)
  * Item ID (number)



  


Development Specification

DB Level: CA_Itm_Item_Unit

  


Fields:

CA_Itm_Item_Unit__ID (number)

CA_Itm_Item_Unit__Active (boolean)

CA_Itm_Item_Unit__DefaultSelling (boolean)

CA_Itm_Item_Unit__MainUnit (boolean)

CA_Itm_Item_Unit__ModDate (date)

CA_Itm_Item_Unit__Quantity (number, 4 decimals)

CA_Itm_Item_Unit__UnitName (string)

CA_Itm_Item_Unit__ItemID (number)

  


TODO_CH: Check the db level name to see if it's what you want.
