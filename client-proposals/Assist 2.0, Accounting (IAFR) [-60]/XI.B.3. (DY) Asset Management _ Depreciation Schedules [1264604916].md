11.2.3. (DY) Asset Management / Depreciation Schedules

  


Requirements

TODO_CCI: Pair programmed by CCI by end of August.

  


NOTE: InSight will only be using straight-line depreciation for their business. They plan to store assets in the accounting system, but only handle book value in Assist. They will handle tax value separately. They will export the asset list for their tax accounting as needed.

  


Asset Class Record:

  * Name (text; required)
  * Useful Life (in years; number; 0 decimals)



  


Asset Record:

  * Asset ID (text; required; usually serial number, could be something else)
  * Name (text; required)
  * Value section:
    * Purchases; read-only embedded spreadsheet of transactions linked to the asset and associated with an Asset-type financial account (with link to add New Purchase, visible if not in service) of:
      * Date
      * Account
      * Amount
      * Undo Purchase (link visible if not in service; used to expense out a purchase)
    * Cost (number; 2 decimals; automatic and read-only)
    * Date Put in Service (date; required)
    * Salvage Value (number; 2 decimals; optional)
  * Accounting section; embedded spreadsheet of:
    * % (default to 100 minus already-entered percentage allocations; validate that all rows add up to 100)
    * Depreciation Expense Account (list of expense GL accounts; required)
  * Depreciation section:
    * Asset Class (used to determine the useful life of the product; editable; warn if changing after purchase, "Changing the asset class will change the depreciation value. Impairment losses must be entered manually.")
    * Useful Life in Years (automatic and read-only)
    * Start of Useful Life (automatic and read-only; the 1st of the month on or after Date Put in Service)
    * End of Useful Life (automatic and read-only; calculated from Start of Useful Life and Useful Life in Years)
    * Depreciation Expense per Month (number; 2 decimals; calculated based on Current Value minus Salvage Value, divided by Remaining Useful Life in Months; the Remaining Useful Life should exclude any months with a depreciation amount to avoid double-depreciating during a month)
    * Sold or Abandoned On (date; editable if a Date Put in Service is specified; warn if the asset accounts are not zero as of this date, based on accounting transactions)
    * New Transaction for Sale / Abandonment / Impairment Loss (link to a New Transaction record with default entries to zero out of any asset accounts for this asset, as well as a line entry without any assigned account and a corresponding debit for the total value of the asset. The amount of the impairment loss must be adjusted.)
  * Linked Transactions (link to report of all transactions linked to this asset)



  


Report:

  * Depreciation Report
    * Column
      * Date (as-of date)
      * Asset ID
      * Asset Name
      * Account
      * Amount (i.e. monthly depreciation amount)
    * Prompt For:
      * As Of Date (default to Today)
    * Notes
      * The "Date" defaults to the start of the month of the "As Of Date".
      * The monthly depreciation would decrease if the value decreases or useful life increases. If the value increases, add an impairment loss. This ensures that the depreciation amount stays in sync with the asset left and asset value, this prevents the any unintended side effects such as depreciating below the salvage value.
      * This will need to have multiple rows for multiple accounts, based on the embedded spreadsheet % / account breakdown on the asset.



  


Automatic Process:

  * Create transactions based on the Asset Depreciation report. Run this automatically soon after midnight on the first day of the month. This would create one transaction per asset.



  


Notes:

  * To enter in existing assets:
    * Enter a journal entry to transfer from equity to asset for the full asset value, dated before the asset is put into service (usually the purchase date)
    * Enter a journal entry to adjust the asset value for depreciation, dated on the day before the start date 
  * Because the depreciation amount is calculated based on the current value and the remaining useful life, decreasing the asset's value will decrease depreciation. As far as the software is concerned, increasing the asset's value will simply increase depreciation. However, this is unlikely to be intended from an accounting perspective. Instead, the accounting team should most likely create a new asset or expense out the changes.
  * The accounting team will be responsible for fleshing out the details of the Sale / Abandonment (assigning debit to the bank asset account, as well as "Gain on Sale of Asset" and "Loss on Sale of Asset" accounts).
  * Assist will not manage any calculations around impairment loss. These must be manually calculated by the InSight accounting team and entered manually.



  


Report Alert:

  * Create a report alert for all transactions that are tied out to a fixed asset GL account but do not have an asset specified (only visible if you have permission to edit accounting).



  


TODO_MM - Matthias Miller 09/05/2023: Note for Mark - that accounting will have to chase this down separately, and asset won't be showing up on the Vendor Invoice verification reports.

  


Accounting Transaction:

  * Line Item - Asset ID (used to link to an asset)
  * Warn when assigning to an account for a fixed asset but without assigning an asset ID.
  * Warn when creating a purchase for an asset already in service. Warn that it will increase depreciation, and that the user should consider an impairment loss or expensing the item immediately if this is not intended.
  * Warn when modifying a transaction that is linked to an asset ID, "Editing a transaction that's linked to an asset may adjust the asset value and depreciation.".
  * Warn when creating a transaction dated after the assets sold / abandoned date.



  


Implementation:

  * InSight will use multiple accounts for assets, one account for Gain, and one account for Loss. For example:
    * NON-CURRENT ASSETS
      * 1500 PROPERTY, PLANT and EQUIPMENT
        * Buildings and Building Improvements
        * Production Equipment and Fixtures
        * Property Improvements
        * Rolling Stock
    * One GL Account for Gain on Sale of Asset, listed as Miscellaneous Income underneath EBT line.
    * One GL Account for Loss on Sale of Asset, listed as Miscellaneous Expense underneath EBT line.
    * One GL Account for Asset Impairment Loss.



  


Development Specification

TODO_JI - End of period - the Depreciation Expense needs to be zeroed out into Accumulated Depreciation

  


Joel Iwashige 08/09/2023: Do I need to do something to formalize a link of this with "[[PC0157618]] - ZFP - Asset management and depreciation"?
