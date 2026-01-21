7.4.5. Delivery Ticket - Member Payments Section

  


Requirements

  * Member Payments section:
    * Member Payments (read-only embedded spreadsheet with the following; used to track Member Payment records linked to the Delivery Ticket, with one row for each Member Payment):  
      * Columns: 
        * Payment ID (macro; displays the "Member Payment ID" from the Payment) 
        * Status (macro; displays the "Payment Status" from the Payment)
        * Payment Type (macro)
        * Payment Date (macro)
        * Subtotal $ (macro; displays the "Ticket Subtotal $" from the Payment)
        * Applied Overpayment $ (macro; displays the "Applied Overpayment $" from the Payment; negative number) 
        * Payment Total $ (macro)
        * View (link to open the corresponding Member Payment record; displays as "Link")
      * Automatically sorted by: Payment ID (alphabetically; earliest at the top) 
      * Buttons to add/remove rows: N/A
      * Show 4 rows without scrolling
      * Other Notes: 
        * N/A



  


  * Total Payment Subtotals $ (read-only macro; number; 2 decimals; displays the sum of all "Subtotal $" values for "Complete" Payments from the "Member Payments" embedded spreadsheet for this Delivery Ticket)



  


  * Total Applied Overpayment $ (read-only macro; number; 2 decimals; displays the sum of all negative "Applied Overpayment $" values for "Complete" Payments from the "Member Payments" embedded spreadsheet) 



  


  * Total Paid to Member $ (read-only macro; number; 2 decimals; displays the sum of all "Payment Total $" values for "Complete" Payments from the "Member Payments" embedded spreadsheet)



  


  * Total Overpayment $ (visible if "Total Buyer Pmt (Pre-Discount) $" is greater than zero; read-only macro; number; 2 decimals; with the following behaviors:
    * displays the excess that was paid to the Member in the case of the "Buyer Invoice $" being higher than the Buyer Grade; i.e. displays the value of "Total Payment Subtotals $" \- "Total Member $", or "0.00" if the value is 0 or negative;
    * displays in gray text with "(Pending)" suffix until "Delivery Ticket Status" = "Closed", at which point it displays in black text if = zero, or in orange text if greater than zero) 
  * Unused Overpayment $ (visible if "Total Overpayment" ≠ "0.00"; read-only macro; number; 2 decimals; with the following behaviors: 
    * displays the value of "Total Overpayment" \- sum of "Applied $" values from the "Used Overpayments" embedded spreadsheet; 
    * displays in gray text with "(Pending)" suffix until "Delivery Ticket Status" = "Closed", at which point it displays in black text if = zero, or in orange text if greater than zero) 
  * Used Overpayments (visible if "Total Overpayment" ≠ "0.00" or if there are any rows on this embedded spreadsheet; read-only embedded spreadsheet with the following; includes a row for each "Complete" Member Payment with a row for the current Ticket on its "Applied Overpayments" embedded spreadsheet; used to document and track the Member Payment(s) & Delivery Ticket(s) to which the total overpayment for this Delivery Ticket was applied: 
    * Columns: 
      * Payment ID (macro; displays the "Member Payment ID" for Payments with an Applied Overpayment for this Delivery Ticket) 
      * Payment Date (macro) 
      * Applied Overpayment ID (column heading displays as "Appl. Overpmt. ID"; macro; displays the corresponding "Applied Overpayment ID") 
      * Applied $ (macro; displays the "Applied $" for the row from the Payment; negative number)
      * View Payment (displays as "Link"; link to open the corresponding Member Payment record)
    * Automatically sorted by: Payment Date (latest at the top)
    * Buttons to insert/append/remove rows: N/A
    * Show 4 rows without scrolling



  


  * Balance Due to Member $ (read-only macro; number; 2 decimals; with the following behaviors:
    * displays the remaining amount due to be paid to the Member, including any amount still due to the Member for this Delivery Ticket; i.e. displays the value of "Total Member $" \- "Total Payment Subtotals $", or "0.00" if the resulting value is 0 or negative;
    * includes "(Pending)" suffix if Delivery Ticket Status ≠ "Closed"; 
    * text color: 
      * displays in red text if "Next Payment Due Date" is on or before the current date; 
      * otherwise, displays in gray text until Delivery Ticket Status = "Closed", at which point it displays in standard black text) 
  * Next Payment Due Date (read-only macro; date; displays the due date for the "Next Member Due $" balance;
    * based on the Date Baseline for the selected Member Payment Terms ("Buyer Settlement Date" or "Ticket Date") and the Due Date configurations of the selected Member Payment Terms item;
    * displays one date at a time in the following sequence (note that these correspond to the same numbers in the other "Next" fields' specs):
      * 1\. If "Balance Due to Member $" = 0.00: Displays "N/A";
      * 2\. Otherwise, if the selected "Member Payment Terms" item has the "Uses Optional Early Payment" checkbox checked and there is no existing Payment with type of "Early Payment" and the current date is on or before the "Early Pay Due Date": Displays the "Early Pay Due Date";
      * 3\. Otherwise (if none of the above conditions apply): 
        * If "Buyer Settlement Date" is not blank (i.e. Ticket is "Closed"): Displays the date calculated based on the following items from the selected Member Terms: "Payment Due In" number of days, "Day Type", and "Date Baseline"; 
        * Otherwise, (if "Buyer Settlement Date" is blank): Displays "TBD"
    * displays in red if not "N/A" and is on or before the current date) 
  * Next Payment Type (read-only macro; plain text; with the following special behaviors:
    * displays one item at a time from the "Member Payment Types" list (note that these correspond to the same numbers in the other "Next" fields' specs):
      * 1\. If Condition #1 for "Next Payment Due Date" is met: Displays "N/A"
      * 2\. If Condition #2 for "Next Payment Due Date" is met: Displays "Early Payment";
      * 3\. If Condition #3 for "Next Payment Due Date" is met: Displays "Balance Payment")



  


  * New Member Payment (visible after the initial save for the Delivery Ticket; link; opens a new Member Payment record with "Delivery Ticket" defaulted)



  


  * Other Notes: 
    * In some cases, GemWood might want to manually set up and apply overpayments that do not come form a specific Ticket (for example, one Member selling logs to another Member, with GemWood handling the financials). In scenarios like this, a user could manually create a Member Payment for a past closed Delivery Ticket for the same Member, so that the Ticket shows an (extra) Overpayment, so that he has an Overpayment amount to apply.



  


Development Specification

Tim Reitz 12/13/2024: "Next Payment" Calculations Worksheet: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1684959456#gid=1684959456](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1684959456#gid=1684959456). 

Tim Reitz 03/12/2025: Updated. 

  


  


Change Requests: 

  * Tim Reitz 03/12/2025: [[[IN11201](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11203&)]] - ZGW - Delivery Ticket - Remove "Next $ Due to Member"
  * Tim Reitz 10/04/2025: [[[IN11653](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11655&)]] - ZGW - Clean up Various Labels
  * 


  


  


Ellis Miller 12/18/2024: 

[ ] Member payments and Used Overpayments are virtual RG's.

BID: 12 HOURS
