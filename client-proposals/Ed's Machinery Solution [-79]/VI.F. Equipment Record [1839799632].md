6.6. Equipment Record

  


Requirements

This is a custom record type that the Solution will use to track the following information for the equipment:

  


  * General information:
    * AppHosting ID (number; auto-generated)
    * Stock Number (text with digits and hyphens; required; assigned from QuickBooks)
    * Lead (text; i.e. "2020 John Deere Combine")
    * Extended Description (text)
    * Photos
    * TractorHouse Link
  * Purchase:
    * Investor (checkbox or Yes/No)
    * Commission (checkbox or Yes/No)
    * Auction (checkbox or Yes/No)
    * Purchase Date
    * Purchase Price (coming off the QuickBooks bill)
  * Sale section:
    * Sold Date
    * Selling Price ($)
  * Costs section:
    * Advertising Days (#)
    * Advertising Rate ($; default to current Advertising Rate)
    * Detailing ($)
    * Freight ($)
    * Repairs; embedded spreadsheet of:
      * Hours (read-only; based on linked time cards)
      * Hours Rate (default to current Repair Rate)
      * Parts Costs
    * Misc ($)
    * Overhead Days (#)
    * Overhead Rate ($; default to current Overhead Rate)
    * Interest Rate (%)
    * Interest ($; auto-calculated from purchase price)



  


NOTE: Currently non-consignment stock numbers are assigned with a prefix indicating the investor. Consignment stock numbers are currently numbered 2-24, where 2 indicates the second consigner, and 24 indicates the 24th items. Ed's will move towards a new format that includes the auction year and month, such as 23-12-2-24, where "23-12" indicates the auction in December of 2023, and "2-24" has the same meaning as before.

  


Development Specification

TODO_IDD: Do they want to track these?

  * Serial #  \- TODO - necessary? Probably a keyword search?
  * VIN - TODO - necessary? Probably a keyword search?
  * Originating Buyer (which of the three?)
  * Seller
  * Buyer (person who ended up buying the equipment)



  


  


The Google Sheet includes:

  * Stock #
  * Make
  * Model
  * Hrs (number)
  * Investor (Y/N)
  * Commission (Y/N)
  * Auction (Y/N)
  * Purchase Date (date)
  * Purchase Price ($)
  * Sold Date (date)
  * Selling Price ($)
  * Detailing ($)
  * Freight ($)
  * Repairs ($)
  * Misc ($)
  * Overhead Days (#)
  * Overhead ($)
  * Advertising Days (#)
  * Advertising ($)
  * Interest Rate (%)
  * Interest ($)
  * Cost above Purchase ($)
  * Total Cost ($)
  * Profit ($)
  * Percent Gained (%)
  * Month
  * Year


