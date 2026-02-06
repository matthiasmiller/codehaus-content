3.4.3. Units Report

  


Requirements

*Documented. Tim Reitz 08/26/2025:

  


Make the following change(s) (full spec included here, with changes noted with blue and strike-through): 

  


Overview: This is a custom, totals-only report that looks at Vehicle records and displays the number of "units" (number of active coverages and new Entry Fees) per Agent + Fund combination, for a selected Coverage Period Year. 

  


Accessed from: Admin | Admin Reports | Units Report

  


Title: Units Report 

  


Preface (two lines): 

"*Premium units are the total count as of <last date of the selected time period>." 

"*Entry Fee units are the total activated from <first date> to <last date>." 

  


Columns: There is one row for each agent listed on a Fees & Credits row for a corresponding fee within the time period. This is similar to the Income Report (though that report looks at dollar amounts from Invoices instead).

  * Agent (no heading label; no total) 
  * Active Liability Units (displays the number of active Liability coverages on vehicles as of the last date of the selected time period; total row shows sum)
  * Active <Alternate text for Collision - Short label> Units (displays the number of active Collision/VLS coverages on vehicles as of the last date of the selected time period; total row shows sum)
  * <Alternate text for Collision - Short label> Entry Fee Units (visible if Solution uses Collision Entry Fee; displays the number of Collision/VLS coverages activated within the selected time period; total row shows sum) 
  * Active Cargo Units (displays the number of active Cargo coverages on vehicles as of the last date of the selected time period; total row shows sum) 



  


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

Tim Reitz 02/27/2025: See the CR where this report is being added: [[[IN11180](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11182&)]] - ZWA - Add Units Report.
