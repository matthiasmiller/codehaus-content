17.0.1. Tract Record **version 2**

The Tract record will include the following: 

  


  * Tract Name
  * Contract Details section:
    * Purchase Type; non-editable list of:
      * Adjustable Tiered Percentages 
      * Flat Payments
    * Adjustable Tiered Percentages; visible for respective purchase type; embedded spreadsheet of:
      * Min Price $ (number; two decimals)
      * Payment % (number; no decimals)
    * Logger (embedded spreadsheet of loggers)
    * Logger Timber Rate ($/bf; two decimals)
    * Logger Pulpwood Rate ($/ton; two decimals)
    * Owner Pulpwood Rate ($/ton; two decimals)
    * Signature Date
    * Expiration Date
    * Pulpwood Price ($/ton; number; two decimals)
    * Eby's Freight Rate ($/mbf)
  * Payments section; embedded spreadsheet of:
    * Payment Type
      * Owner
      * Logger (if Flat Payments)
      * Misc Expense
    * Flat Payment Schedule (visible for Owner Flat Payments; drop list of :)
      * Date
      * Start of Harvest
      * Mid-Harvest
      * End of Harvest
    * Scheduled Date (visible for Owner Flat Payments)
    * Harvest % (0-100; visible for Owner Flat Payments; editable for mid-harvest; 0 for start of harvest; 100 for end of harvest)
    * Yard Tallies (linked RG of Yard Tally IDs; visible for Owner Adjustable Tiered Percentages, and Loggers)
    * Pulpwood (linked RG of Pulpwood IDs; visible for Owner Adjustable Tiered Percentages, and Loggers)
    * Payment Due (editable for Owner Flat Payments; otherwise, auto-calculated from yard Tallies and Pulpwood)
    * To (??) - DONE_DM: same as above -- Contact Record DONE_CH -- must be tied out to a logger
      * Add validation to the yard tally and to the tract that this stays in sync
    * Check # (
    * Amount ($)
    * Paid (checkbox)
    * Payment Date (auto-fills when Paid checkbox is filled; editable; required)
  * Pulpwood section:
    * ID (auto-generated)
    * Date Processed
    * Tons (number; 1 decimal)
    * Logger Paid (checkbox) DONE_CH
  * Harvest section:
    * Harvest Started (checkbox + editable date)
    * Harvest Paused (checkbox + editable date)
    * Harvest Ended (checkbox + editable date)
  * Notes (embedded memo that allows general notes and file attachments)



  


Misc Notes:

  * Pulpwood goes straight to a papermill and is tracked in tons.
  * Owner Payments are reconciled monthly.
  * Logger Payments are reconciled weekly.
  * The Adjustable Tiered Percentages will be limited to 3 tiers for reporting purposes. However, the software can easily be expanded to additional tiers in the future if needed.
  * The Mid-Harvest payment will be determined by the forester, and we do not need reminders.


