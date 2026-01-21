5.7. Booking Record

  


Requirements

Overview: The Booking record is used to keep track of Export Tallies and related details for a customer.

  


Accessed via: Bookings Report

  


Sections and Fields: 

  * Booking section: 
    * Status (auto-set and read-only; Open, Ready for Invoicing, Closed - see explanation in Other Notes below)
    * Booking ID (required; plain text, wide enough for 18 characters; unique identifier; duplicates not allowed - error on Save validation message: "Duplicate Booking IDs are not allowed.")
    * Customer (required; drop list of Customer-type Contacts)
    * Description (single-line plain text; long enough for 50 characters)
    * Total Loads (auto-calculated and read-only; total number of Export Tally records linked to this Booking)
    * Unconfirmed Loads (auto-calculated and read-only; "Total Loads" minus the number of Confirmed Export Tally records linked to this Booking)
    * Early Return Date (required; default to blank; this is the earliest date that the port will accept the container)
    * Cutoff Date (required; default to blank; this is the latest date that the port will accept the container)
    * New Load (link; opens a new Export Tally record with the Booking defaulted; for new Booking records the link is visible after the first save; the link is hidden if the Booking Status = Closed)
    * View Export Tallies (link to the Export Tallies by Booking Report for this Booking; if Booking Status = Open or Ready for Invoicing, this is visible to users with the "View Export Tallies" permission; if the Booking Status = Closed, this is visible only to users with the Edit All Export Tallies permission)
    * Print All Export Tally Summaries (link; opens the Export Tally Summary Printout for all Tallies linked to the Booking record, in a new tab; see printout details in the corresponding section of the proposal)
    * Species + Base Grade Totals (embedded spreadsheet with the following; all rows would be automatically filled and read-only, based on the logs entered on all Export Tallies for the Booking)
      * Columns: 
        * Species 
        * Base Grade
        * Net Board Feet
      * There is one row for every Species + Base Grade combination
      * Automatically sorted by: Species + Base Grade 
      * Show 4 rows without scrolling
    * Total Gross Board Feet (auto-calculated and read-only; number with no decimals; sum of all Gross Board Feet for the linked Export Tallies)  
    * Total Net Board Feet (auto-calculated and read-only; number with no decimals; sum of all Net Board Feet for the linked Export Tallies) 
    * Pricing Notes (memo; visible only for users with the View and Edit Financials permission)
    * Invoice # (plain text field; wide enough for 12 characters; visible for all users; editable only for users with the View and Edit Financials permission)
    * Invoiced (checkbox; auto-set and read-only; filled when an Invoice # is entered; always visible) 
    * Email Booking Summary (link; opens a new tab to send the Booking Summary email for this Booking, with the appropriate fields defaulted; see details in the corresponding section of the proposal)



  


Data Access:

  * View for: Users with the View Export Tallies and Bookings permission
  * Edit for: 
    * If the Status = Open or Ready for Invoicing: Users with the Edit Open Bookings permission
    * If the Status = Closed: Users with the Edit All Bookings permission
  * Delete for: Users with the Edit All Bookings permission
  * Invoice #: Edit for: Users with the View and Edit Financials permission
  * Pricing Notes: View and edit for: Users with the View and Edit Financials permission



  


Validations: 

  * If an Administrator edits a Closed record, show a warning on Save.
    * Validation message: "You are about to save changes to a Closed Booking, which may result in data discrepancies."



  


Other Notes: 

  * Note that this record should have a name, date, and time stamp for Created and Last Modified.
  * Booking Statuses:
    * "Closed": if Invoiced checkbox is filled
    * "Ready for Invoicing": if there is at least one Export Tally linked to the Booking and all Export Tallies linked to the Booking have a Status of Loaded
    * "Open": in any other case



  


Development Specification

Change Requests: 

  * Tim Reitz 08/31/2024: [[[IN10233](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10235&)]] - ZET - Add Export Tally Summary Printout
  * 


  


  


Mockup:

  * Google Sheets: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=993458601](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=993458601)



  


  * Designer: [https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D58&SinglePane=true&State=Tr1GcI4u7tA](https://zch.apphosting.zone/Reports/Standard/Designer/Std_Preview_Database_Level?Asks=AskParentID%3D58&SinglePane=true&State=Tr1GcI4u7tA)



  


  


Ellis Miller 12/20/2022:

[ ] Basic Record (2 HOUR)

[ ] Hide New Load and View Export Tallies link until it's saved for the first time.

[ ] Make Invoiced checkbox a separate stored field since we are restricting the Invoice # record. Use OnChange statements to keep it in-sync. Don't modify the fields with Field Change Exprs on save.

[ ] Virtual RG for Species (4 HOUR):

[ ] Macro BookingSpeciesGradesNbfList: ListSubstitute(BookingExportTalliesList, ExportTallySpeciesGradesNbfTable)

[ ] Macro BookingSpeciesAndGradesList: built from above item

[ ] This list is your virtual RG repeat list. The first two columns are from the RepeatListItem.

[ ] The board feet start with your BookingSpeciesGradesNbfList and do a list substitute based on your RepeatListItem to create a pipe list to sum.

  


[ ] Status macro that looks at Loads records (1 HOUR):

[ ] Need LoadsByBookingAndLoaded.ndx

  


[ ] Permissioning (1 HOUR)

  


BID: 1 Day
