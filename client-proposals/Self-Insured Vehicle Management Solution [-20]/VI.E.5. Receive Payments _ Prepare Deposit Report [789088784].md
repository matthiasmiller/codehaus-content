6.5.5. Receive Payments / Prepare Deposit Report

  


Requirements

Overview: This is a report of unpaid invoices for a selected agent's clients.

  


Accessed from: Home | Invoices | Receive Payments / Prepare Deposit (for Admin users, opens a prompt screen with the "Agent" prompt; for non-admins, opens the report directly)

  


Title: Prepare Deposit 

  


Left pane: This is a report that displays Invoices with "Status" = "Invoiced" for Clients of the selected Agent.

Title: Prepare Deposit

  


Preface: N/A 

  


Columns: 

  * Client
  * Invoice Date
  * Invoice # (link to record)
  * Invoice Status
  * Invoice Total (total row displays sum)
  * Invoice Balance (total row displays sum)



  


Grouped by: Client

  


Sorted by: Invoice Date (earliest at the top) 

  


Filters: 

  * Agent (required; drop list of "In-State Agent"-Type Contacts; with the following details: 
    * limiting the drop list items: 
      * for Admin users: includes all "In-State Agent"-Type Contacts (no limiting); 
      * for non-Admin users who are the "Checkbook Holder" for a Fund: includes the current user's Contact and all Agents who use their Fund; 
      * for all other non-Admin users: includes only the current user's Contact; 
    * defaults to the Contact for the current user) 



  


  


Top right pane: This is a report that includes one row for every undeposited payment for Invoices displayed in the left pane. 

Title: Deposit Helper

  


Preface: N/A 

  


Columns:

  * Client (link to Client record)
  * Payment Date
  * Payment Amount (total row displays sum)
  * Payment Check #
  * Invoice #



  


Grouped by: 

  * First by: Invoice contact (Client)
  * Second by: Check # / Cash



  


Sorted by: Invoice # 

  


Row-Specific Buttons:

  * Cancel Payment (accessed by hovering over the first column in the right pane; row-specific; with the following behaviors: 
    * for a check payment, it cancels (removes the row in the Payments embedded spreadsheet) the undeposited check payments from every Invoice that was paid by this check; 
    * for a cash payment, it cancels undeposited cash payments for this Client and Payment Date)



  


  


Bottom right pane: This is a totals-only report that displays the total quantity and balance of the selected Invoices in the left pane.

Title: Total of Selected Invoices 

  


Preface: N/A 

  


Columns: 

  * # Invoices Selected (displays the number of invoices selected in the left pane) 
  * Total Balance for Selected (displays the sum of the unpaid amounts (as displayed in the Invoice Balance column) for the selected invoices in the left pane) 



  


  * Grouped by: N/A



  


  * Sorted by: N/A



  


  


Buttons: 

  * Pay Selected Invoices (technically on the left pane; with the following details / behaviors: 
    * opens a prompt with the following: 
      * Check Payment (checkbox; default to checked)
      * Payment Amount (required; number field to 2 decimal places; defaults to blank) 
      * Payment Date (required; defaults to the current date) 
      * Check Number (visible and required if "Check Payment" is checked; number; 0 decimals; defaults to blank) 
      * Conditionally visible message: "Warning: You have selected invoices for more than one client."



Austin Priest 06/25/2025: _TR I am not seeing this message. Is this a bug or is the spec outdated?

_CCI1: Tim Reitz 07/19/2025: Could you give input on this? Thanks!

Murshid Rahman 08/19/2025: I think this was never coded. Please see [[PC0141793]] for the job. Thanks 

TODO_VA: Follow up. 

TODO_: Tim Reitz 10/04/2025: Do we think this message is important / necessary? Probably is worthwhile to help out the users. 

  * clicking "Continue" does the following: 
    * Applies the payment to the selected Invoices from oldest to newest based on Invoice #.
    * An error is given if "Payment Amount" exceeds the invoice total: "Check amount is more than the total due for the selected invoices. (Field: SalesFormInvRecordedPmntOverpayFail; Row: <Row ID>) (Record: <Record Id>)".
    * Sets the "Deposited By" field on the Invoice to the selected Agent. 
    * If invoices for multiple clients are selected, payment is still applied to the invoices from oldest to newest  (this allows for one party to pay for multiple clients' invoices). 
    * Sets the Deposit Date and User for cash payments.
  * The report screen automatically refreshes to show the updated reports.


  * Finalize Deposit (technically on the top right pane; used to mark all checks for all invoices in the report as deposited): 
    * This opens a prompt for the following: 
      * "All checks of the agent will be deposited irrespective of selected rows." (message) 
      * Deposit Date (required; defaults to the current date) 
    * Clicking "Continue" updates all undeposited payments as being deposited as of that date.
      * If there is no "Due Amount" and no undeposited lines then "Status" is changed to "Paid"
  * Deposit Breakdown (technically on the top right pane; opens the Deposit Breakdown report for the selected Agent - see corresponding report spec) 



  


Other Notes: 

  * The following data access limitations apply to the report itself (in addition to the limitations on the filter drop list):
    * Admin can view the report for all agents
    * Non-Admin checkbook holders can view the report for themselves and all of the Agents using their Fund.
    * Non-Admin, non-checkbook holder agents can only view the report for themselves.



  


Development Specification

Change Requests: 

  * Austin Priest 08/09/2023: [[[IN8336](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8338&)]] - ZWA - Receive Payments / Prepare Deposit - Unable to cancel pending cash deposits
  * Austin Priest 07/03/2023: [[[IN8312](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8314&)]] - ZWA - The Prepare Deposit report continues to show partially paid invoices as undeposited
  * Tim Reitz 08/23/2025: [[[IN12002](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12004&)]] - ZWA - Receive Payments / Prepare Deposit Report - Fix Filter Visibility


