5.8.1. Export Tally Details Section

  


Requirements

  * Export Tally Details section: 
    * Export Tally Status (auto-set and read-only; Open, Confirmed, Loaded, Closed; see explanation in Other Notes below)
    * Export Tally ID (auto-numbered and sequential, starting at 700001; read-only; unique identifier)
    * Print Export Tally Summary (link; opens the Export Tally Summary Printout in a new tab; see printout details in the corresponding section of the proposal)
    * Email Export Tally Summary (link; opens a new tab to send the Export Tally Summary email, with the appropriate fields defaulted; see details in the corresponding section of the proposal; note that this email can be sent by users with the "Edit Open/Confirmed Export Tallies" permission, even when the Status = Closed) 
    * Booking ID (required; drop list of all open Booking IDs; editable only for Admin, meaning that only Admins can create Export Tallies; warning on Save if changed - validation message: "The Booking ID has been changed."; when in edit mode, an ellipsis button is displayed to the right of the field to open the Booking record; when in read-only mode, the Booking ID is a link to open the record)
    * Early Return Date (auto-set and read-only; from selected Booking)
    * Cutoff Date (auto-set and read-only; from the selected Booking)
    * Description (auto-set and read-only; from the selected Booking)
    * Total Loads (auto-set and read-only; "Total Loads" from the selected Booking)
    * Target Board Feet (embedded spreadsheet with the following:) 
      * Columns: 
        * Base Grade (required; drop list of Base Grades; validate against duplicates on the same tally - error on Save if duplicates exist: "Target Board Feet: The same Base Grade cannot be used more than once.") 
        * Target Board Feet (required; number with no decimals; wide enough to show 5 digits; used as a guide for the Scaler to know how many logs of that Base Grade to put on the Tally) 
        * Remaining Gross Board Feet (auto-calculated and read-only; looks at the Gross Board Feet of all logs on the Tally with the corresponding Base Grade, and displays the difference of the corresponding Target and actual; negative if actual exceeds target; displayed as "Grade <Base Grade> BF: <number>" on the yard app)
      * Automatically sorted by: N/A (unsorted) 
      * Buttons to add and remove rows ("+"/"-") 
      * Allow a maximum of 3 rows (show all 3 rows without scrolling) 
    * Total Target Board Feet (auto-calculated and read-only; sum of all Target Board Feet numbers) 
    * Total Remaining Board Feet (auto-calculated and read-only; difference of Total Target Board Feet and Total Gross Board Feet; negative if actual exceeds target) 
    * Total Net Board Feet (auto-calculated and read-only; number with no decimals; sum of Net Board Feet for all logs on the Tally)
    * Total Gross Board Feet (auto-calculated and read-only; number with no decimals; sum of Gross Board Feet for all logs on the Tally; with the following behaviors: 
      * warning on Save if more than X board feet over the Target Board Feet - message: "The Total Gross Board Feet exceeds the target total by more than <X> board feet. Reduce the total board feet to continue."; 
      * show the total in red if more than X BF over the Target Board Feet; 
      * show the total in orange if more than X board feet under than the Target Board Feet; 
      * show the total in green if within X board feet over or under the Target Board Feet; 
      * note that the value represented here as "X" can be set by an admin user via the "Export tally target warning threshold" System Switch; this normally would be 100 board feet)



  


Development Specification

Change Requests: 

  * Tim Reitz 03/28/2024: [[[IN9658](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9660&)]] - ZET - Export Tally Record - Make Target Fields Editable for Non-Admins
  * Tim Reitz 08/31/2024: [[[IN10233](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10235&)]] - ZET - Add Export Tally Summary Printout
  * 


  


Ellis Miller 12/20/2022: Talk to me about how we do the "starting at 700001"

  


Ellis Miller 12/20/2022: 

[ ] Booking ID Helper List: OpenBookings.ndx or BookingsByOpenClosed.ndx

[ ] Simple RG with macros

[ ] Simple total macros

[ ] Put the 100 into an ExportTallyTargetWarningThreshold system switch. Description:

The threshold difference above or below the export tally target to show warning colors.

BID: 4 HOUR
