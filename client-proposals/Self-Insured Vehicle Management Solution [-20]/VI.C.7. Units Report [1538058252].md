6.3.7. Units Report

  


Requirements

*Done. 

  


Overview: This is a custom, totals-only report that looks at Vehicle records and displays the number of "units" (number of active coverages and new Entry Fees) per Agent + Fund combination, for a selected Coverage Period Year. 

  


Specifically, this report should include the following items as "units": 

  * For "Premium" units: Coverages that were active in the selected Period Year and have their "End Date" in Coverage History set to the last day of the selected Period Year
    * Notes: 
      * This means that if coverage was activated more than once on the same Vehicle in the same Period Year is only counted once, for the coverage that was active on the last date of the Period year. 
      * If a coverage was active during the Period Year, but was deactivated prior to the last date of the Period Year, it is not included on this report.; 
  * For <Collision> "Entry Fee" units: Coverages that were activated at any point in the selected Period year. 
    * Notes: 
      * This means that if <Collision> coverage was activated more than once on the same Vehicle in the same Period Year, each of those activations is counted and included on this report. 



  


Accessed from: Admin | Admin Reports | Units Report

  


Title: Units Report 

  


Preface (two lines): 

"*Premium units are the total count as of <last date of the selected time period>." 

"*Entry Fee units are the total activated from <first date> to <last date>." 

  


Columns: There is one row for each agent with at least one applicable unit for the selected Period Year (specifically, one row for each agent who is listed on a Fees & Credits row for a fee that counts as a "unit" based on the criteria at the top of this report spec). Note that this is similar to the Income Report (though that report looks at dollar amounts from Invoices for its data).

  * Agent (no heading label; no total) 
  * Active Liability Units (displays the number of active Liability coverages on vehicles as of the last date of the selected Period Year; total row shows sum)
  * Active <Alternate text for Collision - Short label> Units (displays the number of active <Collision> coverages on vehicles as of the last date of the selected Period Year; total row shows sum)
  * <Alternate text for Collision - Short label> Entry Fee Units (visible if Solution uses <Collision> Entry Fee; displays the number of <Collision> coverages activated within the selected Period Year; total row shows sum) 
  * Active Cargo Units (displays the number of active Cargo coverages on vehicles as of the last date of the selected Period Year; total row shows sum) 



  


Grouped by: 

  * First by: Fund (based on the Vehicle Fee Fund; alphabetically)
  * Second by: Agent (based on the Vehicle Fee Agent; displayed as the individual rows; alphabetically) 



  


Sorted by: N/A

  


Filters: 

  * Coverage Period Year (required; drop list of Period Years; with the following additional details: 
    * Period Years are listed in the following format: 
      * Upcoming Period Year (visible if the current date is in May or June): "YYYY-YYYY"; 
      * Current Period Year: "YYYY-YYYY (Current)"; 
      * Past Period Years: "YYYY-YYYY"; 
      * example, supposing the current date is in May or June of 2025: 
        * 2025-2026  
        * 2024-2025 (Current) 
        * 2023-2024
        * 2022-2023
        * etc.
    * defaults to the top item; 
    * this looks at the "Coverage Start Date" on Vehicles) 



  


Buttons: 

  * N/A



  


Menu Visibility: Admin only (by virtue of being on the Admin menu) 

  


Other Notes: 

  * If a user wishes to print paper copies of this report, the user should select the PDF option from the Advanced drop-down menu for the report.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/26/2025: Added in [[[IN11180](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11182&)]] - ZWA - Add Units Report
  * Tim Reitz 08/26/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident


