5.8.3. User-Initiated Processes

  


Requirements

User-Initiated Processes: The Solution contains the following automatic processes that are initiated by a user action:

  


1\. "Set / Update Buyer Grade $ on Delivery Ticket from Buyer Payment":

  * Overview: Sets/updates the "Buyer Grade $" field on a Delivery Ticket record.
  * Initiated:
    * By clicking the "Confirm" button on the "Set / Update" child screen on a Buyer Payment record.
  * Prompts: 
    * Delivery Ticket Internal ID (required; hidden, numeric, passed in automatically)
    * Buyer Grade $ (required; number; manually entered)
  * Action(s): 
    * Takes the selected "Delivery Ticket" record and the entered "Buyer Grade $" value. 
    * Edits the "Buyer Grade $" field on the currently-selected Delivery Ticket record
  * Command(s) for Scheduled Tasks:
    * N/A (not run via Scheduled Task)



  


  


2\. "Approve / Deny Invoice":

  * Overview: Sets Invoices to approved or denied, via links in the "Salesperson Invoice Review Email". 
  * Initiated:
    * By clicking the "Confirm" button on the "Approve / Deny Invoice Prompt Screen" (accessed from links in the email). 
  * Prompts (also see the separate spec for this prompt screen):
    * Delivery Ticket Internal ID (required; hidden; numeric, passed in automatically)
    * Approved? (required; "Yes" / "No" list; defaulted based on the link that is clicked)
    * Approval Denied Comments (visible and required if "Approved?" prompt is set to "No", text field, approx. 4 lines, to allow for up to a few sentences)
  * Action(s): 
    * Checks the "Invoice Approved" or "Invoice Approval Denied" checkbox for the corresponding Delivery Ticket record, based on the "Yes"/"No" answer to the "Approved?" prompt.
    *  Sets the "Approval Denied Comments" text field on the corresponding Delivery Ticket record, based on the entry in the corresponding prompt. 
  * Command(s) for Scheduled Tasks: 
    * N/A (not run via Scheduled Task)
  * Other Notes: 
    * Note that only users with the "Edit Delivery Tickets via import" Permission can successfully run this process.



  


Development Specification

TODO_CCI: Tim Reitz 01/09/2025: Please send me the details about the x30s once you have them done, so that I can document them more completely in the living spec. Thanks! 

  


  


  


Std Delivery Ticket Set Buyer Grade Price.x30

  * An x30 that has ask prompts for delivery ticket and $ and saves $ to specified delivery ticket



BID 2 hours

  


Std Invoice Set Approval.x30

  * as spec'ed above



BID 4 Hours
