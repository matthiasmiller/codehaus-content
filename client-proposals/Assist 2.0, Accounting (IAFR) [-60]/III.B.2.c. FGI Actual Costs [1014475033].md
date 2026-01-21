3.2.2.3. FGI Actual Costs

  


Requirements

Actual costs will be stored on an "FGI Actual Cost" record, with the following fields:

  * District (list of districts)
  * Year (number)
  * FGI Category (list of FGI Categories)
  * Actual Costs; embedded spreadsheet of:
    * Period Start Date (date; read-only; 1/1 of the specified year for the first period; the date following the prior period end date for subsequent periods)
    * Period End Date (date; required)
    * Period Cost $ (number; 2 decimals)
    * Period Manufacturer $ (number; automatic; Manufacturer Cost for all buildings built in the period)
    * Period Cost % (automatic; 2 decimals; this is the Cost $ / Manufacturer Total)
  * Update Building Records button; see "Actual Building Costing"; default to most recently-completed period



  


NOTE:

  * Only one combination (District+Year+Cost Type) can exist. These records will be identified using these three settings (e.g. "NC-2023-01" where 01 is the numeric ID of the FGI Category).
  * Validate that there are no duplicate Period End Dates



  


Development Specification

Ellis Miller 04/18/2023:

  


[ ] New Lookup record

[ ] Simple RG.

[ ] Skip the button for now.

  


Niccolas Miller 04/25/2023: [[PC0153317]] - ZFP - FGI: Create FGI Actual Costs Lookup Record (T&M)
