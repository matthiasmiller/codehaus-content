5.5. Invoice Record

  


Requirements

Overview: The Solution uses the standard Silverloom Invoices module to invoice fees and refunds for clients, and to track payments applied to the Invoices.

 

Accessed via: 

  * "View Invoices" report (see corresponding spec) 
  * Home | Invoices | New Invoice (opens a new Draft invoice record, with "Invoice Date" set to the current date) 



  


Sections and Fields: See the following sub-sections of this living spec. 

  


Modification History: This contains the following standard feature(s) for modification tracking: 

  * Modification History (link to open the report for the record)



  


Data Access: 

  * View: A client's agent, the Checkbook Holder for the agent's fund, and all admins. 
  * Edit: A client's agent and all admins. 



_CCI1: Tim Reitz 08/18/2025: Could you confirm / clarify the visibility and editability conditions here? 

I was thinking that "client's agent" means "client's current agent", but I realize that it could mean "client's agent at the time that the invoice was created" \-- which is the current behavior? Thanks!

Murshid Rahman 09/03/2025: The users who have "View Invoices" permission, should be able to view invoices. On the other hand, all admins and invoice contact's current agent should be able to edit invoices. Its not "client's agent at the time that the invoice was created".

TODO_VA: Tim Reitz 09/15/2025: Follow up. 

Other Notes:

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Development Specification

TODO_VA: Tim Reitz 08/26/2025: Add in the notes for data access, special considerations, etc., once those are resolved in the Invoice Snippet.  

  


  


Invoices (5 days)

Line Items:

 \- Date

 \- Vehicle ID as a custom field

 \- Sales Items (Investortools-owned): 

 \- Liability Premium

 \- Collision Entry Fee

 \- Collision Premium

 \- Cargo Entry Fee

 \- Cargo Premium

 \- High Risk Driver Fee

  \- Description \- may not be used much

  \- Amount

  


The invoices won't be printed with a normal invoice template. It looks like an invoice, but it's actually a statement that reports on all unpaid invoices. 

  


Invoice Template

TODO: This needs more spec'ing. 

We'll need to match this pretty closely because the bottom is perforated and the top is likely folded to display in an envelope window. Request an exact PDF. If there are more than X lines (the # that fit on that section), just show text instead of the table:

See attached details.

We will then include a second page with the table for the entire second page. Delete the second page if everything will fit.
