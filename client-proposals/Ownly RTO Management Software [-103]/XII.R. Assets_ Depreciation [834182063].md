12.18. Assets: Depreciation

Seth Miller 01/13/2026: We still need to implement MARCS schedule for Book depreciation as well as tax depreciation

  


Niccolas Miller 01/09/2026: 

  * MACRS is generally not used for book depreciation, only for tax depreciation.
  * See [https://www.irs.gov/publications/p946](https://www.irs.gov/publications/p946) for tax depreciation overview.
    * Section: Which Property Class Applies Under GDS?
      * Rent-to-own dealer.
      * Rent-to-own contract.
    * Section: Which Recovery Period Applies?
      * 3/5/7 year GDS?
      * 4 year ADS?
    * Section: Which Depreciation Method Applies?
      * [Depreciation Methods](https://www.irs.gov/publications/p946#en_US_2024_publink100068700 "https://www.irs.gov/publications/p946#en_US_2024_publink100068700")
      * [MACRS Percentage Table Guide](https://www.irs.gov/publications/p946#en_US_2024_publink1000270861 "https://www.irs.gov/publications/p946#en_US_2024_publink1000270861")
    * Section: Straight Line Method (When using the straight line method,...)
      * You determine the straight line depreciation rate for any tax year by dividing the number 1 by the years remaining in the recovery period at the beginning of that year. When figuring the number of years remaining, you must take into account the convention used in the year you placed the property in service. If the number of years remaining is less than 1, the depreciation rate for that tax year is 1.0 (100%).



  


Seth Miller 11/14/2025: TODO_NM: [[PC0187344]]

  


  * Depreciation Calculations:
    * Book and tax models
    * Straight-line/accelerated
    * Repeating Group (RG) on product record - specifically for tracking depreciation dates and amounts
    * Editable historical depreciation events with permission-controlled visibility



  


  * Proposal:
    * Depreciation is always editable before the depreciation start date
    * Require Accounting admin privileges for depreciation



  


  


  * Depreciation Section
    * Start Date (date; editable; for Book Depreciation) 
    * Start Date (date; editable; for Tax Depreciation)
    * Book Schedule (drop-list of all depreciation schedules for the linked RTO Company in the following format: "<Depreciation Method> \- <Useful Life> <Length (Years)> Years"; note that Length (Years) value and "Years" text is only included if Useful Life is "Fixed Length"; otherwise it should show Contract Length)
      * Book Schedule Method (hidden list field; list of Depreciation Methods; set when Book Schedule is set)
      * Book Schedule Type (hidden list field; list of Useful Life; set when Book Schedule is set)
      * Book Schedule Term Year (hidden number field; set when Book Schedule is set if Useful Life is Fixed Length)
      * Warn when changing it on or after the start date, indicating that it has accounting implications (for book value) and tax implications (for tax value).
    * Useful Life (Months) - freeze this based on the active contract length (if one is active) or based on the fixed length Seth Miller 11/18/2025: per discussion w/ Matthias we will have a field for term length. It's hard to pull from the contract w/ current contract entry. We can make this fancier in the future
    * End Date - MonthInc(StartDate, UsefulLifeMonths) - 1
    * Salvage Value - frozen from method



  


NOTE: Whenever you change the depreciation settings, we will likely warn on save, then save the full depreciation schedule (dates and amounts) in an RG. It should be under an RG button for "Full Depreciation Schedule" not on the main screen. Add a calculated column that shows Book Value / Tax Value.

  * Add a report of depreciation, grouped by calendar/tax year and with totals
  * All depreciation will be dated at the end of every month. If the depreciation start date is on the 20th, it will apply on the 31st. If it's the 31st, it applies on the 31st. NOTE: MACRS years will run from that first month for 12 months (first year), the next 12 months (second year), etc. It follows the year based on the asset being put into service, not based on a calendar year.



  


NOTE: We are deferring tax depreciation

  


  


Matthias Miller 08/13/2025: 

  * What accounting events do we need, for example
    * how are lost buildings typically expensed
    * are early payoffs just adjustments to the remaining asset balance?
      * if someone manages to do an early payoff for less than the value of the building, how should that be handled from an accounting perspective? Presumably cancel out the value of the building, but where does the underpayment get accounted for? A "loss on sale of asset" expense?


