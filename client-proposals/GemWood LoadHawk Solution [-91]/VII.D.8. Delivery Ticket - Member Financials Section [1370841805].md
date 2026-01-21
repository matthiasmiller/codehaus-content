7.4.8. Delivery Ticket - Member Financials Section

  * Member Financials section:
    * GemWood Lumber Brokerage Fee % (number; 2 decimals; with the following behaviors:
      * defaults to the corresponding value from Silverloom Settings as of the time that the Delivery Ticket record was created and does not automatically change if the setting is updated;
      * required and editable for users with the "Manage Financials" Permission; read-only for all other users)
    * Original GemWood Lumber Brokerage Fee $ (hidden; read-only macro; number; 2 decimals; with the following notes/behaviors:
      * used for calculations of numbers that are based on the "Buyer Invoice $" and that should not change based on the Buyer Payments - see below;
      * dynamically displays the rounded value of "GemWood Lumber Brokerage Fee %" * "Buyer Invoice $")
    * GemWood Lumber Brokerage Fee $ (read-only macro; number; 2 decimals; with the following details / behaviors:
      * dynamically displays the rounded value of "GemWood Lumber Brokerage Fee %" * "Ticket Value $";
      * displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text) 



  


  * Original Member Subtotal $ (hidden; read-only macro; number; 2 decimals; with the following details / behaviors:
    * used for calculations of numbers that are based on the "Buyer Invoice $" and that should not change based on the Buyer Payments, specifically the "Early Pay Discount $;
    * dynamically displays the rounded value of "Buyer Invoice $" \- "Original GemWood Lumber Brokerage Fee $")
  * Member Subtotal $ (hidden; read-only macro used for main calculations; dynamically displays the value of "Ticket Value $" \- "GemWood Lumber Brokerage Fee $") 
  * Cached Member Subtotal $ (hidden; auto-set and read-only; with the following details / behaviors: 
    * number; 2 decimals; 
    * is auto-set to the current value of "Member Subtotal $" on every Save; 
    * not used for calculations anywhere, but included for debugging purposes (available via Modification History))



  


  * Member Payment Terms (editable and required if there are no linked non-Canceled Member Payment records for the Delivery Ticket; drop list of "Member" Payment Terms items; with the following behaviors: 
    * defaults to the "Default Member Payment Terms" from the selected Member's Contact record as of the time that the Member is selected on the Delivery Ticket;
    * the selection here automatically affects the Solution's handling of logic and calculations for due dates, early pay discounts, etc., so when this is set or changed, the following are also subsequently set/updated:
      * "GemWood Early Pay Discount %": defaults per the selected Member Terms; 
      * "GemWood Early Pay Due Date": defaults to the calculated date, based on the selected Member Terms; 
    * validation error on Save if "No Member Grade" checkbox is checked and this ≠ "After Buyer Settlement": "No Member Grade: Member Payment Terms must be set to "After Buyer Settlement"";
    * note that changes to this spec should be considered for the Buyer Payment Terms drop list as well) 



  


  * GemWood Early Pay Due Date (visible if the selected Member Payment Terms item has the "Uses Optional Early Payment" checkbox checked; date; with the following behaviors:
    * editable and required for users with the "Manage Financials" Permission; read-only for all other users;
    * is set / updated when "Ticket Date" is set / updated, based on the "Ticket Date" plus the "Early Pay Window [ ] Calendar Days from Ticket Date" for the selected Member Payment Terms item)
  * GemWood Early Pay Discount % (visible if the selected Member Payment Terms item has the "Uses Optional Early Payment" checkbox checked; number; 2 decimals; with the following behaviors:
    * defaults to the "Early Pay Discount %" on the selected Member Payment Terms record as of the time that the Terms were selected on the Delivery Ticket;
    * editable and required for users with the "Manage Financials" Permission; read-only for all other users; 
    * does not automatically update if the default is changed on the Member Payment Terms record; 
    * does update if "Member Payment Terms" is changed; 
    * read-only and displays in gray text with an "(N/A)" suffix if the current date is after the "GemWood Early Pay Due Date", and no "Early Payment" exists for the Delivery Ticket;
    * note that changes to this spec should be considered for the Buyer side as well)
  * GemWood Early Pay Discount $ (visible if the selected Member Payment Terms item has the "Uses Optional Early Payment" checkbox checked; read-only macro; number; 2 decimals; with the following behaviors:
    * dynamically displays the rounded value of "Original Member Subtotal $" * "GemWood Early Pay Discount %";
    * displays in gray text with an "(N/A)" suffix if not applicable (i.e. if the current date is after the "GemWood Early Pay Due Date" and no "Early Payment" exists for the Delivery Ticket);
    * note that this does not change if the "Total Buyer Payment $" ends up being different from the "Buyer Invoice $", since this is based on the latter; 
    * note that changes to this spec should be considered for the Buyer side as well)
  * GemWood Discount $ (hidden; read-only macro; number; 2 decimals; with the following behaviors: 
    * displays the following: 
      * "GemWood Early Pay Discount $" if that is non-zero and applicable (i.e., not gray text with"(N/A)" suffix); 
      * otherwise, "0.00")



  


  * Total Member $ (read-only macro; number; 2 decimals; with the following behaviors:
    * this is the Members' portion for the load;
    * displays the value of "Member Subtotal $" \- "GemWood Discount $";
    * displays in gray text with "(Pending)" suffix until Delivery Ticket Status = "Closed", at which point it displays in standard black text)



  


  * Cached Discounted Member $ (hidden; auto-set and read-only; with the following details / behaviors: 
    * number; 2 decimals; 
    * is auto-set to the current value of "Total Member $" on every Save; 
    * not used for calculations anywhere, but included for debugging purposes (available via Modification History))


