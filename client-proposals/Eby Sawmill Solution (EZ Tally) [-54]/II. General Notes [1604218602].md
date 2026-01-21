2\. General Notes

  


Requirements

In this software solution (as in the logging industry), all prices are reported in dollars per 1,000 board feet ($/mbf). All lengths are reported in board feet (bf). The distinction between bf and mbf is critical. This does not affect values or amounts, since those are in dollars.

  


The Solution will be used in two main locations: the office (on Windows computers) and in the yard (on Android or iPhone mobile devices). 

  


Eby's has a redundant internet solution (wireless and cable).

  


The Solution will not use the calendar date picker. All dates are manually typed into the date fields. 

  


Rounding for Log Values, Pulpwood payments, etc.: 

  * General: Always round to the nearest cent (up or down as needed).
  * For totals (on Yard Tallies, Payments, Summary Reports, etc.): Round first for each item, and total the rounded numbers.



  


Terminology: 

  * Cutback: This is the usable portion of a log. For example, if the full length of a log is 24 feet and 4 feet of the log at one end is rotten, only 20 feet of it is usable. Therefore the cutback = 20 feet.



  


Development Specification

TODO_MM_LATER: 

The following pieces were not on our radar in the HLD. They took time to spec out, and will increase the price tag for the client:

  * Changes to Tract record: 
    * The Prospectus Comparison section came up as something new. Probably spent 4+ hours on this. Matthias said to wait until we get to pricing to see whether we should try to recoup anything for the extra time
    * Down Payments and Expense Withholding features (RGs on Tract record, linking out to Payment records) came later in the game and provided some extra complexity. Maybe spent 3 hours on this. 
    * Pulpwood Prices RG (multiple locations & prices), and related report. Maybe spent 1 hour on this. 
  * Changes to the Export Tally record: 
    * Target Board Feet for Base Grade (RG). Maybe spent .5 hr on this. 
  * Tract Profitability Overview Report (maybe spent .5 hr on this) 
  * Other notes: 
    * Various reports grew from single pane to multi-pane reports.


