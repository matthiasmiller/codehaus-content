20.5.1. Pulpwood Loads Section

  


Requirements

Tim Reitz 11/15/2023: This is being replaced by Pulpwood Load records and a bottom report on the Tract (see [[[IN8780](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8782&)]] - ZET - Add Pulpwood Loads Record & Report (and related / subsequent jobs). 

  


Pulpwood Loads section:

  * Pulpwood Loads (embedded spreadsheet with the following:)
    * Columns: 
      * Load ID (auto-set and read-only)
      * Logger (required; drop list of Logger-type contacts for this Tract; if there is only one Logger for the Tract, auto-fill to that Logger)
      * Date Processed (required; default to blank)
      * Location (required; drop list of Pulpwood Locations included on the Pulpwood Prices table for this Tract; if there is only one Location for the Tract, auto-fill to that Location; if there are no Locations for the Tract, the user should add to the Pulpwood Prices table)
      * Tons (required; number to 2 decimals)
      * Amount (dollar amount; number to 2 decimals; auto-calculated and read-only; Tons * Pulpwood Location Price)
      * Notes (plain text)
      * Logger Payment ID (auto-set and read-only; when the row is added this sets to the earliest unpaid Payment record for the corresponding Contact + Tract; if no unpaid Payment exists, the Solution will automatically create one and apply the Payment ID here)
      * View (link; displays as "Link"; opens the corresponding Logger Payment record) 
      * Logger Paid (checkbox; auto-set based on the corresponding Logger Payment)
      * Landowner Payment ID (auto-set and read-only, like the Logger Payment ID; note that if Purchase Type = Flat Payments, this remains blank since the Landowner does not receive payment for pulpwood) 
      * View (link; displays as "Link"; opens the corresponding Landowner Payment record; note that if Purchase Type = Flat Payments, this remains blank) 
      * Landowner Paid (checkbox; auto-set based on the corresponding Landowner Payment; note that if Purchase Type = Flat Payments, this remains blank)
    * Automatically sorted by: Date Processed + Logger 
    * Buttons to add and remove rows ("+"/"-")
      * Note that the "-" button is hidden for rows with at least one Payment (Landowner or Logger) that is Paid. 
    * Show 8 rows without scrolling (on a large job there can be over 100 loads of pulpwood)
    * Other Notes: 
      * Note that the user can enter a negative Tons amount to enter a negative $ amount on the Payment (if too many tons have been entered and paid).



  


Development Specification

\- To set the Pulpwood Load ID: Use a NewRGRowID

  


CCI BID: 

[ ] Basic RG. 4 HOUR

  


NIC:

[ ] Fill in Logger and Landowner Payment IDs
