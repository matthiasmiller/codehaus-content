6.9.2.2. Agreement - Billing Details Section

  


Requirements

  * Billing Details section: 
    * Payables Contact Name (optional; drop list of Individual Contacts that are linked to the Customer; default to blank; the contact selected here is the one who receives the emails for Page Count Request and Page Count Reminder)
    * View/Edit Contact (visible if a Payables Contact is selected; opens the selected Contact's record) 
    * Billing Address (required; drop list of Billing-type addresses for the selected Customer; displays the full address)



TODO_EM: Tim Reitz 07/31/2023: What's the right way to do the address drop list + auto-filled fields? (see the 2 yellow highlights on the mockup). 

Tim Reitz 08/03/2023: Thoughts from Matthias: 

Dev Spec:

\- either use a choice report, or

\- have a macro that generates a string table where the first column is the drop list value, and the right column is all the address components (show a drop list of addresses and store the selected address into fields (i.e. have a macro that....)) 

  * Street (auto-filled and read-only; based on the selected Address)
  * City (auto-filled and read-only; based on the selected Address)
  * State (auto-filled and read-only; based on the selected Address)
  * Zip (auto-filled and read-only; based on the selected Address)
  * Phone (auto-filled and read-only; if a Payables Contact is selected, defaults to that Contact's primary Phone number, if no Payables Contact is selected, defaults to the selected Customer's primary Phone number)
  * Fax (auto-filled and read-only; if a Payables Contact is selected, defaults to that Contact's Fax number, if no Payables Contact is selected, defaults to the selected Customer's Fax number; if multiple Fax numbers are listed in either case, this looks at the highest one on the list)
  * Email (auto-filled and read-only; if a Payables Contact is selected, defaults to that Contact's primary Email address, if no Payables Contact is selected, defaults to the selected Customer's primary Email address)



  


  * Black Meter Billing Type (visible and required if there is at least one "Printer" type Device in the Billing Group; drop list of Per Group, Per Device; if "Per Group" is selected, all printers in the Agreement's Billing Group have their included black pages and black page usage combined for billing) 
  * Group Black Allotment (visible if Black Meter Type = Per Group; auto-set and read-only; displays the sum of "Included Black Pages" for all printers in the Billing Group) 
  * Group Black Overage $ (visible and required if Black Meter Type = Per Group; number field to 3 decimals; dollar amount per page for all color pages used beyond the group's allotment)
  * Color Meter Billing Type (visible and required if there is at least one "Printer" type Device in the Billing Group; drop list of Per Group, Per Device; if "Per Group" is selected, all printers in the Agreement's Billing Group have their included black pages and black page usage combined for billing) 
  * Group Color Allotment (visible if Color Meter Type = Per Group; auto-set and read-only; displays the sum of "Included Color Pages" for all printers in the Billing Group) 
  * Group Color Overage $ (visible and required if Color Meter Type = Per Group; number field to 3 decimals; dollar amount per page for all color pages used beyond the group's allotment)



  


  * Total Monthly Base Price (read-only; sum of Monthly Base Prices for all included Manged Devices)
  * Base Price Billing Frequency (required; drop list of Monthly, Quarterly, Annually; applies only to base charges since page counts will all be billed quarterly)
  * Billing Start Date (required; date field; defaults to the first date of the month following the Agreement Creation Date; used as the starting point for the Billing Frequency; becomes read-only when there is at least one linked invoice on the Invoices embedded spreadsheet)
  * Generate Supplemental Invoice (Phase 4) (button; visible if the Agreement Creation Date is more than 7 calendar days before the Billing Start Date; clicking this link generates a new Invoice for the Customer for any Base Prices, rounded to the nearest 1/4 month in the future (1st, 8th, 15, or 22nd); disappears once it has been clicked)



TODO_EM: Ben Reitz 09/21/2023: are you fine with this design?

TODO_JM: Ben Reitz 09/21/2023: are you fine with this design?

TODO_IDD4: Ben Reitz 09/21/2023: spec out a background process for this button

  


  * Invoices (embedded spreadsheet that displays the invoices for the Agreement, with the following:)
    * Columns: 
      * Customer (Phase 3: required; drop list of Customers; defaults to the current Customer on the Agreement record)
        * Phase 4: details to be determined; probably defaults to the customer on the linked invoice 
      * Billing Cycle Start Date (Phase 3: blank field; details to be determined in Phase 4)  
      * Billing Cycle End Date (Phase 3: blank field; details to be determined in Phase 4)
      * Amount (Phase 3: required; number field to 2 decimals
        * Phase 4: details to be determined
      * Invoice Date (Phase 3: required; date field)
        * Phase 4: details to be determined
      * Invoice # (Phase 3: optional; plain text field; manually filled with an invoice number)
        * Phase 4: To be auto-set when an invoice is linked to the row
      * Invoice Status (Phase 3: blank)
        * Phase 4: auto-set and read-only; displays the Status of the corresponding Invoice 
      * View (Phase 4; displays "Link" if there is a linked invoice for the fee; opens the corresponding invoice) 
    * Automatically sorted by: Invoice Date
    * Buttons to insert/append/remove rows: N/A
    * Show 6 rows without scrolling
    * Other Notes:
      * Phase 4 will determine exactly how invoices are linked to Agreements, but there probably will be a custom field for "Agreement" on the Invoice record.



  


Development Specification

Tim Reitz 08/01/2023: At his point the client is fine with having the Agreement Total Base Charge be the sum of the devices' base charges, but a possible future feature: add an RG for recurring charges:  

  * Start Date
  * End Date 
  * Sales Item 
  * Amount
  * Description


