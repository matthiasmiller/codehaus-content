5.2.12. Contact - Invoices Section

  


Requirements

*Done.

  


  * Invoices section (standard section, with customizations; visible for all Contact Types; visible to the Client's agent, the Checkbook Holder for the agent's fund, and all admins): 
    * Invoices (standard; no label; read-only embedded spreadsheet showing Invoices for the Contact with "Status" ≠ "Canceled", with the following:
      * Columns: 
        * Invoice #
        * Date
        * Status
        * Amount
        * View (link to the Invoice record; displays as "Link")
      * Automatically sorted by:
        * First by: "Status" ("Invoiced" / "Draft" / "Paid")
        * Second by: "Date" (newest at the top)
      * Buttons to add/remove rows: N/A
      * Shows 4 rows without scrolling)
    * Current Uninvoiced Fees & Refunds (custom; read-only macro; number; 2 decimals; with the following details / behaviors:
      * displays the total of all uninvoiced items for the Contact, which is the sum of the following:
        * all uninvoiced items from the "Fees & Credits" tables on Vehicles with "Client Name" = the current Contact and "Billing Action" = "Invoice" and "Invoice" = blank;
        * all Contact Fees (i.e. HRD Fees) with "Effective Date" = the current date or in the past;
      * displays with a light yellow background if ≠ "0.00")
    * Prepare Invoice for Fees & Refunds (custom; button; opens the "Prepare Invoice" Child Screen - see corresponding spec) 



  


  * This client has <#> unpaid invoice(s) (custom; visible if the Contact has unpaid Invoices; on-screen message; "#" displays the corresponding number of Invoices)
  * View Unpaid Invoices (custom; visible if the Contact has unpaid invoices; link; prompts the user to save the record before opening; opens the "Unpaid Invoices for Contact" report) 
  * Print Statement (custom; visible if the Contact has unpaid invoices; link; opens the "Unpaid Invoices" (custom Statement) printout PDF for the Contact; prompts the user to save the record before opening) 
  * View All Invoices (standard; link; opens the "Invoices for Contact" report for the current Contact) 
  * Create Blank Invoice (standard; link; opens a blank new Invoice record for the current Contact) 



  


  


  * "Prepare Invoice for <Client Name>" Child Screen (custom; includes the following): 
    * Current Uninvoiced Fees & Refunds (unlabeled, read-only embedded spreadsheet with the following: 
      * Columns: 
        * Date (read-only macro; date; with the following details / behaviors: 
          * displays the "Fee Date" from the Fees & Credits embedded spreadsheet for Vehicle-related items or the "Effective Date" from the Fees embedded spreadsheet for High-Risk Driver Fee items; 
          * note that this corresponds to the Date on the Invoice itemization)
        * Vehicle (read-only macro; plain text; with the following details / behaviors: 
          * displays the Vehicle details in the following format: "<Year> <Make> <Model> <VIN>"; 
          * note that this is blank for High-Risk Driver fees, as those do not have a corresponding Vehicle record) 
        * View Vehicle (link; displays as "Link"; with the following details / behaviors: 
          * opens the corresponding Vehicle record, in a new tab if the current Contact record is in edit mode; 
          * note that a refresh of the Contact screen might be needed to display the updated Vehicle details if changes are made; 
          * note that this is blank for High-Risk Driver fees, as those do not have a corresponding Vehicle record) 
        * Type (read-only macro; displays the corresponding Sales Item that will be shown on the Invoice) 
        * Amount (read-only macro; number; 2 decimals; displays the dollar amount for the item, as a positive number for Fees or negative number for Refunds) 
      * Automatically sorted by: Date (most recent at the top)
      * Buttons to add/remove rows: N/A (none) 
      * Shows 12 rows without scrolling 
      * Other Notes: 
        * N/A) 
    * Total to be Invoiced (read-only macro; number; 2 decimals; displays the sum of all "Amount" values from the "Current Uninvoiced Fees & Refunds" embedded spreadsheet) 
    * Create Invoice (button; runs the "Create Invoice(s) Automatic Process" automatic process (see corresponding spec) to create an Invoice for the above listed uninvoiced items for the Client)



  


Other Notes: 

  * Custom: Note that the standard Silverloom "Statement" link is hidden, replaced by the custom "Print Statement" link, since the Solution uses a customized statement template.



  


Development Specification

Change Requests: 

  * Austin Priest 06/12/2023: [[[IN8252](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8254&)]] - ZWA - Changes to Print Statement PDF
  * Tim Reitz 08/19/2025: [[[IN11314](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11316&)]] - ZWA Multi-State Feature - Umbrella Incident
  * Tim Reitz 08/23/2025: [[[IN9943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9945&)]] - ZWA - Pre-ZWW - Vehicle Record - Fees & Credits - Add "Dismiss" Option for Fees
  * Tim Reitz 08/25/2025: [[[IN12020](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12022&)]] - ZWA - Contact Record - Invoices Section - Changes to "Current Uninvoiced Fees & Refunds"


