15.2.2. Classic Accounting Invoice (Read-Only)

  


Requirements

Overview: This is a hidden record type that mirrors the invoices in Classic Accounting and is used for syncing between the two programs.

  


Note that this is a separate record from the auto-created Invoices for Managed Service Agreements and other sales created in the Solution. This will be used to track invoices for supplies, profitability reporting, etc.

  


Accessed via: The Classic Accounting Invoices report (see corresponding section of this proposal)

  


Sections and Fields: 

  * Classic Accounting Reference Number (= AHZ Invoice #?) 
  * Customer Org ID



DONE_JM - Does Classic Accounting have separate records for organizations and contacts?

TODO_CH: Currently CA strictly pulls from the Contact record. Should we do the same, using the contact Org ID? 

TODO_TR: update here accordingly: 

  * Invoice Date 
  * Invoice Number 



TODO_JM: what are the fields for date and number? 

  * Ship To TX (= shipping address)
  * Line Items (embedded spreadsheet with the following:) 
    * Columns: 
      * Quantity
      * Item ID (unique identifier rather than sales item number; but we would want to include the sales item # in AHZ) 
      * MemoTX (= item description) 
      * Amount  ($) 
      * Entry Total (= line total $) 
      * OrderSeq (= line item sequence) 
    * Sorting: N/A



  


Data Access: 

  * Admin-only viewing of records
  * Certain aspects will be visible to other users (such as sales items in customer history) 



TODO_JM: which users? (see note below)

TODO_TR: We could have this be permission-based, and have one called "View Classic Accounting Data" and a sub-permission (if necessary) called "View Classic Accounting Financials". Let's go as simple as we can though (1. admin only if it makes sense, 2. one permission if we can, or 3. split out permissions)

  


Other Notes:

  * The following are listed as line items in Classic Accounting, and should be brought over as such (using __): 
    * Tax
    * Discounts
    * Shipping



TODO_JM: do they have their own Item IDs? 

  * The Solution will not pull across customer addresses on the invoices synced from Classic Accounting. 



  


NOTE: It's possible that this could be imported directly onto a standard Invoice instead. This will be determined as part of the in-depth design.

DONE_CH: Would we use a custom record if we don't use the standard Invoices? 

What will determine which route we take?

DONE_TR: Whether we need to use standard invoices probably depends on things like...

  * Do we need to print these? We need to take a look, but I'd expect it'd be substantially cheaper to have shared templates in this case
    * Tim Reitz 04/20/2022: Per the client today: No, not printing them at this point.
  * Do these need to be included in the standard Sales reports?
    * Tim Reitz 04/20/2022: Yes, we would want them to be included in Sales reports, but would it be better to use the standard ones or do custom ones?
  * Tim Reitz 04/20/2022: Also, presumably we would want the CA invoices to appear on the Invoices reports with the AHZ invoices to give more complete reporting (especially Invoices by Customer). 



TODO_CH: See responses above from 4/20.

  


  


DONE_JM: What fields need to be brought in from Classic Accounting?

TODO_TR: Make sure all needed fields are accounted for in the Solution.

  


TODO_JM: copy of CA invoice

Tim Reitz 04/20/2022: Emailing today.

  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1533495013](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=1533495013)

TODO_CH: auto-generated detail screens for this like Sales Items? 

  


CCI: See note about using standard Invoices.

  


Lookup Records:

  * 3 fields
  * 1 RG
  * 2 restrictions + permission



  


Report

  


HL Est: 12 hours
