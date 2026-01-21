7.4.6. Delivery Ticket - Buyer Payments Section

  


Requirements

  * Buyer Payments section: 
    * Total Buyer Pmt. (Pre-Discount) $ (read-only macro; number; 2 decimals; this represents the pre-discount amount of Buyer Payment funds applied to the Ticket; with the following special behaviors:
      * displays the sum of "Pre-Discount $" columns on the Buyer Payments embedded spreadsheet;
      * displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text;
      * the "Closed" checkbox is automatically checked if this amount is not zero and matches the "Buyer Invoice $" - see the spec on the "Closed" checkbox for the Delivery Ticket and the spec for the "Pre-Discount $" on the Buyer Payment) 
    * Total Buyer Discount $ (read-only macro; number; 2 decimals; displays the sum of "Discount $" columns on the Buyer Payments embedded spreadsheet; displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text)
    * Total Buyer Discount % (read-only macro; number; 2 decimals; displays the calculated discount %, rounded to the nearest 2 decimals; i.e. "(<"Total Buyer Discount $"> / <"Total Buyer Pmt. (Pre-Discount) $">) * 100"; displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text)



  


  * Total Buyer Payment $ (read-only macro; number; 2 decimals; with the following details / behaviors: 
    * displays the value of "Total Buyer Pmt. (Pre-Discount) $" \- "Total Buyer Discount $"; 
    * this is the amount that is used as the benchmark for Member Payments, Sales Commission, and Internal Fee Payouts after the Delivery Ticket is closed; 
    * displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text) 
  * Buyer Settlement Date (visible if "Delivery Ticket Status" = "Closed"; read-only macro; date; displays the "Payment Date" of the most recent Buyer Payment for this Ticket; hidden and N/A (blank) if the Ticket is not "Closed")



  


  * Total Claim $ (read-only macro; number; 2 decimals; with the following details / behaviors: 
    * displays the value of "Buyer Invoice $" \- "Total Buyer Payment $" (post-discount); 
    * this accounts for any differences in grade and any discounts; 
    * may be positive, negative, or zero; 
    * displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text) 
  * Total Claim % (read-only macro; number; 2 decimals; with the following details / behaviors: 
    * displays the calculated claim %, rounded to the nearest 2 decimals; i.e. "(<"Total Claim $"> / <"Total Buyer Payment $">) * 100"; 
    * displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text) 



  


  * Est. Buyer Balance $ (visible if "Delivery Ticket Status" is not "Closed"; read-only macro; number; 2 decimals; displays the value of "Buyer Invoice $" \- "Total Buyer Pmt. (Pre-Discount) $"; displays in gray text with "(Estimate)" suffix)



  


  * Buyer Payments (read-only embedded spreadsheet with the following; includes a row for each "Complete" Buyer Payment record that has an amount that applies to this Delivery Ticket: 
    * Columns: 
      * Payment ID (hidden column; macro; plain text; displays the "Internal Payment ID" from the linked Buyer Payment); 
      * Buyer (macro; displays the "Buyer" from the linked Buyer Payment);
      * Payment Total $ (macro; displays the "Payment Total $" from the linked Buyer Payment);
      * Payment Date (macro; date; displays the "Payment Date" from the linked Buyer Payment);
      * Pre-Discount $ (macro; number; 2 decimals; displays the "Pre-Discount $" for this Ticket from the linked Buyer Payment);
      * Discount $ (macro; number; 2 decimals; displays the "Discount $" for this Ticket from the linked Buyer Payment);
      * Applied $ (macro; number; 2 decimals; displays the "Applied $" for this Ticket from the linked Buyer Payment);
      * View (link to open the corresponding Buyer Payment; displays as "Link");
    * Automatically sorted by: 
      * First by: Payment Date (most recent at the top); 
      * Second by: Payment ID (lowest at the top); 
    * Buttons to insert/append/remove rows: N/A;
    * Show 4 rows without scrolling)
  * New Buyer Payment (visible if Delivery Ticket Status = "Awaiting Buyer Payment" or "Awaiting Grade Report / Settlement"; link; opens a new Buyer Payment record with the "Buyer" defaulted and a new row automatically added to the "Linked Delivery Tickets" embedded spreadsheet for the current Delivery Ticket)



  


Development Specification

Ellis Miller 12/18/2024: 

  


USA: 12 HOURS
