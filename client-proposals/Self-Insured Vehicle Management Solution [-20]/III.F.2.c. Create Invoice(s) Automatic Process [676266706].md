3.6.2.3. Create Invoice(s) Automatic Process

  


Requirements

*Done. 

  


  * Name: "Create Invoice(s) Automatic Process" (informal) / "Contact Fees and Credits Import" (formal / coding)
    * Description:
      * This process creates Invoices for uninvoiced fees and refunds, and can be run in various ways with various outputs. Generally speaking, this includes Contact fees with eligible "Effective Date" values, and Vehicle fees with "Billing Action" = "Invoice".
      * This automatic process is run with an input report to set the prompts as needed ("Input Report for Contact Fees and Credits Import").
    * Prompts (on the Input Report for Contact Fees and Credits Import): 
      * All Clients? (checkbox; with the following details:
        * if checked, the process creates Invoices for all Clients with uninvoiced items that match the other criteria (note that in this case, the "Contact Name" and "Vehicle ID" prompts don't apply);
        * if not checked, the process creates Invoices a single Client, as specified in the "Contact Name" prompt;
        * note that if uninvoiced items exist for multiple Funds for the same Client, a separate invoice is created for each applicable Fund) 
      * Contact Name (plain text; with the following details:
        * required if "All Clients?" is not checked; 
        * if set, the process creates Invoices only for the selected Client) 
      * Vehicle ID (plain text; with the following details:
        * if set, the process creates Invoices for fee/refund items for the selected Vehicle, all for the the selected Client, and includes Contact fees for the selected Client if applicable;
        * if not set, the process creates Invoices for all Vehicles for the selected Client) 
      * Only Vehicle Fees? (checkbox; with the following details:
        * defaults to not checked; 
        * if checked, the process excludes Contact fees, and creates Invoices only for items for the selected Vehicle, for the selected Client or all Clients (if "Contact Name" is blank);
        * if not checked, the process includes Contact fees) 
      * Start Date (optional; date; with the following details:
        * defaults to blank = all;
        * looks at the Fee date ("Effective Date" for Contact fees and "Date" for Vehicle items); 
        * if set, the process includes items only within the set date range) 
      * End Date (optional; date; with the following details:
        * defaults to blank = all;
        * looks at the Fee date ("Effective Date" for Contact fees and "Date" for Vehicle items); 
        * if set, the process includes items only within the set date range) 
    * Initiated:
      * From the Admin menu, as part of the annual renewal process (Admin | Renewals and Printing | Create Annual Invoices):  
        * Summary: Creates Invoices for all eligible uninvoiced items (Contact, and Vehicle with "Billing Action" = "Invoice") with Fee Dates through the end of the Current Period End Date; 
        * When initiated from here, the filters are set as follows: 
          * "All Clients?": checkbox checked; 
          * "Contact Name": N/A (blank); 
          * "Vehicle ID": N/A (blank); 
          * "Only Vehicle Fees?": checkbox not checked; 
          * "Start Date": N/A (blank); 
          * "End Date": set to the Current Period End Date (as specified in Silverloom Settings); 
      * From the Contact record, when the "Create Invoice" button is clicked:  
        * Summary: Creates Invoices for all eligible uninvoiced items (Contact, and Vehicle with "Billing Action" = "Invoice") for the current Contact, with Fee Dates through the current date; 
        * When initiated from here, the filters are set as follows: 
          * "All Clients?": checkbox not checked; 
          * "Contact Name": set to the name of the current Contact; 
          * "Vehicle ID": N/A (blank); 
          * "Only Vehicle Fees?": checkbox not checked; 
          * "Start Date": N/A (blank); 
          * "End Date": set to the current date; 
      * From the Vehicle record, when the conditionally-visible "Create Invoice" button is clicked: 
        * Summary: Creates Invoices for all uninvoiced Vehicle items with "Billing Action" = "Invoice" for the Prior Owner of the current Vehicle; 
        * When initiated from here, the filters are set as follows: 
          * "All Clients?": checkbox not checked; 
          * "Contact Name": set to Vehicle's prior owner (per the "Prior Owner" macro); 
          * "Vehicle ID": set to the ID for the current Vehicle record; 
          * "Only Vehicle Fees?": checkbox checked;  
          * "Start Date": N/A (blank); 
          * "End Date": N/A (blank); 
    * Action(s): 
      * Creates Invoices based on the set prompts, as described above.



  


Development Specification

Change Requests: 

  * Tim Reitz 08/23/2025: [[[IN9943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9945&)]] - ZWA - Pre-ZWW - Vehicle Record - Fees & Credits - Add "Dismiss" Option for Fees



  


TODO_CCI1: Tim Reitz 08/18/2025: This process [for annual invoicing] is not including some historical items, but I don't know why. For example, there are items in the live system from prior to this year's annual process (i.e., earlier in 2025, from 2024, 2023, and even 2022). 

Could you see the question at the bottom of the incident body in [[[IN8249](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8251&)]] - ZWA - Invoicing Errors (Old Line Items Added to New Invoices)? (You can search for "TODO_CCI1" there.) 

Murshid Rahman 08/20/2025: I am taking a note and I will reply to this after a bit of testing on next week. Thanks.

Tim Reitz 08/22/2025: Ok, thanks! 

As a related / side note, I think time spent on this item could be tracked on the PC linked in the above CR, since it pertains to that job.
