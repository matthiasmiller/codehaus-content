25.2.2.1. Delivery Ticket - (OLD) Member Payments Section

  * Member Payments section:



  


_VA: Tim Reitz 11/22/2024: I think this moves to the Member Payment Record:

  * Applied Credits from Overpaid Tickets Applied Overpayments (embedded spreadsheet with the following; editable with "Edit Payments" permission; editable fields are editable until __; used to apply overpayments from other Delivery Tickets to the current Delivery Ticket, reducing the amount that would otherwise be due to the Member):



_DD: Tim Reitz 11/19/2024: What do you want to call this?

  * "Applied Overpayments"
  * "Applied Credits from Other Tickets"
  * "Applied Credits from Overpaid Tickets"



_VA: Tim Reitz 11/21/2024:

[ ] When created: Overpayment / Underpayments.

[ ] When used: Applied Overpayments (these are seen as credits back to GemWood).

_VA: Tim Reitz 11/21/2024: We don't need special handling or an ID for correcting underpayments to the Member. These would be handled as additional Payments on the same Ticket.

  


_DD: Tim Reitz 11/19/2024: Up until what point should we be able to add / remove overpayment items from other Tickets?

_VA: Tim Reitz 11/21/2024: Up until the point that the Member Payment is marked as Paid.

  * Columns:
    * Delivery Ticket (required; drop list of Delivery Ticket #s for the Member for which "Unused Overpayment" is greater than zero) 
    * Credit ID (auto-set and read-only; displays in the following format: "<Ticket #>c<sequential number for the Ticket>", i.e. "DHW0123c1", "DHW0123c2", etc.)



_VA: Tim Reitz 11/21/2024: GW sees this as the Member crediting the $ back to GW.

  * Unused Overpayment (auto-calculated and read-only; dynamically displays the current "Unused Overpayment" amount for the selected Delivery Ticket) 
  * Applied $ (required; number; 2 decimals; error on the field if entered value exceeds the the "Unused Overpayment" amount for the selected Delivery Ticket; defaults to blank) 
  * Applied Date (required; date; defaults to the current date)
  * View Ticket (displays as "Link"; link to open the selected Delivery Ticket record)


  * Automatically sorted by: Balance to Apply
  * Buttons to insert/append/remove rows: "+" / "-"
  * Show 4 rows without scrolling


  * Total Applied Overpayments (auto-calculated and read-only; displays the sum of "Applied $" values from the "Applied Credits from Other Tickets" embedded spreadsheet)



  


  


_VA: Tim Reitz 10/24/2024: Think through how to track when GW has taken the 2% early pay discount (so that we can display the warning if late, etc.). 

_VA: Tim Reitz 11/19/2024: I think we need to include early pay discount details (%, $, due date) on the Member Payments RG as well??

  


_VA: Tim Reitz 11/22/2024: This gets moved to: 

[X] Read-only RG on the Delivery Ticket 

[X] Logic and entry fields on the new Member Payment record. 

  


  * Member Payments (visible after the first save for the Delivery Ticket record; editable for users with the "Edit Payments" Permission; embedded spreadsheet with the following; used to track payments that are made to the Member for the Delivery Ticket):  
    * Columns: 
      * Payment ID (auto-set and read-only; displays in the following format: "<Ticket #>p<sequential number for the Ticket>", i.e. "DHW0123p1", "DHW0123p2", etc.)
      * Payment Type (required; editable if "Paid" checkbox for the row is not checked; drop list of the following items; defaults to blank; uses to track what type of payment this is, for due date & discount calculations;  
        * "Upfront Payment": visible if the selected Member Payment Terms has the "Uses Required Upfront Payment" checkbox checked; 
        * "Early Payment": visible if the selected Member Payment Terms has the "Uses Optional Early Payment" checkbox checked; 
        * "Payment in Full": always visible) 
      * Due Date (required; date; defaults to __ when the row is added)
      * Payment Amount $ (number; 2 decimals; with the following special behaviors; 
        * by default is auto-set and read-only, displaying __; 
        * if the "Override Amounts" checkbox is checked, is editable and required; 
        * if edited, displays a warning message on the field: "Are you sure you want to change the Amount?") 



_VA: Tim Reitz 10/28/2024: DD would like the Member Payment info to be auto-calculated, so that when they set up the ACH, they only need to check a checkbox to mark it as paid. 

  * Think through this for each Terms option (and how to handle for potential future Terms that might be set up). 
  * We probably should change "Balance" to "Current Balance" and auto-calc a total there (then use that field to determine if a payment is needed. 


  * Paid (checkbox; defaults to not checked; to be checked when the corresponding payment is sent to the Member)
  * Payment Date (required if the "Paid" checkbox is checked for the row; date; defaults to the current date when the "Paid" checkbox is checked; if the "Due Date" for the row is before the "Payment Date", this date displays in red font, and a warning displays on the field: "This Payment Date is after the Due Date.") 
  * Confirmation # (required if the "Paid" checkbox is checked for the row; plain text; defaults to blank) 
  * Notes (optional; plain text field; defaults to blank) 



_DD.: Tim Reitz 10/17/2024: Do you expect that you would always enter the payment when it actually is/has been made, or would you enter the values in ahead of time and come back to set the other details later?

Tim Reitz 10/17/2024: This affects the need to think through varying requirements (i.e. if Member Terms = Buyer Payment, then this wouldn't be required until after the Buyer Payment is received...). If always entering payments when/after they have been made, then SIMPLE - can require the fields right away.

_VA: Tim Reitz 11/04/2024: Client would like to go ahead and include these rows right away, with anticipated amounts & due dates (editable). 

_EM: Tim Reitz 11/19/2024: Thoughts on this?

Tim Reitz 11/19/2024: Should we actually add the rows here first (one at a time based on Due Date, or all anticipated payments based on the Terms)? Then display the upcoming unpaid one at the top as the "Next"?

_VA: Tim Reitz 11/19/2024: 

[X] Let's hide the RG & related fields until the first Save. Then make it visible and add the rows. 

[X] Default the due dates as able. 

[X] Default the $ amounts as able - ready only unless override checkbox (below) is checked  

[X] Could have an "Override Amounts" checkbox on the detail screen that makes all row Amounts editable. 

[X] Include a warning on the field "Are you sure you want to change the Amount?". 

  * Automatically sorted by: Due Date (latest at the top) + Payment Amount (largest at the top) 
  * Buttons to add/remove rows: "+" / "-" 
  * Show 4 rows without scrolling
  * Other Notes: 
    * After the first save for the Delivery Ticket record (when this embedded spreadsheet becomes visible), a row is automatically added for each anticipated payment to the Member, based on the selected "Member Payment Terms" item: 
      * If "Member Payment Terms" = "75% Upfront": Two rows are added, with the following fields auto-set: 
        * Row 1: 
          * Due Date: Current date + "Upfront Payment Due In [   ] Business Days"; for example 11/19/2024 + 1 = 11/20/2024; 
          * Payment Amount $: Value of ("Upfront Payment %" from the Terms record / 100) * "Total Member $", rounded to the nearest $250.00; for example: (75.00 / 100) * 11,550 = 8,662.50, rounded to 8,750.00; 



EM: Tim Reitz 11/19/2024: This is rather complex...

  * Row 2: 
    * Due Date: __



EM: Tim Reitz 11/19/2024: This gets really complex - there isn't a due date for the remainder payment until the Buyer Payment is settled. 

  * Payment Amount $: __



EM: Tim Reitz 11/19/2024: And this amount is only an estimate until they Buyer Payment is settled.... Should we try to defer this complex math for now, and have them manually add rows until they want to spend the money to design and build the automation? 

  * If "Member Payment Terms" = "2/10 net 30": One row is added, with the following fields set: 



_: total balance due on Ticket Date + 10 (for discount), or total balance due on Ticket Date + 30 (for full value) 

  * Row 1: 
    * Due Date: __
    * Payment Amount $: __


  * If "Member Payment Terms" = "After Buyer Settlement": 



_: total balance due ___ business days (or 1 business day) after first Buyer Payment date

  * Row 2: 
    * Due Date: __
    * Payment Amount $: __


  * Additional validations:
    * N/A


  * Total Paid to Member (visible after the first save for the Delivery Ticket record; auto-set and read-only; number; 2 decimals; displays the sum of all "Payment Amount $" values from the "Member Payments" embedded spreadsheet) 
  * Override Amounts (visible after the first save for the Delivery Ticket record; editable for users with the "Edit Payments" Permission; checkbox; defaults to not checked; if checked, all "Payment Amount $" fields on the "Member Payments" embedded spreadsheet become editable; if unchecked again, all "Payment Amount $" fields become read-only again) 



EM: Tim Reitz 11/19/2024: Do they continue to update dynamically with changes to the "Total Member $" (either when it's checked or unchecked or both)? 

  


  * Balance Due to Member (auto-set and read-only; number; 2 decimals; displays the value of "Total Member $" \- "Total Paid to Member", or "0.00" if the value is 0 or negative, i.e. displays the remaining amount due to be paid to the Member; displays in gray italicized text with "(Pending)" suffix until Delivery Ticket Status = "Closed" or "Canceled", at which point it displays in standard black text) 



  


  * Total Overpayment $ (auto-calculated and read-only; number; 2 decimals; displays the value of "__" \- "Total Paid to Member", or "0.00" if the value is 0 or negative, i.e. displays the excess that was paid to the Member in the case of the "Member Grade $" being higher than the Buyer Grade; displays in gray italicized text with "(Pending)" suffix until Delivery Ticket Status = "Closed" or "Canceled", at which point it displays in standard black text)



_DD: Tim Reitz 11/19/2024: What numbers do we look at here?

  * "Buyer Grade Report $" (assessed) OR "Total Buyer Pmt. (Pre-Discount) $
    * minus
  * "Total Member Grade $" ?



_VA: Tim Reitz 11/21/2024: This is calculated off of the post-discount $ from the Buyer.

_VA: Tim Reitz 11/21/2024: Maybe make this visible only if the buyer payment is greater than zero.

_VA: Tim Reitz 11/21/2024: If it's an Underpayment, it would be nice to make another payment to the Member while the Ticket is still open.

  * Used Overpayments (visible if "Total Overpayment" is not "0.00"; read-only embedded spreadsheet with the following; used to document and track the Delivery Ticket(s) to which the overpayment for this Delivery Ticket was applied)
    * Columns: 
      * Delivery Ticket (displays the "Delivery Ticket #")
      * Credit ID (displays the corresponding "Credit ID")
      * Applied $ (number; 2 decimals; displays corresponding "Applied $", i.e. the amount of overpayment from the current Delivery Ticket that was applied to the corresponding Delivery Ticket)
      * Applied Date (displays the corresponding "Applied Date")
      * Ticket Closed (date; displays the "Closed Date" from the corresponding Delivery Ticket; blank until that Ticket is closed)
      * View Ticket (displays as "Link"; link to open the corresponding Delivery Ticket record)
    * Automatically sorted by: Applied Date (latest at the top)
    * Buttons to insert/append/remove rows: N/A
    * Show 4 rows without scrolling
  * Unused Overpayment $ (visible if "Total Overpayment" is not "0.00"; auto-calculated and read-only; number; 2 decimals; displays the value of "Total Overpayment" \- total "Applied $" from the "Used Overpayments" embedded spreadsheet)


