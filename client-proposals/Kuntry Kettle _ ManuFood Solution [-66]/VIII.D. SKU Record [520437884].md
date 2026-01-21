8.4. SKU Record

  


Requirements

ManuFood will include the standard AppHosting.zone SKU, including:

  * SKU Category 
  * SKU
  * Description
  * Display UOM
  * Units of Measure (UOM; defines ratios of UOMs as a multiplier)
  * Notes



  


Customizations for Kuntry Kettle:

  * Supplier (list of Suppliers)
  * FOB UOM (list of UOM's on SKU)
  * FOB Cost (number; 2 decimals)
  * Freight UOM (list of UOM's on SKU)
  * Freight Cost (number; 2 decimals)
  * Price / ____ (FOB Cost + Freight Cost based on Display UOM)
  * Price / ____ (FOB Cost + Freight Cost based on Measure UOM or Smallest UOM)
  * Allergens (drop list of Allergens; allow adding to the list)
  * Production Points (number; 2 decimals)
  * Reorder Level (number)
  * Optim. Reorder Qty (number)
  * Require Certificate of Analysis (checkbox)
  * Display UOM (i.e. bag, drum, case, box, etc in a pallet)
  * Measure UOM (i.e. # of pounds in unit, or # of drops in a bottle)



  


Kuntry Kettle will be using the following Units of Measure for their SKUs:

  * Truckload
  * Stack (vertical stack within a truckload)
  * Pallet (number of pallets in a stack; normally 1-2)
  * Day (used for costs such as production overhead)



  


Development Specification

TODO_JN - Any objection to making Retail Price optionally be a dated RG? Or always?

Matthias thinks we will need to do this - turn the SKU Retail Price into a dated RG. 

Tim Reitz 12/20/2022: Is this the "Price" fields? I don't see Retail Price in the specs above. 

  


  


TODO_IDD: set up a Snippet for SKU Record

TODO_IDD - Confirm that the Price / ____ is using the right UOMs
