17.8. QuickBooks Integration

Integration between Silverloom and QuickBooks will be set up. 

  


The process looks something like the following: 

  


  * Sync Process
    * Export Customers from QuickBooks
    * Import Customers into QuickBooks matching on:
      * QuickBooks Account Number (if possible)
      * Silverloom Account Number (if possible)
      * Customer Name (if possible)
      * (otherwise, new record)
      * NOTE: Delete unmatched records.
    * Export all QuickBooks customers from Silverloom that have a blank account number
    * Import those customers into QuickBooks, matching on name, thus setting the account number in QuickBooks
    * Rerun the Export Customers from QuickBooks / Import Customers into QuickBooks process
    * Export the time data



  


Various reports are needed to facilitate this sync.

  


  


Matthias Miller 12/04/2025: No longer needed
