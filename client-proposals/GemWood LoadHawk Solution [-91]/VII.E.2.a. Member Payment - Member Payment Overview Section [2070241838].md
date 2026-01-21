7.5.2.1. Member Payment - Member Payment Overview Section

  


Requirements

  * Member Payment Overview section:
    * Status (same as the Status specced on the Buyer Payment Detail screen)
    * Internal Payment ID (same as the Internal Payment ID specced on the Buyer Payment Detail screen) 
    * Payment Category (same as the Payment Category specced on the Buyer Payment Detail screen) 



  


  * Left side:
    * Member Payment ID (auto-set and read-only; displays in the following format: "<Ticket #>p<sequential payment number for the selected Ticket, blank for the first>", i.e. "DHW0123p" for the first Payment linked to the Ticket, "DHW0123p2" for the second Payment, etc.; if a Payment record is deleted, subsequent Payment records for the same Ticket will still take the deleted Payment into account)
    * Member (auto-set and read-only; displays the Member for the selected Delivery Ticket; displays as a link to open the corresponding Member Contact record)
    * Delivery Ticket (with the following details / behaviors: 
      * required; 
      * read-only; set via the Delivery Ticket Choice Report;  
      * displays as a link to open the corresponding Delivery Ticket record; 
      * when set, the following field(s) are affected: 
        * "Payment Type": sets to the Next Payment Type" from the selected Delivery Ticket; 
      * if cleared, all dependent fields are cleared) 
    * Select Delivery Ticket (button; displays as an ellipsis button to the right of the "Delivery Ticket"; visible in Edit Mode if Payment "Status" ≠ "Complete"; opens the "Select Delivery Ticket Choice Report" as a child screen - see corresponding spec below)
    * Payment Terms (auto-set and read-only; displays the "Member Payment Terms" from the selected Delivery Ticket)
    * Payment Type (required; drop list of "Early Payment" and "Balance Payment" from the Member Payment Types list; with the following details / behaviors: 
      * if "Next Payment Type" for the selected Delivery Ticket is not blank: auto-set and read-only; sets to the "Next Payment Type" from the selected Delivery Ticket at the time that the "Delivery Ticket" field is set on the Payment;
      * if "Next Payment Type" for the selected Delivery Ticket is blank: editable) 
    * Due Date (date; with the following special behaviors:
      * if "Next Payment Due Date" for the selected Delivery Ticket is not blank: auto-set and read-only; displays the "Next Payment Due Date" from the selected Delivery Ticket at the time that the Delivery Ticket is selected on the Payment; 
      * if "Next Payment Due Date" for the selected Delivery Ticket is blank: required; defaults to the current date;
      * if this date is before the "Payment Date", displays in red font) 
    * Payment Date (required; date; defaults to the current date; validation warning on the field if set to a date after "Due Date": "Payment Date is after the Due Date.")
    * Confirmation # (optional; plain text field; wide enough for 12 characters; defaults to blank)



  


  * Right side:
    * Complete (editable if the "Canceled" checkbox is not checked; checkbox + date, which toggle; with the following details / behaviors: 
      * defaults to not checked, but automatically checks on the first Save after the record has been created; 
      * when the checkbox is checked, the date defaults to the current date) 
    * Canceled (editable if the "Complete" checkbox is not checked; checkbox + date, which toggle; with the following details / behaviors: 
      * defaults to not checked; 
      * when the checkbox is checked, the following things happens: 
        * the date defaults to the current date; 
        * "Applied $" is cleared and all rows from the "Applied Overpayments" embedded spreadsheet are deleted, to unlink the payment and applied overpayments from the Tickets; 
        * a warning message displays on the field: "All line items have been deleted and unlinked from Delivery Tickets. To undo, refresh the page before saving."
      * validate against canceling a Member Payment if it is referenced on the "Applied Overpayments" embedded spreadsheet on any other Member Payments - error message on the checkbox: "This payment cannot be canceled because overpayment from it has been applied to one or more other payments.") 
    * "No email address for Member - payment notice must be sent manually." (on-screen message in black text; visible after the initial Save for the record in the location of the "Send Member Payment Issued Email" link if the selected Member does not have any email addresses entered on their Contact record)
    * Add'l Notes for Member Payment Email (button; with the following behaviors: 
      * visible if the selected Member Contact has at least one email address; 
      * opens a child screen with an editable memo that can be edited by the user to add custom text to bottom of the standard email body on a per-Payment basis; 
      * memo remains editable if Status = "Complete" or "Canceled") 
    * Send Member Payment Issued Email (visible after the initial save for the record if the selected Member Contact has at least one email address; link; prompts the user to save the current record, then sends the email without a preview and sets the "Sent to Member" field to the current date and time; note that the user must refresh the screen to view the changes) 
    * Sent to Member (auto-set and read-only; this is the most recent date and time that the "Member Payment Issued" email was sent)
    * Print Member Payment Printout (visible after the initial save for the record; link; prompts the user to save the current record, then generates the "Member Payment / Delivery Ticket Printout" printout and opens it in the browser) 
    * Ticket Subtotal $ read-only macro; number; 2 decimals; with the following details / behaviors:
      * displays the "Applied $" from the "Payment on Ticket" embedded spreadsheet; example: "10,000.00") 
    * Applied Overpayment $ (read-only macro; number; 2 decimals; with the following details / behaviors:
      * displays the sum of the "Applied $" values from the "Applied Overpayments" embedded spreadsheet, as a negative number; example: "-3,000.00") 
    * Payment Total $ (read-only macro; number; 2 decimals; with the following details / behaviors: 
      * displays the sum of "Ticket Subtotal $" \+ "Applied Overpayment $"; example: (10,000.00) + (-3,000.00) = "7,000.00"; 
      * validate against negative numbers - error on Save: "Payment Total $ cannot be negative. Please adjust the applied $.")



  


Development Specification

Change Requests: 

  * Tim Reitz 02/25/2025: [[[IN11173](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11175&)]] - ZGW - Member Payment Detail Screen - Hide Email Option if Member Has No Email 
  * Tim Reitz 05/12/2025: [[[IN11383](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11385&)]] - ZGW - Member Payments - Validate Against Canceling Payments With Applied Overpayments
  * Tim Reitz 05/12/2025: [[[IN11384](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11386&)]] - ZGW - Member Payment - Add Validation Against "Payment Total $" Being Negative
  * Tim Reitz 05/22/2025: [[[IN11478](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11480&)]] - ZGW - Member Payment Detail Screen - Add "Print" Link
  * Ben Reitz 10/08/2025: [[[IN11556](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11558&)]] - ZGW - Member Payment record - Add "Sent" confirmation field


