7.5.2.2. Member Payment - Ticket Details Section

  * Ticket Details section:
    * Left side:
      * Load Type (read-only macro; displays the "<Thickness> <Species> <Grade>" (i.e. "4/4 WO Rift") for the first row in the Load Itemization table for the selected Delivery Ticket)
      * Buyer (read-only macro; displays the "Buyer" from the selected Delivery Ticket; the name is a link to open the corresponding Contact record)
      * Buyer's PO # (auto-set and read-only; displays the Purchase Order from the selected Delivery Ticket, if one is selected there; the PO # is a link to open the corresponding Purchase Order record)
      * View Purchase Order Attachment(s) (visible if "Buyer's PO #" is not blank; if the Purchase Order has more than 1 attached file, this opens the "Purchase Order Attachments" report, filtered to the Purchase Order - see corresponding spec; if just 1 file, this bypasses the report screen to open that file directly; if no files, this opens the blank report) 
      * "One or more values do not match the current values on the Delivery Ticket. Update the incorrect values to match, then save." (on-screen message in red font; visible if one or more of the following conditions are met: 
        * "Ticket Value $" does not equal "Ticket Value $" on the corresponding Delivery Ticket; 
        * "GemWood Fee $" does not equal "GemWood Lumber Brokerage Fee $" on the corresponding Delivery Ticket; 
        * "GW Discount $" does not equal "GemWood Discount $" on the corresponding Delivery Ticket; 
        * "Member $" does not equal "Total Member $" on the corresponding Delivery Ticket)



  


  * Right side:
    * Ticket Value $ (normally auto-set and read-only stored field; set to the "Ticket Value $" from the corresponding Delivery Ticket when a Ticket is selected; dynamically displays in gray font if "Delivery Ticket Status" ≠ "Closed") 
      * If this does not equal the "Ticket Value $" from the corresponding Delivery Ticket, this field is editable and the value from the Delivery Ticket displays in red font (read-only macro) to the right of this field. 
    * GemWood Fee $ (normally auto-set and read-only stored field; displays the "GemWood Lumber Brokerage Fee $" from the corresponding Delivery Ticket when a Ticket is selected; dynamically displays in gray font if "Delivery Ticket Status" ≠ "Closed") 
      * If this does not equal the "GemWood Lumber Brokerage Fee $" from the corresponding Delivery Ticket, this field is editable and the value from the Delivery Ticket displays in red font (read-only macro) to the right of this field. 
    * GW Discount $ (normally auto-set and read-only stored field; displays the "GemWood Discount $" from the corresponding Delivery Ticket when a Ticket is selected)
      * If this does not equal the "GemWood Discount $" from the corresponding Delivery Ticket, this field is editable and the value from the Delivery Ticket displays in red font (read-only macro) to the right of this field. 
    * Member $ (normally auto-set and read-only stored field; displays the "Total Member $" from the corresponding Delivery Ticket when a Ticket is selected; dynamically displays in gray font if "Delivery Ticket Status" ≠ "Closed") 
      * If this does not equal the "Total Member $" from the corresponding Delivery Ticket, this field is editable and the value from the Delivery Ticket displays in red font (read-only macro) to the right of this field. 
    * "Note: Values in gray font are current estimates, pending Buyer settlement." (visible if "Delivery Ticket Status" ≠ "Closed"; on-screen message)


