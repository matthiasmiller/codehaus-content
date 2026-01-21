2.3. Solution 3 - Raspberry Pi to Sync Tax Rates with CA

In short, this solution would allow a Raspberry Pi running on their network to connect out to download the latest tax rate.

  


  * Option 1. Name the tax codes appropriately in CA in a way that salespeople can find the correct one. For example, it might be Zip Code + County. The Raspberry Pi would have a daily process to look up the tax rates and apply them correctly.



  


  * Option 2. In addition to #1, the Raspberry Pi would geocode the Customer addresses and associate the appropriate rate to the Contact. (This assumes that Classic Accounting has a way to associate a tax rate to a Customer.)



  


  * Option 3. In addition to #1, the Raspberry Pi would watch for new invoices. If a new invoice gets created, it would look up the tax code for the shipping address, and it would apply that tax to the invoice.



  


Pros:

  


  * Low cost; high return on effort



  


Cons:

  


  * Only solves the sales tax issue and does not allow for expansion.



  


Estimated Cost:

  


  * Initial Investment - $5k-10k
  * Maintenance - Time and Materials on an as-needed basis


