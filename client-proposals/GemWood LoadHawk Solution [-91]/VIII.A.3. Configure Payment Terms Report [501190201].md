8.1.3. Configure Payment Terms Report

  


Requirements

Overview: This is a custom report of all Payment Terms records in the database. 

  


Special Features: This report contains some special features for confirming calculations that depend on Payment Terms, such as Due Date, discount amounts, etc. These features are enabled via a "Show Sample Calculations" checkbox filter. Data pulled directly from the Payment Terms records is displayed in the standard black font, sample data entered in the "Calculations" filters is displayed in green font, and the resulting calculated data is displayed in purple font. Note that the spec for these special features is preliminary, and is to be finalized as part of the coding process, as the developers determine what columns and features are helpful and necessary for this report. 

  


Accessed from: Advanced | Configuration | Configure Payment Terms (opens the report directly, bypassing the filter screen)

  


Title: Payment Terms

  


Columns: 

  * Name (link to open the record)
  * Description 



  


  * Narrow blank spacer column, visible if "Show Sample Calculations" checkbox is checked
  * Sample Ticket Date (visible if "Show Sample Calculations" checkbox is checked; displays the value from the corresponding filter; green font) 
  * Sample Buyer Invoice $ (visible if "Show Sample Calculations" checkbox is checked; displays the value from the corresponding filter; green font)
  * Sample Total Buyer Payment $ (visible if "Show Sample Calculations" checkbox is checked; displays the value from the corresponding filter; green font) 
  * Sample Buyer Settlement Date (visible if "Show Sample Calculations" checkbox is checked; displays the value from the corresponding filter; green font)
  * Sample Lumber Brokerage Fee % (visible if "Show Sample Calculations" checkbox is checked; displays the value from the corresponding filter; green font) 
  * Calculated Lumber Brokerage Fee $ (visible if "Show Sample Calculations" checkbox is checked; displays the calculated amount for the row; purple font) 



  


  * Narrow blank spacer column
  * Uses Optional Early Payment (displays "Yes" / "No") 
  * Early Pay Window (Calendar Days) (displays the value of "Early Pay Window [  ] Calendar Days") 
  * Calculated Early Pay Due Date (visible if "Show Sample Calculations" checkbox is checked; displays the calculated amount for the row; purple font)
  * Early Pay Discount % 
  * Calculated Early Pay Discount $ (visible if "Show Sample Calculations" checkbox is checked; displays the calculated amount for the row; purple font) 



  


  * Narrow blank spacer column
  * Payment Due In 
  * Day Type 
  * Date Baseline 
  * Calculated Due Date (visible if "Show Sample Calculations" checkbox is checked; displays the calculated amount for the row; purple font)



  


  * Narrow blank spacer column, visible if "Show Sample Calculations" checkbox is checked
  * Sample Commission % (visible if "Show Sample Calculations" checkbox is checked; displays the value from the corresponding filter; green font) 
  * Calculated Commission $ (visible if "Show Sample Calculations" checkbox is checked; displays the calculated amount for the row; purple font) 
  * Sample Internal Fee Payout % (visible if "Show Sample Calculations" checkbox is checked; displays the value from the corresponding filter; green font) 
  * Calculated Internal Fee Payout $ (visible if "Show Sample Calculations" checkbox is checked; displays the calculated amount for the row; purple font) 



  


Grouped by:

  * First: "Active" / "Inactive" 
  * Second: "Member Payment Terms" / "Buyer Payment Terms" 



  


Sorted by: Name (alphabetical)

  


Filters: 

  * Show Sample Calculations (checkbox; defaults to not checked; if checked, additional filters and columns are displayed) 
  * Sample Buyer Invoice $ (visible and required if "Show Sample Calculations" checkbox is checked; number; 2 decimals; defaults to "1,000.00")
  * Sample Total Buyer Payment $ (visible and required if "Show Sample Calculations" checkbox is checked; number; 2 decimals; defaults to "900.00") 
  * Sample Lumber Brokerage Fee % (visible and required if "Show Sample Calculations" checkbox is checked; number; 2 decimals; defaults to "4.00")
  * Sample Ticket Date (visible and required if "Show Sample Calculations" checkbox is checked; date; defaults to 10 days before the current date) 
  * Sample Buyer Settlement Date (visible and required if "Show Sample Calculations" checkbox is checked; date; defaults to 3 days before the current date)
  * Sample Sales Commission % (visible and required if "Show Sample Calculations" checkbox is checked; number; 2 decimals; defaults to "1.00") 
  * Sample Internal Fee Payout % (of GW Fee) (visible and required if "Show Sample Calculations" checkbox is checked; number; 2 decimals; defaults to "1.00") 



  


Buttons: 

  * New Payment Terms (opens blank new record)



  


Menu Visibility: All users

  


Other Notes:

  * N/A



  


Development Specification

Mockup Without Calculations: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1914299866#gid=1914299866](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1914299866#gid=1914299866)

Tim Reitz 01/23/2025: Updated.

Mockup With Calculations: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1252148888#gid=1252148888](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1252148888#gid=1252148888)

Tim Reitz 03/07/2025: Updated.

  


Ellis Miller 12/16/2024: CODE BY USA.

[ ] Consider 3 row column headings with aggressive abbrv and tooltips as needed to make this as narrow as possible.

[ ] You may want to code this as part of the Delivery Ticket calculations. Most of the calcs are done there and I'm adding this here to prove them out.

BID: 1 Day

  


Tim Reitz 12/06/2024: CC USA will code the calculations, and add conditionally-visible columns to this report as needed for debugging / testing purposes.
