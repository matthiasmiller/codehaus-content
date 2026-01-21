5.3.4. Logger Details Section

  


Requirements

Logger Details section:

  * Logger (embedded spreadsheet; at least one row is required) 
    * Columns: 
      * Logger (drop list of Logger-type contacts; warn on each save if blank - warning message: "The logger should not be blank."; validate against multiple rows for the same logger - error message on the field: "This logger has already been added to this Tract.")
      * Logger Timber Rate ($/mbf; required; number with no decimals; warning on Save if changed when there is at least one Yard Tally for this Logger + Tract: "There already is at least one Yard Tally for this Logger linked to this Tract. Changing the Logger Timber Rate will result in data discrepancies.")
      * Logger Pulpwood Rate ($/ton; required; number to two decimals; warning on Save if changed when there is at least one row for this Logger in the Pulpwood Loads embedded spreadsheet: "There already is at least one load of pulpwood recorded for this Logger on this Tract. Changing the Logger Pulpwood Rate will result in data discrepancies.")
    * Automatically sorted by: Logger
    * Buttons to add and remove rows ("+"/"-")
      * The "-" button to remove rows is hidden for Loggers that have at least one Yard Tally linked to them for this Tract. 
    * Show 3 rows without scrolling
  * New Logger (link; opens a new Contact record with Contact Type defaulted to Logger; once saved, this new contact will appear on the Logger drop list)



  


Development Specification

BID: 

[ ] Basic screen: 2 HOURS

[ ] CanDelete Permission (may require ndx): 1 HOUR
