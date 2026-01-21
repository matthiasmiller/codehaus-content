6.7.1. Bookings Report

  


Requirements

Overview: The Bookings report would be a multi-pane report showing Bookings and their corresponding Export Tallies.

  


Accessed from: Main | Logs Exports | Bookings (bypasses the filter screen to open the report directly). 

  


The left pane is a report of Booking records, based on the selected filters, with each line representing one Booking.

  


Title: Bookings

  


Columns: 

  * Booking ID (link to record)
  * Customer
  * Description
  * Total Loads
  * Unconfirmed Loads
  * Early Return Date
  * Cutoff Date
  * PDF (link; generates a PDF of the Booking Summary Printout for the corresponding Booking; opens in a new tab; see the corresponding section of the proposal) 
  * Excel (link; generates an Excel file of the Booking Summary Printout for the corresponding Booking; opens a new tab and prompts to download/save the file; see the corresponding section of the proposal)



  


Grouped by: Status (Open at the top; Ready for Invoicing in the middle; Closed at the bottom in gray)

  


Sorted by: Early Return Date (earliest date at the top) then by Booking ID (alphabetical)

  


  


The right pane is visually the same as the left pane of the Export Tallies Report (see the corresponding section of this proposal for the full spec), filtered to show results for the selected Booking (or the last-selected Booking if multiple are selected) in the left pane of the Bookings report. 

  


Grouped by: N/A

  


Sorted by: Tally ID

  


Filters: 

  * Status (multi-select drop list of Open, Ready for Invoicing, Closed; defaults to Open and Ready for Invoicing; for the left pane) 
  * Booking ID (drop list of all Booking IDs; filters down as you type; defaults to blank = all; for the left pane) 
  * Customer (drop-list of all Customer contacts; filters down as you type; defaults to blank = all; for the left pane)
  * Early Return Start Date (defaults to blank = all; for the left pane)
  * Early Return End Date (defaults to blank = all; for the left pane)
  * Cutoff Start Date (defaults to blank = all; for the left pane)
  * Cutoff End Date (defaults to blank = all; for the left pane)
  * Tally Loaded Start Date (defaults to blank = all; for the left pane - returns all Bookings that have at least one Export Tally with a Loaded date in the range)
  * Tally Loaded End Date (defaults to blank = all; for the left pane - returns all Bookings that have at least one Export Tally with a Loaded date in the range)
  * Container # (if Booking ID is blank, drop list of all Container Numbers for all Export Tallies; if a Booking ID is selected, drop list of Container Numbers for Export Tallies on the selected Booking ID; filters down as you type; defaults to blank = all; for the right pane) 



  


Buttons: 

  * New Booking (opens a new Booking record)



  


Menu Visibility: Users with the View Export Tallies and Bookings permission

  


Other Notes:

  * If changes are made to the right pane, corresponding changes should likely be made to the Export Tallies report.



  


Development Specification

Change Requests: 

  * Tim Reitz 06/20/2024: [[[IN9198](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9200&)]] - ZET - Booking & Export Tally Reports - Reconsider filters
  * Tim Reitz 08/31/2024: [[[IN10233](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10235&)]] - ZET - Add Export Tally Summary Printout
  * Tim Reitz 08/31/2024: [[[IN10485](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10487&)]] - ZET - Booking Summary PDF and Excel file - Stop Downloading as Zip File
  * 


  


  


Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=509997103](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=509997103)

  


Ellis Miller 12/21/2022:

[ ] Let's name the two reports "Std Export Tallies (sub-pane).r20" and "Std Export Tallies (multi-pane).r20". Use macros as much as possible to minimize cloning.

[ ] Clone all of the ask prompts as well to simplify the logic. Consider having a ExportTalliesRptSubset(....) catalog subset that takes a bunch of ask answers as parameters so that the subsetting logic is shared.

[ ] To filter Container #, we will need a TalliesByBookingIDAndContainerID.ndx.

  


BID: 1 Day
