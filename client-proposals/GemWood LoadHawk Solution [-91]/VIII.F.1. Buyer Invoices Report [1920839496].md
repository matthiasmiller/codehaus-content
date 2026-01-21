8.6.1. Buyer Invoices Report

  


Requirements

Overview: This is a custom report of Buyer Invoice details, based on Delivery Ticket records.

  


Accessed from: Main Menu | Buyers | Buyer Invoices

  


Title:

  * If "Buyer" filter is blank: "Buyer Invoices for All Buyers"
  * If "Buyer" filter is not blank: "Buyer Invoices for <Buyer Name>"
  * If "A/R Aging" filter is checked: includes "Aging" prefix (i.e. "Aging Invoices for All Buyers", etc.)



  


Columns: 

  * Ticket Date 
  * Invoice #
  * Delivery Ticket (link to open the corresponding Delivery Ticket record; displays as "View Ticket")
  * Delivery Ticket Status
  * Buyer 
  * Invoice $ (displays the "Buyer Invoice $"; total row shows sum) 
  * Balance $ (displays the "Buyer Balance $"; total row shows sum) 
  * Due Date (displays the "Buyer Due Date"; displays in red font if on or before the current date) 
  * # Days Past Due (if overdue, displays the number of days since the Due Date, in red font) 
  * Closed Date (displays the Closed Date or Canceled Date, as applicable) 
  * View/Print Invoice (link; displays as "PDF") 



  


Grouped by: 

  * Default: Delivery Ticket Status (standard sequence)
  * If "A/R Aging" filter checkbox is checked: special grouping:
    * Overdue (if "Due Date" is in the past)
    * Within 10 Day Window (if "Due Date" = the current date or is within 10 days of the current date)
    * Beyond 10 Day Window (if "Due Date" is more than 10 days in the future)



  


Sorted by: Due Date (earliest at the top) 

  


Filters: 

  * Buyer (optional; drop list of Buyer-type Contacts; filters down as you type; defaults to blank = all) 
  * Invoice # (optional; drop list of Invoice #'s from Delivery Ticket #'s with Status = "Awaiting Buyer Payment" or "Awaiting Grade Report / Settlement"; if a selection is made in the "Buyer" filter, list includes only items for the selected Buyer; if "Buyer" filter is blank, list includes all items; filters down as you type; defaults to blank = all) 
  * Due Date Start (optional; date; defaults to blank = all; looks at the Due Date) 
  * End (optional; date; defaults to blank = all; looks at the Due Date)
  * A/R Aging (checkbox; defaults to not checked; if checked, the report displays only items from Delivery Tickets with "Status" ≠ "Closed" or "Canceled")



  


Buttons: 

  * New Buyer Payment (opens a new Buyer Payment record; if a Buyer is selected in the report's "Buyer" filter, the new record has the "Buyer" field defaulted accordingly, otherwise defaults to blank)



  


Menu Visibility: 

  * All Users 



  


Other Notes: 

  * Rows for Tickets with "Delivery Ticket Status" = "Closed" or "Canceled" are displayed in gray font.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=664853694#gid=664853694](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=664853694#gid=664853694)

Austin Priest 12/05/2024: Updated
