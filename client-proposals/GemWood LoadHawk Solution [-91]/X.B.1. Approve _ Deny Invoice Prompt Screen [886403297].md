10.2.1. Approve / Deny Invoice Prompt Screen

  


Requirements

This is a special prompt screen that is used to quickly mark a Delivery Ticket / Buyer Invoice as approved or denied. The same prompt screen is used for both the "approve" and "deny" actions, but the prompts are defaulted differently based on which link is selected. 

  


This may be opened from multiple places: 

  * The "Invoices Awaiting Approval" report (see the corresponding spec)
  * The "Salesperson Invoice Review Email" (see the corresponding spec) 



  


Note that the Salesperson needs to be logged into the Solution on whichever device he uses to receive the email and mark it as approved/denied.

  


It contains the following:

  


  * Approve / Deny Invoice (screen header; standard)
  * Approved? (required; drop list of "Yes" / "No"; defaults based on the link from which the screen was opened)
  * Ticket # (required; with the following details: 
    * drop list of Ticket #'s for Delivery Tickets with "Status" = "Awaiting Salesperson Approval" or "Salesperson Approval Denied"; 
    * defaults to the Delivery Ticket for which the prompt screen was opened from the report or the email; 
    * included to provide an easy visual reference for the user to confirm which invoice is being approved/denied; 
    * located to the right of the "Approved?" prompt) 
  * Approval Denied Comments (visible and required if "Approved?" = "No"; multi-line plain text field (approx. 4 lines, to allow for up to a few sentences); defaults to the current entry in the "Approval Denied Comments" field on the selected Delivery Ticket) 
  * Confirm (button; initiates the "Approve / Deny Invoice" automatic process - see corresponding spec; note that only users with the "Edit Delivery Tickets via import" Permission can successfully run this process)



  


Other Notes: 

  * N/A



  


Development Specification

Change Requests: 

  * Tim Reitz 10/04/2025: [[[IN11560](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11562&)]] - ZGW - Improve Approval / Denial Process
  * 


  


  


Mockup: N/A

  


Tim Reitz 12/04/2024: Note that this is a simple x30.

  


Ellis Miller 12/24/2024: NOTE: This will be coded in the "User-Initiated Processes" section.
