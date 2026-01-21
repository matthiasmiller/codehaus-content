6.7.2. Export Tallies Report

  


Requirements

Overview: This is a report of Export Tallies and their corresponding logs, based on a variety of filters. 

  


Accessed in various forms from:

  * Main | Logs Exports | Export Tallies (bypasses the filter screen to open the report directly)
  * The "View Export Tallies" link on the Booking record
  * It also is used as the right pane of the Bookings report (but the right pane of this report is hidden when displayed there)



  


Title: Export Tallies for <filter information>

  * If Customer and Booking ID filter both = blank: "Export Tallies for All Bookings"
  * If Customer filter is set: "Export Tallies for <Customer>"
  * If Booking ID filter is set, or if both Customer and Booking ID filters are set: "Export Tallies for Booking <ID>"



  


The left pane shows a summary of Export Tally records based on the selected filters, with each row representing a Export Tally. Note that the spec for this left pane also applies to the right pane of the Bookings report. 

Title: Export Tally Summary

  


Columns:

  * Export Tally ID (link to record)
  * Status
  * Gross Board Feet
  * Container #
  * Heavy Weight
  * Light Weight
  * Seal #
  * Loaded Date
  * Tally PDF (link; displays as "PDF"; generates a PDF of the Export Tally Summary Printout for the corresponding Tally; opens in a new tab; see the corresponding section of the proposal)
  * Customer
  * Booking ID



  


Grouped by: 

  * If Group by filter = Status: Status (Open, Confirmed, Loaded, Closed) 
  * If Group by filter = Booking: Booking ID (alphabetical) 
  * If Group by filter = blank: No grouping



  


Sorted by: Export Tally ID (newest / highest number at the top)

  


The right pane shows a breakdown of all Export Tallies from the left pane, with each row representing one log, and a totals row at the bottom; not included on the Bookings report:

Title: Export Tally Breakdown

  


Columns: 

  * Tag # (no total row)
  * Species (total row shows quantities of logs)
  * Length (for logs with no Cutback, this simply displays the Length; for logs with Cutbacks, this is displayed as "12/8" for a 12-foot full Length and an 8-foot Cutback length; total row shows average, using the full Length)
  * Diameter (whole number; total row shows average)
  * Base Grade (no total row)
  * Gross Board Feet (whole number; total row shows average)
  * Net Board Feet (whole number; total row shows average)
  * Tally Sequence (displays the row sequence number from the original entry sequence on the embedded spreadsheet on the Export Tally; no total row)



  


Grouped by: First by Group by filter (same grouping as the left pane), then by Export Tally ID with the newest / highest number at the top 

  


Sorted by: Tally Sequence

  


Filters: 

  * Group by (drop list of "Status", "Booking", and blank; defaults to Status; selecting the blank option causes the report to be run with no grouping)
  * Customer (drop list of all Customer-type contacts; filters down as you type; defaults to blank = all; applies to the left pane)
  * Booking ID (if the Customer filter is blank, this is a drop list of all Booking IDs; if Customer filter is set, this is a drop list of all Booking IDs for the selected Customer; filters down as you type; defaults to blank = all; applies to the left pane)
  * Tally ID (if Booking ID is blank, drop list of all Export Tally IDs; if Booking ID is set, drop list of Export Tally IDs for the selected Booking; filters down as you type; defaults to blank = all; applies to the left pane)
  * Container # (if Booking ID is blank, drop list of all Container Numbers for all Export Tallies; if a Booking ID is selected, drop list of Container Numbers for Export Tallies on the selected Booking ID; filters down as you type; defaults to blank = all; applies to the left pane) 
  * Seal # (drop list of Seal #'s; filters down as you type; defaults to blank = all; applies to the left pane)
  * Tally Loaded Start Date (defaults to blank = all; applies to the left pane)
  * Tally Loaded End Date (defaults to blank = all; applies to the left pane)



  


Buttons: 

  * N/A



  


Menu Visibility: Users with the View Export Tallies and Booking permission

  


Other Notes:

  * If changes are made to the left pane, corresponding changes should likely be made to the right pane of the Booking report.



  


Development Specification

Change Requests: 

  * Tim Reitz 06/20/2024: [[[IN9198](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9200&)]] - ZET - Booking & Export Tally Reports - Reconsider filters
  * Tim Reitz 08/31/2024: [[[IN10233](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10235&)]] - ZET - Add Export Tally Summary Printout
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1158742920](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=1158742920)

  


Ellis Miller 12/21/2022:

[ ] Note that this report "Std Export Tallies (multi-pane).r20" is cloned as "Std Export Tallies (sub-pane).r20" for the Booking report. See comments in the booking report.

  


  


[ ] Left pane prompts:

[ ] BookingsByCustomer.ndx

[ ] TalliesByBooking.ndx

[ ] TalliesByBookingIDAndContainerID.ndx (added for Booking report)

  


Right Pane:

[ ] Note that this is not row-dependent, it is simply a different view to all of the data in the left pane.

  


BID: 1 Day
