5.4.2. Logs Section

  


Requirements

Logs section:

  


  * Logs (embedded spreadsheet with the following:) 
    * Columns: 
      * Species (required; drop-list of active Species abbreviations; editable if Status = Open)
      * Length (required; number to 0 decimals; this is the full length of the log in feet; editable if Status = Open)
      * Cutback (optional; number to 0 decimals; this is the usable length of the log in feet; editable if Status = Open)
      * Diameter (required; number to 0 decimals; inches; editable if Status = Open)
      * Grade (required; drop list of active Grades; editable if Status = Open)
      * Price (auto-set based on the selected Species and Grade; read-only; number to 2 decimal places; $/mbf) 
      * Gross Board Feet (auto-calculated using the Doyle method, looking at the full Length; read-only; number with no decimals - round up or down to the nearest whole number)
      * Net Board Feet (auto-calculated using the Doyle method; read-only; if there is a Cutback, this looks at the Cutback; if there is no Cutback, this looks at the Length and so is the same as Gross BF; number with no decimals - round up or down to the nearest whole number)
      * Log Value ($; auto-calculated and read-only; number to 2 decimals; Net Board Feet / 1000 * Price)
      * Condition (optional; drop list of active Log Conditions; editable if Status = Open)
      * Other Log Condition (editable if Condition = "Other" and if Status = Open; plain text)
      * ID (required; numeric; hidden; with the following special behaviors:
        * set as a random number up to 10 digits, both from the Yard App and the main system to be used as an internal unique identifier for each log;   
        * validate against duplicates within the same Yard Tally)
      * Tally Sequence # (auto-set and read-only; sequential number that corresponds to the log's row on the Logs table; this is used as the log's visual identifier in both the Yard App and the main system; note that if a log is deleted from the tally, other logs' Sequence #'s may change accordingly)
    * Automatically sorted by: N/A (unsorted)
    * Buttons to add and remove rows ("+"/"-") 
      * Buttons are only visible if Status = Open, so that logs cannot be deleted from a Confirmed or Closed Tally 
    * Show 25 rows without scrolling
  * Qty. (below the Tally Sequence # column; no label; auto-set and read-only; displays the total number of logs/rows in the table) 
  * Average Length (below the Length column; no label; auto-set and read-only; displays the average of all rounded Length values, rounded to the nearest whole number) 
  * Average Diameter (below the Diameter column; no label; auto-set and read-only; displays the average of all rounded Diameter values, rounded to the nearest whole number) 
  * Average Price (below the Price column; no label; auto-set and read-only; displays the average of all rounded Price values, rounded to the nearest whole number) 
  * Total Gross BF (below the Gross Board Feet column; no label; auto-set and read-only; displays the sum of all rounded Gross Board Feet values, rounded to the nearest whole number) 
  * Total Net BF (below the Net Board Feet column; no label; auto-set and read-only; displays the sum of all rounded Net Board Feet values, rounded to the nearest whole number) 
  * Total Log Value (below the Log Value column; no label; auto-set and read-only; displays the sum of all rounded Log Value values, rounded to the nearest 2 decimal places)



  


Development Specification

Change Requests: 

  * Tim Reitz 02/05/2024: [[[IN9325](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9327&)]] - ZET - Yard Tally & Export Tally - Log IDs
  * Tim Reitz 06/20/2024: [[[IN9494](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9496&)]] - ZET - Yard Tally Record - Add Totals below the Logs Table
  * 


  


  


  


[ ] The visible SpeciesCode is an editable macro that uses an ActiveSpeciesCodes helper list. OnChange, it sets an underlying Species list field.

[ ] If we don't have it, create a ActiveSpeciesCodes list that just left(2) of each of the active list items. If we have an ActiveSpecies.ndx, we can do this without hitting the lookup records.

[ ] The hidden Species list field should not be editable. We'll just use the SpeciesCode for editing.

[ ] Auto-set price by adding OnChange to both Species and Grade.

[ ] Auto-incremented ID (use a stored Max field so that we don't reuse if the last item is deleted).

  


BID: 4 HOURS
