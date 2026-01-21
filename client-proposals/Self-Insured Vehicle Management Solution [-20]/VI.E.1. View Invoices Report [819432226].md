6.5.1. View Invoices Report

*Done. 

  


Overview: This is the standard multi-pane Silverloom "All Invoices" report, based on Invoice records, with customizations.

  


Accessed from: Home | Invoices | View Invoices. 

  


Title: Invoices

  


Left Pane: This is the standard "Invoices Cockpit" report, used to filter the right pane:

Preface: N/A

  


Columns:

  * Views



  


The "Views" column includes the following rows/options:

  * Open Invoices (filters the right pane to show only Invoices with "Status" = "Draft" or "Invoiced")
  * Closed Invoices (filters the right pane to show only Invoices with "Status" = "Closed" or "Canceled")
  * All Invoices (no filtering for the right pane)
  * Recent Invoices (filters the right pane to show invoices that have been edited within the last 60 days (i.e. the entire last month plus current partial month to date))



  


  


Right Pane: This is the standard "Invoices" report, filtered based on the "View" selection in the left pane:

Preface: N/A

  


Columns: 

  * Invoice Number
  * Invoice Date
  * Total Amount
  * Contact
  * Organization
  * Location (displays the City and State of the Invoice Contact, in the following format: "<City>, <State abbreviation>") 
  * Payment Date
  * Status
  * Current Agent (custom column) 



  


Grouped by:

  * If "Show recent invoices only (modified in last 60 days)" checkbox is not checked: "Status"
  * If "Show recent invoices only (modified in last 60 days)" checkbox is checked: Last edited date:
    * "Today:
    * "Yesterday"
    * Day of the week (for items within the past week)
    * "Last Week"
    * "Two Weeks Ago"
    * "Three Weeks Ago"
    * "Last Month"
    * "Older"



  


Sorted by: Invoice Date + Invoice ID (newest at the top)

  


Filters: 

  * Invoice # (plain text; defaults to blank = all)
  * Contact (drop list of Contacts; defaults to blank = all)
  * Organization (drop list of Organizations; defaults to blank = all)
  * City (plain text; defaults to blank = all)
  * State (drop list of "State" list items (State abbreviations); defaults to blank = all)
  * Zip (plain text; defaults to blank = all)
  * Invoice date from (date; looks at the "Invoice Date"; defaults to blank = all)
  * Through (date; looks at the "Invoice Date"; defaults to blank = all)
  * Status (multi-select list of "Invoice Status" list items; defaults to blank = all)
  * Sales (Item(s) (multi-select list of Sales Item records; defaults to blank = all)
  * Show recent invoices only (modified in last 60 days) (checkbox; defaults to not checked)



  


Buttons: 

  * Search (opens the a prompt screen with all of the filters for the "Invoices" report (right pane))
  * New Invoice (opens a new Draft invoice record, with "Invoice Date" set to the current date)



  


Data Access: All users

  


Other Notes:

  * N/A


