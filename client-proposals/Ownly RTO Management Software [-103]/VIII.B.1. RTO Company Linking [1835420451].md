8.2.1. RTO Company Linking

Seth Miller 01/27/2026: _Seth: spec and delegate.

Niccolas Miller 02/03/2026: TODO_NM: [[PC0189380]]

  


TODO_SETH:

  * We need to meticulously go through and make sure that all Contact linking filters by RTO Company.
  * Add permission for "Allow Breaking RTO Company Linking" (deny all)
  * Add validation on records. Make sure that any linked contact records are the same RTO Company. WARNING with the above permission. Otherwise ERROR.



  


  * We want a Spider Web report (not on the menu) that takes a contract. I think it can be pretty slow but basically it should do a:
    * ListExpand(ValidatedListString(DatabaseLevels, "Contact") + Tab + String(ContractID), ...and then for each of these, it would do a ____Field and find all the related Level+RecordID pairs
      * Contract
        * Primary Customer
        * Secondary Customer
        * Asset
        * Payment
        * Invoices / Bills (do we have this yet?)
      * Asset
        * Manufacturer
        * Dealer
        * Salesperson
      * Contact
        * Dealer (if Salesperson)
        * Manufacturer (if Manufacturer)
      * Payment
        * Associated Linked Contracts
        * Associated Invoices / Bills
      * TODO_SETH - See if I left anything about
    * Columns:
      * Record Name
      * Record ID
    * Group By
      * RTO Company (either do another ___FIeld lookup, or put it into the RLI)
    * Button:
      * Use the same report we use for Record IDs to drill into that record.
    * TODO_SETH - Make sure I caught all the important links


