6.3.3. Coverage Deactivation Dates Report

  


Requirements

*Done. 

  


Overview: This is a custom report of Vehicles that have one or more active coverages with "Deactivation Date" set (i.e. coverages that are set to be deactivated, which can happen in the case of a short-term coverage or in the case of a user forgetting to click the "Deactivate" button after setting the date). This report displays one row for each coverage.

  


Note that the following data access notes apply:

  * Admin users can see all Vehicles, including any that they manage
  * Non-Admin users can only see rows for Vehicles that they manage



  


Accessed from:

  * Home | Vehicles | Coverage Deactivation Dates (bypasses the prompt page to open the report directly) 
  * Via the "Coverage Deactivation Due / Overdue" report alert notification (see corresponding spec)



  


Title: 

  * If the "Show only due / overdue coverages" filter checkbox is not checked: "Coverage Deactivation Dates"
  * If the "Show only due / overdue coverages" filter checkbox is checked: "Coverage Deactivation Dates / Overdue Dates"



  


Preface: N/A

  


Columns: 

  * Owner (displays the current "Owner" for the Vehicle; link to the Owner's Contact record)
  * Vehicle (displays as "Link"; link to Vehicle record)
  * Year (displays the Vehicle Year)
  * Make (displays the Vehicle Make)
  * Model (displays the Vehicle Model)
  * Coverage (displays the Coverage Type)
  * Deact. Date (displays the Deactivation Date for the Coverage)
  * Agent (displays the current "Owner's Agent" for the Vehicle)



  


Grouped by:

  * "Due / Overdue" (includes rows with "Deactivation Date" = the current date or in the past);
  * "Coming Due" (includes rows with "Deactivation Date" in the future) 



  


Sorted by: Deactivation Date (earliest at the top)

  


Row-Specific Buttons: N/A 

  


Filters: 

  * Show only due / overdue coverages (checkbox; defaults to not checked; when checked, the report only includes Vehicles with "Deactivation Date" set to the current date or in the past)



  


Buttons: N/A

  


Menu Visibility: All users 

  


Other Notes: 

  * N/A



  


Development Specification

Austin Priest 08/08/2025: _TR I don't understand how this grouping works. I am only seeing rows in the grouping Due / Overdue. I don't think the grouping is working properly. When I check the Show only due / overdue coverages filter it hides one of the rows that is showing up in the Due / Overdue grouping.

TODO_CR: Tim Reitz 08/11/2025: Confirmed that this looks like a bug. Let's write up a CR. 

Here's a link to the report in the test system for easy access: [https://testweaverland.silverloom.io/Reports/Standard/Std_Coverage_Deactivation_Dates?Asks=vAskAgent%3D%22Reitz%2C+Tim%22&State=ctLVLwm53iQ&](https://testweaverland.silverloom.io/Reports/Standard/Std_Coverage_Deactivation_Dates?Asks=vAskAgent%3D%22Reitz%2C+Tim%22&State=ctLVLwm53iQ&). 

Note that the bottom row has a Deact. Date of 01/01/2026 (in the future), but it is included in the "Due / Overdue" grouping (and no "Coming Due" grouping is visible. 

  


TODO_CR: Tim Reitz 08/27/2025: Maybe also change the "Vehicle" column link display to be the VIN, instead of just "Link".
