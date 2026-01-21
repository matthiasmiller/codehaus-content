5.3.5. Financial Details Section

  


Requirements

Financial Details section:

  * Tract Profitability (link; opens the Tract Profitability by Tract Report, filtered to this Tract) 
  * Landowner % Payments (visible if Purchase Type = Adjustable Tiered Percentages; link; opens the Landowner % Payments Summary report, filtered to this Tract) 
  * Landowner Flat Payments (visible if Purchase Type = Flat Payments; link; opens the Landowner Flat Payments Summary report, filtered to this Tract) 
  * Logger Payments (link; opens the Logger Payment Summary report, filtered to this Tract)
  * Timber Freight $ (read-only macro; displays the value of "Eby's Timber Freight Rate" * "Total Net BF"/1000) 
  * Pulpwood Freight $ (read-only macro; displays the sum of "Total Pulpwood Freight" amounts from the Pulpwood Prices table) 
  * Total Freight $ (read-only macro; displays the sum "Timber Freight $" and "Pulpwood Freight $") 
  * Total Net BF (auto-set and read-only; displays the Total Net BF from all Yard Tallies for the Tract; rounded to the nearest whole number)
  * Total Gross BF (auto-set and read-only; displays the Total Gross BF from all Yard Tallies for the Tract; rounded to the nearest whole number)
  * Total Log Value $ (auto-set and ready-only; displays the Total Value from all Yard Tallies for the Tract; rounded to the nearest 2 decimal places) 
    * Note: Remove the colon from the three existing labels.



  


Development Specification

BID: 1 HOUR

  


  


Change Requests: 

  * Tim Reitz 06/06/2024: [[[IN9495](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9497&)]] - ZET - Tract Record & Yard Tallies Report - Add More Totals
  * Tim Reitz 07/15/2024: [[[IN10071](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10073&)]] - ZET - Tract Profitability by Tract Report - No timber value for Percentage-based Tracts
  * Ben Reitz 05/01/2025: [[[IN10943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10945&)]] - ZET - Fix Timber Freight Calculations (prev. Tract Profitability Report - Incorrect formula)


