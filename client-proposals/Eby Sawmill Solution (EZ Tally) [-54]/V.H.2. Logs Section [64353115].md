5.8.2. Logs Section

  


Requirements

  * Logs section
    * Logs (embedded spreadsheet with the following:) 
      * Columns: 
        * Tag # (required; editable if Status = Open; numeric string field; wide enough for six digits; in the AppHosting Solution, this is filled manually; in the yard app, this is filled manually for the first log in a Tally; then the fields sequentially advance from the Tag # that was filled/entered for the previous log, unless the user edits an existing Tag #, and if a log is deleted from the middle of the list, the existing logs do not change; validate against duplicate Tag #'s on the same Export Tally - validation error message on Save: "Duplicate Tag #'s are not allowed.")
        * Species (required; editable if Status = Open; drop-list of active Species abbreviations)
        * Length (required; editable if Status = Open; number to 0 decimals; feet; this is the full length of the log)
        * Cutback (optional; editable if Status = Open; number to 0 decimals; feet; this is the usable length of the log)
        * Diameter (required; editable if Status = Open; number to 0 decimals; inches)
        * Base Grade (required; editable if Status = Open; drop list of Base Grades - single-digit numbers 0 through 5)
        * Gross Board Feet (auto-calculated using the Doyle method, looking at the full Length; number with no decimals - round up or down to the nearest whole number)
        * Net Board Feet (auto-calculated using the Doyle method; if there is a Cutback, this looks at the Cutback, if there is no Cutback, this looks at the Length and is the same as Gross BF; number with no decimals - round up or down to the nearest whole number)
        * ID (required; editable if Status = Open; numeric; normally set in the Yard App; in the AppHosting Solution, this is auto-incremented; editable via imports/reports; validate against duplicates) 
      * ID (required; numeric; hidden; with the following special behaviors:
        * set as a random number up to 10 digits, both from the Yard App and the main system to be used as an internal unique identifier for each log;   
        * validate against duplicates within the same Yard Tally)
      * Tally Sequence # (auto-set and read-only; sequential number that corresponds to the log's row on the Logs table; this is used as the log's visual identifier in both the Yard App and the main system; note that if a log is deleted from the tally, other logs' Sequence #'s may change accordingly)
      * Automatically sorted by: N/A (unsorted)
      * Buttons to add and remove rows ("+"/"-") 
        * Buttons are only visible if Status = Open, so that logs cannot be deleted from a Confirmed or Closed Tally 
      * Show 25 rows without scrolling 
    * Confirmed (checkbox + date and time + user name; cannot be checked if there are no logs entered in the Logs table - error message on the field: "This Export Tally cannot be confirmed because there are no logs on it."; error on the field if Total Gross Board Feet is exceeds the Target Board Feet by more than the "Export tally target warning threshold": "The Total Gross Board Feet exceeds the target total by more than <X> board feet. Reduce the total board feet to continue."; filling the checkbox auto-fills the date/time and username, which are read-only; the Tally can be "unconfirmed" by clearing the checkbox; clearing the checkbox also clears the date/time and username)



  


Development Specification

Tim Reitz 02/05/2024: CR: [[[IN9325](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9327&)]] - ZET - Yard Tally & Export Tally - Log IDs

  


Ellis Miller 12/20/2022: DONE_MM: Please document why we have both an ID and a Tag #. I think it is:

The ID is used by the Yard App to easily import data onto a specific row.

Matthias Miller 01/05/2023: The reason we need it is if someone wants to change the tag number on an existing row.

  


Ellis Miller 12/20/2022: 

[ ] Basic RG

[ ] Validate that ID is non-blank and not duplicated.

[ ] Auto-incrementing

[ ] Plugging in formulats

BID: 4 HOUR
