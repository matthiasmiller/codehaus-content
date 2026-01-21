3.2.2.4. FGI Financial Allocations

  


Requirements

The financial allocation record determines which funds get put into which account and is the bridge between FGI and accounting.

  


The financial allocation will be a specific record that specifies:

  * Effective Date (date; required)
  * District (district; list of districts)
  * Accounting Company (required; list of companies)
  * Subset (building-level expression)
  * FGI Accounts section; embedded spreadsheet of:
    * FGI Cost Category (required; list of FGI Cost Categories)
    * FGI Source Account (required; list of general ledger accounts)
    * FGI Destination Account (required; list of general ledger accounts)
    * COGS Expense Account (required; list of general ledger accounts)
    * COGS Variance Account (required; list of general ledger accounts)
  * Sales Order section:
    * Accounts Receivable Account (list of accounts)
    * Unearned Income Account (list of accounts)
    * Payments; embedded spreadsheet of:
      * Payment Type (list of Payment Types on sales order)
      * Payment Account (list of accounts)
      * Payment Fee Account (list of accounts)
    * Sales Tax Account (list of accounts)
    * Shipping Income Account (list of accounts)
    * Income Account; embedded spreadsheet of:
      * Account (list of accounts; required)
      * Subset (building-level subset expression)
    * Accessories; embedded spreadsheet of:
      * Search Term (string; required)
      * Account (required; list of accounts)
    * Discounts Account (list of accounts)



  


NOTE:

  * The internal record name will be "OH-2022-12-01" for an Ohio financial allocation effective on December 1, 2022.
  * Validate against multiple rows for the same Payment Type
  * Validate against multiple rows for the same FGI Cost Category



  


Permissions:

  * This should be controlled by an "Configure FGI Costs" permission



  


NOTE:

  * The FGI Cost Allocation can be edited at any time. Any sold (i.e. delivered) sheds will remain unmodified.
  * EBMS has the concept of "departments", which allow specifying general ledger account numbers that can collapse into the parent category. This is currently controlled using the "Depth" on the balance sheet report.



  


Development Specification

DONE_CCI: Under the hood, we'll have this be a lookup record named NC-2020-10-22, which will prevent duplicate entries for the same district + day

  


[ ] Simple lookup record.

[ ] Record name is District + Effective Date (NC-2020-12-22).

  


Niccolas Miller 04/25/2023: [[PC0153364]] - ZFP - FGI: Create FGI Financial Allocations Lookup Record (T&M)
