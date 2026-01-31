3.3.4.1. Invoice - Itemization Section

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Itemization section:

Embedded spreadsheet with the following:

  * Columns:
    * Date (optional date field; defaults to blank) 
    * Vehicle Name (drop-list of vehicles for the selected Contacts)
    * Sales Item (drop-list of active sales items)
    * Description (plain text)
    * Amount (number; two decimals)
  * Append and Delete buttons ("+", "-")
  * Automatically sorted by: Date 



  


  * Total Amount (auto-calculated and read-only; displays the sum of Amount for all rows in the spreadsheet;)
  * Total Paid (auto-calculated and read-only; displays the sum of all Amount for all rows in the Payments spreadsheet)
  * Payments (button; opens an embedded spreadsheet of:
    * Columns:
      * Date (defaults to the current date)
      * Check #
      * Amount (number; two decimals)
      * Deposit Date
      * Deposited By (drop-list of contacts)
      * Notes (plain text)
  * Due Amount (auto-calculated and read-only; displays the difference of Total Amount and Total Paid)



  


Other Notes: 

  * The "Collision Entry Fee" list item in the drop list for Sales Items is included if Solution uses Collision Entry Fee. 
  * The "Cargo Entry Fee" list item in the drop list for Sales Items is included if Solution uses Cargo Entry Fee.



  


Development Specification

Ellis Miller 09/05/2024: 

  


2 Hours

[ ] Add ActiveSalesItems macro to use as HelperList to filter down SalesItems based on system switches as noted above.
