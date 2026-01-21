7.5.2.4. Member Payment - Applied Overpayments Section

  * Applied Overpayments section:
    * Applied Overpayments (no label; embedded spreadsheet with the following; used to apply overpayments from other Delivery Tickets to the current Delivery Ticket as a negative number, reducing the amount that would otherwise be due to the Member for the Delivery Ticket; 
      * Columns: 
        * Type (read-only macro; displays the "Applied Overpayment" list item)
        * Ticket # (required; drop list of Delivery Ticket #s for the Member for which "Unused Overpayment $" is greater than zero; error on the field if another row on the same Member Payment record is set to the same Ticket #: "Duplicate rows not allowed.") 
        * Applied Overpayment ID (label displays "ID"; auto-set and read-only; displays in the following format: "<Ticket #>c<sequential number for the Ticket>", i.e. "DHW0111c1", "DHW0111c2", etc.; note that the "c" stands for "credit", carried over from GemWood's previous solution and numbering convention) 
        * Ticket Date (auto-set and read-only; displays the "Ticket Date" for the row's Delivery Ticket) 
        * Orig. Total $ (auto-set and read-only stored field; sets to the "Total Overpayment $" for the row's Delivery Ticket, as of the time that the "Ticket #" was selected on the row)
        * Balance $ (read-only macro; dynamically displays the current "Unused Overpayment $" for the row's Delivery Ticket, including the current Payment) 
        * Applied $ (required; number; 2 decimals; defaults to the "Balance $" for the row; error on the field and on Save if if Payment "Status" ≠ "Complete" and entered value exceeds the the "Balance $": "Applied $ exceeds current Balance $.") 
        * View (displays as "Link"; link to open the selected Delivery Ticket record) 
      * Automatically sorted by: N/A 
      * Buttons to insert/append/remove rows: "+"/"-" (visible if Payment "Status" ≠ "Complete")
      * Show 6 rows without scrolling 
      * Additional Validation: 
        * N/A


