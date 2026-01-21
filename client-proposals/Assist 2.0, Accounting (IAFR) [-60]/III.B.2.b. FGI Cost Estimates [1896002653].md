3.2.2.2. FGI Cost Estimates

  


Requirements

For context, each building has two costs:

  * Standard Cost (i.e. projected cost)
  * Actual Cost



  


Each district will have an embedded spreadsheet (migrated from Inventory Material %) of:

  * Effective Date (date; required)
  * Raw Material % (number)



  


The Company record (used for builders) currently has an embedded spreadsheet of Date and Building Inventory %. This will change to:

  * Effective Date (date; required)
  * Building Inventory % (number; keep until we fully migrate to FGI)
  * Production Labor % (number)
  * Production Overhead % (number)
  * Freeze Labor as Actual Cost (checkbox)



  


The "Freeze Labor as Actual Cost" will be used for subshops who do have fixed labor rates.

  


Migration:

  * When migrating, we need to make sure we don't lose old data. For example, we are keeping Building Inventory %.
  * We will want to provide a spreadsheet to Mark to be able to populate values for existing building records as needed.



  


Other Notes:

  * The Wholesale % on districts is NOT related to FGI numbers.



  


Development Specification

Ellis Miller 04/18/2023: 

  


Districts

[ ] Add Raw Material % RG (DONE: Figure out where Inventory Material % is)

  


Company Record:

[ ] Relabel the date field

[ ] Add 3 new fields to the RG

  


Nothing is needed on the building record.

  


Niccolas Miller 04/25/2023: [[PC0153314]] - ZFP - FGI: Cost Estimates (T&M)
