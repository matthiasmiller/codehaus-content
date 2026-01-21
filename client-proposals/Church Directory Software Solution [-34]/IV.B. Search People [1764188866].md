4.2. Search People

  


Requirements

The View Households should filter by:

  * First Name
  * Middle Name
  * Last/Maiden Name
  * Person #
  * Household #
  * Church #
  * Address (partial searching)
  * City
  * State (drop list)
  * Zip
  * Only show heads of households (checkbox)
  * Only show households needing followup (checkbox)



  


The report will only show people matching ALL conditions.

  


It should show columns for each of the prompts.

  


It should group by Active Households, then by Inactive Households.

  


Additional notes about partial searching: Each search term will be searched for separately and must be found in the address text. For example, if the address is "1378 S Cumberland Rd" then searching for "378" or "378 land" will return a match. Searching for "1378 S" will match because of the "S" in Street. Searching for "1378 Cumberland Road" will not match because "Road" is not in the search results.

  


Development Specification

Austin Priest 06/28/2023: [[[IN8115](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8117&)]] - ZPP - Directory - Adding "address" as a search option

  


  


  


Bid: 0.5 day.
