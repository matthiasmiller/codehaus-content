7.5.1.2. Buyer Payment - Payment Details Section

  * Payment Details section:  
    * Linked Delivery Tickets (embedded spreadsheet with the following; used to track the Delivery Tickets that have amounts ("sub-payments") applied to them from this Payment:  
      * Columns: 
        * Delivery Ticket (required; drop list of Delivery Tickets with Status = "Awaiting Buyer Payment" or "Awaiting Grade Report / Settlement" for the selected Buyer; filters down as you type; defaults to blank)
        * View (visible when a Delivery Ticket is selected; link to open the selected Delivery Ticket record; displays as "Link") 
        * Buyer's PO # (read-only macro; displays the "Buyer's PO #" for the selected Delivery Ticket) 
        * Buyer Payment Terms (read-only macro; displays the "Buyer Payment Terms" from the selected Delivery Ticket)
        * Invoice # (read-only macro; plain text; displays the "Invoice #" from the selected Delivery Ticket)
        * Invoice $ (read-only macro; number; 2 decimals; displays the "Buyer Invoice $" from the selected Delivery Ticket)
        * Due Date (read-only macro; date; displays the "Buyer Due Date" from the selected Delivery Ticket; displays in red font if this is before the "Payment Date" for the Buyer Payment) 
        * Pre-Discount $ (used to document the pre-discount amount being applied from this Payment record to the selected Delivery Ticket; with the following details / behaviors: 
          * required;
          * number; 2 decimals;
          * defaults to blank; 
          * if the sum of all "Pre-Discount $" values for a given Delivery Ticket across all Buyer Payment records = "Buyer Invoice $" for the Ticket, then the "Buyer Payment Finalized + Delivery Ticket Closed" checkbox on the Delivery Ticket record is automatically checked; 
          * warning on the field if "Buyer Paying Freight $" on the Delivery Ticket ≠ zero: "Please confirm that the Buyer's payment includes funds for freight - see "Buyer Paying Freight $" on the Ticket.")  
        * Discount $ (used to document the discount amount that the Buyer took off of the "Pre-Discount $" amount; with the following details / behaviors:
          * required;
          * number; 2 decimals;
          * defaults to blank;  
          * if this is set to a non-zero value and the "Est. Buyer Early Pay Due Date" for the Delivery Ticket is before the "Payment Date" date for this Buyer Payment, the value displays in orange font, and a warning message displays in orange with the "Details for Selected Load" \- see corresponding spec)
        * Discount % (with the following details / behaviors:
          * read-only macro;
          * displays the value of "Discount $" / "Pre-Discount $", rounded to the nearest 2 decimals;
          * displays here in purple font if one of the following is true: 
            * if this is greater than the "Est. Buyer Early Pay Discount %" for the corresponding Delivery Ticket, or 
            * if this is greater than 0 and if the "Est. Buyer Early Pay Discount %" for the corresponding Delivery Ticket is blank/not visible; 
          * note that if one of these conditions is true, an on-screen message is also displayed in purple below the "Details for Selected Load" \- see corresponding spec) 
        * Applied $ (read-only macro; displays the actual amount being applied to the selected Delivery Ticket for this row; displays the value of "Pre-Discount $" \- "Discount $")
        * Current Balance (value visible if the "Complete" checkbox is checked; read-only macro; dynamically displays the current "Est. Buyer Balance $" from the selected Delivery Ticket record)
      * Automatically sorted by: Delivery Ticket (greatest number at the top)
      * Buttons to insert/append/remove rows: "+" / "-" (hidden if the "Complete" checkbox is checked) 
      * Show 12 rows without scrolling 
      * Additional Validation: 
        * N/A



  


  * "Buyer Grade Report attachments are lacking for the following Ticket(s): <Ticket #<Ticket #>>, <Ticket #<Ticket #>>. Select the corresponding row from on the table and click "Upload Attachment" below." (on-screen message in red text; with the following details: 
    * visible if one or more Delivery Tickets meet the following conditions:
      * "Delivery Ticket "Status" ≠ "Closed" and 
      * "Buyer Grade Report Files" embedded spreadsheet is empty) 
  * "Buyer Grade $ is required for the following Ticket(s) since one or more Buyer Grade Report attachments are included: <Ticket #<Ticket #>>, <Ticket #<Ticket #>>. Click "Set / Update" to document the Buyer Grade $" (on-screen message in red text; with the following details: 
    * visible if one or more Delivery Tickets meet the following conditions: 
      * at least one attachment is included in the "Buyer Grade Report Files" embedded spreadsheet for a Delivery Ticket and 
      * "Buyer Grade $" for that Ticket = blank) 



  


  * Details for Selected Load (static label)
  * Upload Attachment (visible if the corresponding Delivery Ticket has no "Buyer Grade Report" attachments; link to upload a Buyer Grade Report file for the currently-select row in the "Linked Delivery Tickets" table; opens the upload screen as described in the corresponding spec)
  * View <X> File(s) (visible if the corresponding Delivery Ticket has one or more "Buyer Grade Report" files; "X" is the number of attached files; if 1 file, this opens that file directly; if more than 1 file, this opens the Buyer Grade Attachments Report, filtered to the selected Delivery Ticket -- see corresponding spec) 



  


  * Buyer Grade $ (read-only macro; number; 2 decimals; displays the "Buyer Grade $" from the currently-selected Delivery Ticket row) 
  * Set / Update (button; to the right of "Buyer Grade $"; with the following details:  
    * clicking this displays a prompt with the following:
      * Buyer Grade $ (required; number field; 2 decimals; for the user to enter a dollar amount)
      * "Cancel" (clicking this allows the user to close the prompt without updating the value)
      * "Confirm" (clicking this runs the "Set / Update Buyer Grade $ on Delivery Ticket from Buyer Payment" automatic process that updates the "Buyer Grade $" field on the currently-selected Delivery Ticket record)
    * prompt automatically closes when the process runs) 



  


  * "A discount is being applied after the Est. Buyer Early Pay Due Date for this Ticket (<Est. Buyer Early Pay Due Date>)." (message in orange text; with the following behaviors / details: 
    * visible if  "Discount $" for the corresponding row is set to a non-zero value and the "Est. Buyer Early Pay Due Date" for the Delivery Ticket is before the "Payment Date" date for this Buyer Payment;)
  * "The discount % is higher than the estimated discount % on the Ticket (<Est. Buyer Early Pay Discount %>)." (message in purple text; with the following behaviors / details: 
    * visible if one of the conditions for displaying "Discount %" in purple for the selected row is true (see corresponding spec); 
    * if "Est. Buyer Early Pay Discount %" on the Delivery Ticket is blank/not visible, "none" is displayed inside the parentheses in this message, instead of a percentage, to provide clarity to the user that no discount was planned/estimated for the Ticket)


