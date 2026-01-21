5.2.11. Contact - Fees Section

  


Requirements

*Done. 

  


  * Fees section (custom section; with the following visibility and editability conditions:
    * visible to the Client's agent, the "Checkbook Holder" for the Agent's Fund, and all Admin users if one or both of the following are true:
      * if the selected "Contact Type" for the record has "Client?" = "Yes";
      * if there are any rows in the "Contact Fees" embedded spreadsheet;
    * note that additional visibility conditions may apply to specific fields (i.e. Admin-only);
    * all fields are editable for Admin users only):



  


  * Assess High-Risk Driver Fee (button; only visible for admin users; opens a child screen with the following:
    * Prompts:
      * "Driver Name" (drop list of "Household Drivers" for the current Contact; defaults to blank);
      * "Fee" (number; 2 decimals; defaults to "1,000.00")
    * "Confirm" (button; when clicked with both prompts set, three rows are added to the "Contact Fee" embedded spreadsheet, with "Effective Date" set to the following three dates:
      * The current date;
      * The Current Period End Date (June 30);
      * The Next Period End Date (June 30))



  


  * Contact Fees (no label; embedded spreadsheet with the following; used to track Contact fees (currently only High-Risk Driver Fees), including paid, invoiced, and upcoming: 
    * Columns: 
      * Effective Date (required; date; defaults to the current date; editable for Admin users if there is no invoice number entered)
      * Owner (required; drop list of all Contacts with for which the "Contact Type" has "Client?" = "Yes"; defaults to the current Contact; editable for Admin users if the row is not linked to an Invoice, i.e. "Invoice" is blank) 
      * Driver (required; drop-list of "Household Drivers" for the current Contact; defaults to blank; editable for Admin users if "Invoice" is blank) 
      * Type (required; drop list of blank and "High-Risk Driver Fee" (from the "Sales Items List"); defaults to "High-Risk Driver Fee"; editable for Admin users if "Invoice" is blank)
      * Fund (required; drop-list of all Funds; defaults to the Contact's Agent's Fund; editable for Admin users if "Invoice" is blank; note that when a Fund change happens for an Agent, the Fund associated with uninvoiced fees does not change)
      * Invoice (auto-set and read-only; sets to the Invoice # when the row is included on the Itemization of an Invoice)
      * Status (read-only macro; displays the current Status of the linked Invoice)
      * Amount (required; number; two decimals; defaults to "1,000.00"; editable for Admin users if there is no invoice number entered)
      * View (link to invoice; displays as "Link")
    * Automatically sorted by: N/A (none) 
    * Buttons to add/remove rows: 
      * "+" (visible only for Admin users)
      * "-" (visible only for Admin users; hidden if the selected row is linked to an Invoice)
    * Shows 7 rows without scrolling 



  


  * View High-Risk Drivers (visible to Admin users; prompts the user to save the record before opening; opens the "High-Risk Drivers" report, with the "Client or Vehicle Owner Name" filter set to the current Contact)



  


Development Specification

TODO_CR: Tim Reitz 08/20/2025: The "Owner" column / field drop list currently includes all client Contacts, meaning that a fee could be added for any client. I'm not sure why it doesn't filter down to just the current contact (other than that it could be due to the Transfer Fees process for new Contacts). Perhaps we should eventually make this be auto-set and read-only interactively (editable only via import), to eliminate chances of fees being set for other clients.
