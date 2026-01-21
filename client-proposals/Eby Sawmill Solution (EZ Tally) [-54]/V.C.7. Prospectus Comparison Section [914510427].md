5.3.7. Prospectus Comparison Section

  


Requirements

Prospectus Comparison section (visible if Purchase Type = Flat Payments):  

  * Forester (optional; drop list of Forester-type Contacts; filters down as you type)
  * Scale (visible and required if a Forester is selected; drop-list of International / Doyle; default to International; see Other Notes for explanation about International vs. Doyle scales) 
  * Prospectus Comparison (visible if a Forester is selected; embedded spreadsheet with the following:) 
    * Columns: 
      * Species (auto-filled and read-only; the first time a Forester specified, the spreadsheet automatically includes a row for each active Species in the Solution) 
      * # of Trees (optional; number to 0 decimal places; default to blank)
      * Avg DBH (optional; DBH stands for Diameter at Breast Height; number to 1 decimal place; not used for any calculations; default to blank)
      * Avg BF (auto-calculated and read-only; this = "Total BF" / "# of Trees" for the row; displays "0" if N/A)
      * Total BF (required if a Forester is selected; number to 0 decimal places; user enters "0" if there are no logs for a row) 
      * Price/MBF (required if a Forester is selected; number to 0 decimal places; this will be defaulted to "0" if Total BF is entered as "0"; validate that it is non-zero if Total BF is non-zero - validation error message on Save: "Price/MBF is cannot be 0 if Total BF is not 0.") 
      * Value (auto-calculated and read-only; this = "Total BF" / 1000 x "Price/MBF" for the row; displays "0" if N/A)
      * (blank spacer column)
      * Harvested Doyle BF (auto-set and read-only; displays the rounded total Net Board Feet for logs of that Species for the Tract; displays "0" if N/A) 
      * Harvested Avg. $/MBF (auto-set and read-only; this is the average price paid for logs of that Species for the Tract; calculated as follows: (Harvested Value for the row) / (Harvested Doyle BF for the row) * 1,000 with the results rounded to the nearest 2 decimal places; displays "0" if N/A)
      * Harvested Value (auto-set and read-only; actual total value of logs of that Species for the Tract, rounded to 2 decimal places; displays "0" if N/A)
      * (blank spacer column)
      * Compare BF (auto-calculated and read-only; this = "Harvested Doyle BF" \- "Total BF"; may be negative, indicating more harvested than estimated; displays "0" if N/A)
      * Compare Avg. $/MBF (auto-calculated and read-only; this = "Harvested Avg. $/MBF - "Price/MBF" for the individual rows and for the totals; may be negative, indicating more harvested than estimated; displays "0" if N/A) 
      * Compare Value (auto-calculated and read-only; this = "Harvested Value" \- "Value"; may be negative, indicating more harvested than estimated; displays "0" if N/A)
    * Automatically sorted by: Species, with the "Misc." Species at the bottom (sort alphabetically by species, except for "Misc." which is at the bottom)
    * Show 15 rows without scrolling



  


  * Totals (auto-calculated and read-only; displayed on the screen directly below the corresponding columns, with no additional labels; all display "0" if N/A):
    * # of Trees (sum of column values)
    * Avg DBH (average of column values; exclude 0s and blanks)
    * Avg BF (average of column values; exclude 0s)
    * Total BF (sum of column values)
    * Price/MBF (average of column values; exclude 0s)
    * Value (sum of column values)
    * Harvested Doyle BF (sum of column values; note that this is the total Net Board Feet for the Tract) 
    * Harvested Avg. $/MBF (average Price per MBF; calculated as follows: (Harvested Value total, calculated from the individual row values) / (Harvested Doyle BF total) * 1,000 with the result rounded to the nearest 2 decimal places) 
    * Harvested Value (sum of column values; note that this is the total of Log Values for the Tract)
    * Compare BF (difference of Total BF total and Harvested Doyle BF total; may be negative, indicating more harvested than estimated)
    * Compare Avg. $/MBF (difference of Price/MBF total and Harvested Avg Price total; may be negative, indicating higher harvested than estimated)
    * Compare Value (difference of Value total and Harvested Value total; may be negative, indicating higher harvested than estimated)



  


Other Notes:

  * International vs. Doyle scales: The majority of prospectuses use the International Scale, which is another method of scaling logs, but a few use the Doyle Scale. The Solution should track which scale a given prospectus is using, but does not need to do any calculations with the International Scale (it is tracked for informational purposes only).



  


Development Specification

CCI:

[ ] Basic RG: 4 HOURS

[ ] Harvested Doyle BF -- use TractTotalHarvestedNetBF

[ ] Harvested Avg Price / MBF -- use TractTotalHarvestedValue / TractTotalHarvestedNetBF / 1000

[ ] Harvested Value -- use TractTotalHarvestedValue

[ ] Place the totals carefully to line up with columns, Nic will provide macros for these.

  


NIC:  

[ ] TractTotalHarvestedNetBF( vOptionalSpecies) -- returns the total Doyle Harvest BF -- summing the Net BF from yard tallies.

[ ] TractTotalHarvestedValue( vOptionalSpecies) -- returns the total value for all harvested amounts for this species.

[ ] Add TractTotal and TractAvg macros for each column (unless it's simply TractTotalHarvestedValue(""), e.g. TractAvgDBH, Be careful to not average averages.

4 HOURS
