13.3.3.4. Sales Tax

We are doing a manual implementation of sales tax for the first cut (i.e. not linking with taxjar).

  


Sales Tax fields

  * State (required; string)
  * State Rate (required; number with 5 decimals)
  * County (required; string)
  * County Rate (required; number with 5 decimals)
  * City (required; string)
  * City Rate (required; number with 5 decimals)
  * Other (optional; string)
  * Other Rate (required if other is filled in; number with 5 decimals)



  


Events RG:

Tax rates are cached on incurred rows. Tax amounts are auto calculated for incurred rows, but cached for payment rows. 

  


Sales Liability RG (this is a cached RG of sales tax liabilities that is updated via a daily scheduled task)

  * Effective Date (required; date)
  * Liability Type (required; list with options of "Incurred" and "Paid")
  * State (required; string)
  * State Rate (required; number with 5 decimals)
  * County (required; string)
  * County Rate (required; number with 5 decimals)
  * City (required; string)
  * City Rate (required; number with 5 decimals)
  * Other (optional; string)
  * Other Rate (required if other is filled in; number with 5 decimals)
  * Taxable Subtotal Adjustment (required; number, 2 decimals)
  * Nontaxable Subtotal Adjustment (required; number, 2 decimals)
  * Tax Amount (required; number, 2 decimals)


