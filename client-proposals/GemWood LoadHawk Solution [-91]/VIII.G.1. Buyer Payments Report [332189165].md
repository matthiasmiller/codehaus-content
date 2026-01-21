8.7.1. Buyer Payments Report

  


Requirements

Overview: This is a custom report of Buyer Payments (Payment records with "Payment Category" = "Buyer"), with various filters.

  


Accessed from:   

  * Main Menu | Payments | Buyer Payments
  * Other links



  


Title: 

  * If "Buyer" filter is blank": "Buyer Payments"
  * If "Buyer" filter is set: "Buyer Payments for <Buyer Name>"



  


Columns: 

  * Status 
  * Payment Description (link to open the record)
  * Payment Date 
  * Payment Total $ (visible if "Report Rows" = "One per Payment"; total row displays sum) 
  * Sub-payment PO # (visible if "Report Rows" = "One per Sub-payment")  
  * Sub-payment Ticket # (visible if "Report Rows" = "One per Sub-payment")  
  * Sub-payment Pre-Discount $ (visible if "Report Rows" = "One per Sub-payment") 
  * Sub-payment Applied $ (visible if "Report Rows" = "One per Sub-payment"; total row displays sum) 
  * Sub-payment Due Date (visible if "Report Rows" = "One per Sub-payment")



  


Grouped by: 

  * First by: Selection in the "Group By" filter: 
    * If "Group By" filter = blank: N/A (no grouping) 
    * If "Group By" filter = "Status": Status (standard sequence) 
    * If "Group By" filter = "Buyer + Status":
      * First by: Buyer (alphabetical)
      * Second by: Status (standard sequence)
    * If "Group By" filter = "Status + Buyer":
      * First by: Status (standard sequence)
      * Second by: Buyer (alphabetical)
  * Second by (only if "Report Rows" = "One per Sub-payment"): Payment (alphabetical) 



  


Sorted by: 

  * First by: Payment Date (latest at the top)
  * Second by: Payment Description (alphabetically)



  


Filters: 

  * Report Rows (required; drop list of "One per Sub-payment" / "One per Payment"; defaults to "One per Sub-payment") 
  * Buyer (drop list of Buyer-type Contacts; filters down as you type; defaults to blank = all)
  * Payment Date Start (date; looks at the Payment Date; defaults to blank = all)
  * End (date; looks at the Payment Date; defaults to blank = all)
  * Status (optional; multi-select drop list of "Draft / Complete / Canceled" list items; defaults to all selected)
  * Group By (optional; drop list of blank = none / "Status" / "Buyer + Status" / "Status + Buyer"; defaults to blank = none)
  * Sub-payment PO # (visible if "Report Rows" = "One per Sub-payment"; drop list of Buyer's PO #'s for the selected Buyer, or all PO #'s if "Buyer" = blank; list displays in the following format: "<Buyer's PO #> (<PO Date>, <Buyer>)"; filters down as you type; defaults to blank = all) 
  * Sub-payment Ticket # (visible if "Report Rows" = "One per Sub-payment"; drop list of Delivery Tickets for the selected Buyer, or all Delivery Tickets if "Buyer" = blank; filters down as you type; defaults to blank = all) 
  * Sub-payment Pre-Discount $ (visible if "Report Rows" = "One per Sub-payment"; number; defaults to blank = N/A) 
  * Sub-payment Applied $ (visible if "Report Rows" = "One per Sub-payment"; number; defaults to blank = N/A) 
  * Sub-payment Due Date (visible if "Report Rows" = "One per Sub-payment"; date; defaults to blank = all) 



  


Buttons: 

  * N/A 



  


Menu Visibility: All users

  


Other Notes:

  * N/A



  


Development Specification

Mockup (one row per sub-payment): [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1022570186#gid=1022570186](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1022570186#gid=1022570186) 

Tim Reitz 02/21/2025: Updated. 

Mockup (one row per Payment): [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1981818251#gid=1981818251](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1981818251#gid=1981818251)

Tim Reitz 02/21/2025: Updated.
