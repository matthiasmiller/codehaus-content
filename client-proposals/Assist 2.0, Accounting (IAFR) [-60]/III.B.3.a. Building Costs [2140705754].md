3.2.3.1. Building Costs

  


Requirements

Add an FGI Breakdown section to the building record. It would be an embedded spreadsheet within the Pricing section with:

  * FGI Category (required; FGI Cost Categories)
  * Standard Cost % (copied from the district record)
  * Standard Cost $ (automatic; Manufacturer Price * Standard Cost %; includes "Labor Intensive Amount" for Production Labor)
  * Freeze Standard Cost as Actual Cost (checkbox)
  * Actual Cost Date (date that cost was calculated)
  * Actual Cost $ (number; 2 decimals)
  * Actual Cost Variance $ (automatic; Actual Cost $ - Standard Cost $)
  * Accounting COGS Basis (list of "Standard Cost" or "Actual Cost")
  * Accounting COGS Cost $ (automatic; Standard Cost if basis is Standard Cost; otherwise Actual Cost)
  * Accounting COGS Variance $ (automatic; Actual Cost $ - Accounting Cost $)



  


The "Freeze Standard Cost as Actual Cost" will be set automatically based on the builder's settings. When checked, the Actual Costs will become read-only and will reflect the Standard Cost.

  


Change BuildingInventoryAmt to use the overridden inventory number if specified. Otherwise, it should calculate it from the "FGI Breakdown". Make sure these numbers are frozen historically.

  


When doing this, make sure the following reports continue to function as expected:

  * Production | Buildings | Finished Goods Inventory
  * Production | Buildings | Finished Goods Summary
  * Phone Menu Dashboard Stats ([https://insite.apphosting.zone/Reports/Standard/Std_Dashboard_Stats](https://insite.apphosting.zone/Reports/Standard/Std_Dashboard_Stats))



  


NOTE:

  * Buildings will enter and leave FGI as currently specified in Assist.



  


Development Specification

DONE_JN: I need to talk to you about how this affects inventory

  


DONE_JN: We need a way to freeze these numbers on sale.

Matthias Miller 05/01/2023: Done

  


DONE_HLD - give Josh an x30 to freeze accounting costs. Check w/ Duane to make sure they don't manually mark things delivered. If they do that, it should be a field change expression on the building record.

Matthias Miller 05/01/2023: Done

  


DONE_NM - Wait to update BuildingInventoryAmt until we have the rest of this stuff built out. Presumably break into separate job.

  


Niccolas Miller 04/25/2023: 

[[PC0153402]] - ZFP - FGI: Building Costs (T&M)

[[PC0153536]] - ZFP - FGI: Building Costs: Use Overridden Inventory Number (T&M)
