6.5.6. Deposit Breakdown Report

  


Requirements

*Done. 

  


Overview: This is a custom report of Invoices with deposits.

  


Accessed from: Home | Invoices | Deposit Breakdown (for Admin users, opens a prompt screen with the "Agent" prompt; for non-admins, opens the report directly) 

  


Title: Deposit Breakdown

  


Left pane: This pane shows Invoices with "Status" = "Invoiced" or "Paid", based on the filter selections.

Title: Deposit Breakdown 

  


Preface: "The right panes show totals and details for the highlighted deposit."

  


Columns: 

  * Deposit Date
  * Originating Fund
  * Client
  * Invoice # (link to open record) 
  * Invoice Date
  * Payment Date
  * Payment Check #
  * Payment Amount (total row displays sum) 



  


Grouped by: Deposit Date + Originating Fund + Current Agent

  


Sorted by: Invoice ID + Payment deposit date + Originating Fund + Current Agent

  


Filters: 

  * Current Agent (drop list of "In-State Agent"-Type Contacts and blank = all; with the following details: 
    * limiting the drop list items: 
      * for Admin users: includes all "In-State Agent"-Type Contacts (no limiting); 
      * for non-Admin users who are the "Checkbook Holder" for a Fund: includes the current user's Contact and all Agents who use their Fund; 
      * for all other non-Admin users: includes only the current user's Contact; 
    * defaults to the current user) 
  * Originating Fund (drop list of all Funds; defaults to blank = all)
  * Deposit Date Start (date; defaults to six months before the current date)
  * Deposit Date End (date; defaults to blank = all)



  


Top right pane: This pane displays the totals for each Sales Item for the last-selected deposit (Deposit Date + Fund + Current Agent) in the left pane.

Title: Deposits Total Helper Top Right Pane

  


Preface (in bold): Deposit Totals (<Deposit Date>, <Fund Name>, <Agent LastName, FirstName> \- <Agent Code>)

  


Columns:

  * Sales Items
  * Payment Amount (total row displays sum)



  


Grouped by: N/A 

  


Sorted by: Sales Item (alphabetical)

  


  


Bottom right pane: This pane displays a breakdown for the last-selected deposit in the left pane.

Title: Deposits Total Helper Bottom Right Pane

  


Preface: "Deposit Breakdown (<Deposit Date>, <Fund Name>, <Agent LastName, FirstName> \- <Agent Code>)"

  


Columns:

  * Sales Items
  * Invoice # (link to record)
  * Payment Amount (total row displays sum) 



  


Grouped by: Sales Item

  


Sorted by: Invoice # 

  


  


Other Notes:

  * Clicking the bold line for a deposit in the left pane will display the corresponding items for that deposit in the right panes. To allow this, this report is being changed to not allow this user to select multiple lines at a time.
  * The following data access limitations apply to the report itself (in addition to the limitations on the filter drop list):
    * Admin can view the report for all agents
    * Non-Admin checkbook holders can view the report for themselves and all of the Agents using their Fund.
    * Non-Admin, non-checkbook holder agents can only view the report for themselves.



  


Development Specification

Change Requests: 

  * Tim Reitz 06/11/2024: [[[IN9648](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9650&)]] - ZWA - Income Report & Deposit Breakdown Reports - Clarify Date Labels
  * Tim Reitz 08/23/2025: [[[IN12002](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12004&)]] - ZWA - Receive Payments / Prepare Deposit Report - Fix Filter Visibility


