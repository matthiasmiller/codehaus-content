12.15. Sales Tax

Seth Miller 01/06/2026: Design has changed some and will require filtering through the details below as some is out of date

  


TODO_SETH:

  


Validating Addresses

  * Do not allow more than 1 physical location
  * Sort physical locations to the top
  * On the MRG, show:
    * Green - Verified
    * Gray - Pending Verification
    * Red - Invalid (with ... to view error message)
  * Use hidden RG fields:
    * Field change expression that changes to "pending verification" if you modify a physical address
    * Use a hidden "Address Verification" list (?) and ping when it's Pending Verification.
  * Need to require physical addresses on the dealers (warn on change that changing it will impact tax)



  


TODO_JOSH:

[ ] Seth will give you a field to watch for pinging & an x30 to call w/ results (figure out w/ Josh how to get errors)

  


TODO_IDD:

  * Options to Reduce Pings:
    * Group based on Jurisdiction + Rates
    * Ping one sample address
    * Re-ping the entire group
  * Option 1 - Manual Ping - Be able to search by certain factors and manually re-ping



  


  


  


  


TODO_SETH - Delegate 

  


  


Sales Tax rate is calculated when fees are incurred.

Sales Tax is paid when cash is collected.

  


  * WSGI
    * configuration
      * TaxJar API Key / etc
      * database trigger
      * respect rate limiter status codes + headers; monthly sync will likely trigger this



  


  * Lists
    * Sales Tax Filing Frequency
      * Monthly
      * Quarterly
      * Semiannually
  * Contacts
    * Type
      * Sales Tax Vendor
    * Fields
      * Sales Tax Filing Frequency
      * Filing Period Start Month (mirror / refactor Assist logic)



  


  


Seth Miller 10/22/2025:

TODO_IDD:

  * How does it work when we need to correct the sales tax liability info on an event row?


  * Matthias Miller 10/22/2025: i.e. change jurisdiction? I think we just change it and it gets corrected on the next liability payment?? If there are other issues, Duane will manually edit the RG for customers until he gets tired of doing it.


  * Do we need to look at the building address instead of the customer address?


  * We need the dealership + building address.



  


TODO_Seth: the following sections needs to be specced yet:

  * Contract Record
    * Button for "Update Rate from TaxJar" (updates Contract)
    * Events RG
      * Add fields for
        * Combined Rate (State Rate + County Rate + City Rate + Other Rate)
        * State
        * State Rate
        * County
        * County Rate
        * City
        * City Rate
        * Other
        * Other Rate
      * Add Expr for Combined Rate before all of these...
      * Link "View Sales Tax Liabilities" based on Contract ID, with basic event row information (Event Type, ADjustment Type, Event Date, Amount?) --- TBD something simple but gives access
      * Autopopulate based on any cached rates in the current month (prefer the one <= the incurred date; otherwise, get the earliest one > the incurred date)
      * Validate against incurring events if no available (current month) sales tax rate exists on contact record. In that case you need to ping
    * Require dealership on contracts - TODO_NM: Make sure it's required on prod, not here
    * Under the Primary & Secondary Customer:
      * Add Street, City. State, Zip fields to the location for the building
      * Add a button called "Copy from Customer" (visible if they have a single row with a blank address type or a Physical row)
    * Update rate from TaxJar (checkbox; TEMP: modify field change expr that adds row to ContactSTHist RG, set source and destination, fakes rates 5%-7% total broken down)
      * Automatically checked when any address field changes
    * Read-only RG of tax rates: ContractSTHist...
      * Effective Date (required; defaults to today)
      * Source (Dealer Address)
        * Street (required; simple string field)
        * City (required; simple string field)
        * State (required; list of States)
        * Zip (required; simple number field)
      * Destination (Address from contract)
        * Street (required; simple string field)
        * City (required; simple string field)
        * State (required; list of States)
        * Zip (required; simple number field)
      * Output
        * Error (simple string field)
        * State (required; list of states)
        * State Rate (required; number with 5 decimals)
        * County (required; simple string field)
        * County Rate (required; number with 5 decimals)
        * City (required; simple string field)
        * City Rate (required; number with 5 decimals)
        * Other (simple string field)
        * Other Rate (required if Other is specified; number with 5 decimals)
      * Show note on the main screen if the address is invalid. Create a note and assign it to the person who added/changed the address
  * Daily x30 to ping all active contracts if they do not have a cached effective date in the current calendar month



  


  


  


  * Bill
    * Sales Tax Liability (paid based on cash collected)
      * Contract ID
      * Contract Event ID
      * State
      * State Rate
      * County
      * County Rate
      * City
      * City Rate
      * Other
      * Other Rate
      * Nontaxable Subtotal Adjustment
      * Taxable Subtotal Adjustment
      * Tax Amount (expression)
    * TaxJar CSV Export (flat file export of some kind)
      * TODO_DB 
    * Allow rerunning the preview report to export as PDF



  


  * Process
    * Preview Sales Tax Liability (select vendor + period)
    * Create Bill (x30)
    * On the Bill...
      * Let's not make this technically too complicated, but can we use the same report to Preview Changes (looks at difference between database + this) w an option to apply? -- maybe pair program Matthias & Seth


