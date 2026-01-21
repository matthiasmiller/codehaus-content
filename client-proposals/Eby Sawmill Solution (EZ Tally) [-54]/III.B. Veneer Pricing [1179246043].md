3.2. Veneer Pricing

  


Requirements

Initial Implementation: The original implementation of veneer pricing is a simple calculation: 

  


$/mbf = (Grade - 500) * 100

  


Example: A log with a Grade of 510 and containing 40 Net BF would have a value of $40.00, calculated as follows: "([510 - 500] * 100 * 40) / 1,000)".

  


Future Expansion: To allow for the future possibility of having a veneer base price plus an incremental amount, the Solution has System Switch settings for the following:

  * Veneer Base Price per mbf (required; number with no decimal places; default to 0)
  * Veneer Incremental Price per mbf (required; number with no decimal places; default to 100)



  


Note that these switches can only be modified by administrators.

  


Since veneer grades start at 500, the Solution would the following formula to calculate the price of a veneer grade:

  


$/mbf = Veneer Base Price + (Grade - 500) * Veneer Incremental Price

  


Development Specification

Change Requests: 

  * Tim Reitz 08/07/2024: [[[IN9541](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9543&)]] - ZET - Yard App - Yard Scaling - Average Price field: Veneer logs not being accounted for
  * 


  


  


Add Switches

Zero decimals for these switches. Validate that these are non-blank. 

Names are:

  * VeneerBasePricePerMbf
  * VeneerIncrementalPricePerMbf



Labels are above. 

User-changeable.

Note in description: "Used to calculate VeneerPriceMbfFromGrade."

  


Add Calc Macro

Add a VeneerPriceMbfFromGrade( vGrade) macro:

  * Assign Parameter vGrade = ValidatedListString(...);
  * Returns NA if not IsVeneerGrade (another parameterized macro). 
  * See formula above
  * Create an InternalVeneerPriceMbfFromGrade(vGrade, vBasePrice, vIncrementalPrice)
    * Add unit tests for:
      * 500, 0, 100
      * 599, 0, 100
      * 500, 200, 150
      * 599, 200, 150


