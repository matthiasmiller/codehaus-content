3.2.5.1. Actual Building Costing

  


Requirements

Once a building cost has been updated (see FGI Actual Costs), a button can be used to automatically distribute that expense across buildings.

  


This will run an automatic process that will save a cost override on all buildings during that period. It will prompt for:

  * District (required; list of Districts)
  * Year (required; number)
  * FGI Cost Category (required; list of FGI Cost Categories)
  * Period (list of period end dates; required)
  * Transaction Date (required; default to Today)



  


It will:

  * Calculate the total costs for that period, subtracting all costs that are marked as "Freeze Standard Cost as Actual Cost".
  * Distribute the remaining cost to all remaining buildings (including sold buildings), weighted by the building's Standard Cost $ for the specified cost. This will update the Actual Cost Date and will populate the Actual Cost Location if it's blank.
  * Reconcile all building records, with the requested entry date (i.e. transaction date).
  * It's likely that the distributing the actual cost will result in rounding differences. Any rounding differences will be applied to the building with the most expensive standard cost.



  


NOTE:

  * Create a "Building Cost Calculator" report to help with this that prompts for:
    * District
    * FGI Category
    * Start/End Date (filters Build Date)
    * Period Cost
  * It should show columns for:
    * STIN
    * Build Date
    * Manufacturer Cost
    * FGI Category Cost
  * It should show total rows for total manufacturer costs and total FGI category cost.



  


Development Specification

DONE_CCI: This will run an r20 that does the weighted average. Use pre-import validation to make sure that the period start date and end date are valid for the selected FGI Cost Item.

  


  


Niccolas Miller 04/25/2023: [[PC0153540]] - ZFP - FGI: Actual Building Costing (T&M)

  


Niccolas Miller 04/26/2023: This should be an x30 list that runs this and the x30 from the Building Accounting Reconciliation section.
