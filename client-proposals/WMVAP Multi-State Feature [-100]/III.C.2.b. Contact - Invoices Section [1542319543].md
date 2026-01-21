3.3.2.2. Contact - Invoices Section

  


Requirements

*Documented. Tim Reitz 08/19/2025

  


Make the following changes (full spec included here, with changes noted with blue and strike-through): 

  


Invoices section (standard section, with customizations; visible for all Contact Types; visible to the Client's agent, the Checkbook Holder for the agent's fund, and all admins): 

  


  * Invoices (standard; no label; read-only embedded spreadsheet with the following:
    * Columns: 
      * Invoice #
      * Date
      * Status
      * Amount
      * View (link to the Invoice record)
  * Total Uninvoiced Fees (custom; read-only macro; number; 2 decimals; displays the total uninvoiced fees for the client, and the total of all Contact Fees, including ones that are to be assigned in the future)
  * Total Refunds (custom; read-only macro; number; 2 decimals; displays the total uninvoiced refunds for the client)
  * Total Credits (custom; read-only macro; number; 2 decimals; displays the total available credit for the client)
  * Create Invoice for Fees & Refunds (custom; button; creates invoices for uninvoiced Vehicle-related Fees & Refunds, and uninvoiced High-Risk Driver Fees with "Effective Date" on or before the current date; prompts the user to save the record before opening) 



  


  * This client has <#> unpaid invoice(s) (custom; read-only message; visible if the contact has unpaid invoices)
  * View Unpaid Invoices (custom; report link; visible if the contact has unpaid invoices; prompts the user to save the record before opening; opens the "Unpaid Invoices for Contact" report) 
  * Print Statement (custom; link; opens the Statement printout PDF for the client; visible if the contact has unpaid invoices; prompts the user to save the record before opening)
  * View All Invoices (standard; link; opens the "Invoices for Contact" report for the current client)
  * Create Blank Invoice (standard; creates an invoice for the current client)



  


Other Notes:

  * Note that the standard Silverloom "Statement" link is hidden, replaced by the custom "Print Statement" link, since the Solution uses a customized statement template.



  


Other miscellaneous background changes also are being made to improve the use and function of the Solution.

  


Development Specification

Tim Reitz 04/30/2025: Gray text might not be current - there are multiple CRs making changes to this section of the Contact record, so let's update the living spec directly rather than depending on this proposal for the correct spec for the gray content. 

  


Ellis Miller 09/05/2024: 

  


4 Hours, mostly a bit of cleanup

[ ] Rename "ContactInvoicesSectionIsVisible" to "CustomContact_InvoicesSectionIsVisible".

[ ] Instead of overriding the InsertInvoiceStatementInContact section, let's simply add a CustomContact_ShowStatementLink macro that returns true by default and is overridden in Weaverland to return false.

[ ] Since Weaverland doesn't use "Std Customer Statement.r21", let's override it with a template that simply says "This template is intentionally blank for this system. Use the Unpaid Invoices Template instead."
