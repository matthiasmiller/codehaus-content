7.5.1.1. Buyer Payment - Buyer Payment Overview Section

  * Buyer Payment Overview section: 
    * Status (located in the header bar for this section; no label; read-only macro; displays the current status (items correspond to the "Draft / Complete / Canceled" simple list): 
      * "Draft": if neither the "Complete" nor "Canceled" checkbox is checked; 
      * "Complete": if the "Complete": checkbox is checked; 
      * "Canceled": if the "Payment Canceled" checkbox is checked) 
    * Internal Payment ID (hidden; auto-set and read-only; unique identifier for the record; sequential number shared across all Payment Types) 
    * Payment Category (hidden field; required; drop list of "Payment Category" list items; defaults as set by the record or report from which the Payment record is created; becomes read-only after the initial Save; this is used to determine which detail screen to display - Buyer or Member) 



  


  * Payment Description (read-only macro; displays the following: "<Buyer Name> Pmt. on <Payment Date> <(#)>", with "#" being a sequential number if multiple Buyer Payment records exist for the same Buyer + Payment Date; this is used as the visual identifier for the record throughout the Solution)
  * Buyer (required; drop list of active Buyer-type Contacts; filters down as you type; defaults to blank; includes an ellipsis button to open the selected record, or create a new one if the drop list is blank; becomes read-only if there is one or more rows in the "Linked Delivery Tickets" embedded spreadsheet)
  * Payment Date (required; date; with the following details / behaviors: 
    * defaults to the current date; 
    * warning on Save if one or more "Due Date" or "Est. Buyer Early Pay Due Date" dates for linked Delivery Tickets are before this date: "One or more Due Dates or Est. Early Pay Due Dates for linked Delivery Tickets are overdue.") 
  * Payment Total $ (read-only macro; dynamically displays the sum of all "Applied $" amounts from the "Linked Delivery Tickets" embedded spreadsheet)
  * Complete (editable if the "Canceled" checkbox is not checked; checkbox + date, which toggle; defaults to not checked, but automatically checks on the first Save after the record has been created; when the checkbox is checked, the date defaults to the current date) 
  * Canceled (editable if the "Complete" checkbox is not checked; checkbox + date, which toggle; defaults to not checked; with the following special behaviors: 
    * when the checkbox is checked, the following things happens: 
      * the date defaults to the current date; 
      * all rows from the "Linked Delivery Tickets" embedded spreadsheet are deleted, to remove the sub-payments from the Tickets; 
      * a warning message displays on the field: "All sub-payments have been deleted and unlinked from Delivery Tickets. To undo, refresh the page before saving.")


