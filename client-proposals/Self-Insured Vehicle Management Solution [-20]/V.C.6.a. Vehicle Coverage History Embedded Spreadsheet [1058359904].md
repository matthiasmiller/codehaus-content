5.3.6.1. Vehicle Coverage History Embedded Spreadsheet

Tim Reitz 07/25/2025: Changes probably being made to this RG in [[[IN11786](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11788&)]] - ZWA - Vehicle - Coverages - Research & fix issue causing coverages to retain active status when Deactivation Date is set. 

Wait to make edits to this spec until after that is documented (or update the spec there if needed). 

  


  * Vehicle Coverage History (auto-populated and read-only embedded spreadsheet with the following: 
    * Columns:
      * Date (date; sets to the current date when the coverage was activated/reactivated)
      * Owner (list field that displays Contact names (list items); sets to the name of the vehicle Owner for the coverage)
      * Coverage Type (list field that displays "Coverage Types" list items; sets to the Coverage Type for the coverage)
      * No-Charge (checkbox; sets according to the "No-Charge Vehicle" field)
      * Start Date (date; sets to the coverage start date)
      * End Date (date; sets to the coverage end date, updates if coverage is ended early)
      * Status (list field that displays "Coverage History Status" list items; with the following details / behaviors:
        * automatically sets when one of the following happens: 
          * when the "Activate" button is clicked for coverages; 
          * when the "Deactivate" button is clicked on coverages; 
          * when the "Confirm" button is clicked while a vehicle is transferred; 
          * when the Vehicle renew automatic process runs; 



: Tim Reitz 07/08/2025: Update these button / import specs for the onchange.

when clicked, the following other fields are affected: 

  * "Status" on the Vehicle Coverage History (see corresponding spec)



Tim Reitz 08/15/2025: Actually, this isn't needed, due to changes in [[[IN11786](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11788&)]]. 

  * sets as described below: 
    * Sets to "Active":
      * If the coverage "Activation Date" is in the current Period Year or in the upcoming Period Year.
    * Sets to "Used":
      * If the coverage "Activation Date" is before the "Period Start Date" for the current Period Year (for rows added retroactively for the prior period)
      * If the coverage "Deactivation Date" is after the "Period Start Date" for the current Period Year (for rows deactivated in the current period)
    * Sets to "Canceled":
      * If the coverage "Deactivation Date" is before the "Period Start Date" for the current Period Year (for rows added for the upcoming period and subsequently canceled/deactivated))


  * Automatically sorted by: Date (latest at the top) 
  * Shows 25 rows without scrolling
  * Other Notes: 
    * Note that there is no linking between this "Coverage History" embedded spreadsheet and the "Fees and Credits" embedded spreadsheet, though rows are added to both simultaneously.


