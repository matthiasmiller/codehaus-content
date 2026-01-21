16.2.2. Syncing Sales Tax Codes

Configure Sales Tax Rates mentions syncing...

  * Sales tax is pulled from QB into the software. They set up the tax in QB.



  


TODO_CH

  


  * Sales tax can populate from QB into the database



Make a difference

  * Update
  * Refresh
  * Populating (takes all the information from QB, and rewrites it into the database)


  * Sometimes QB does not round/figure the tax the same way as their current software
    * 238.05 in the database
    * 238.0? in the QB
  * They use penny balances, because of the state/county/city combinations
  * Take the State Rate, and add that to the invoice, and the county rate, add that to the invoice, and the city rate, add that to the invoice -- comes out one way
    * QB Has a Sales Tax Group that has individual items with specific % items


