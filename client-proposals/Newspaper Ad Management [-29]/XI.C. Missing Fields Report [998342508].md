11.3. Missing Fields Report

  


Requirements

The Missing Fields Report defaults to the current publication date and shows any "required" (warn on Save) fields that have been left blank in any ads in the selected publication date.

  


It should include the following columns:

  * Publication Date
  * Customer (link to Customer/Ads Page)
  * Primary Contact Name
  * Ad Title
  * Missing Fields (bulleted list of missing required fields for the ad)
    * Includes
      * Ad Size
      * Ad Color
      * Ad Image
      * Special Placement Page Number
      * Special Placement Page Location
  * Publication (only for Full Admins)



  


Filters:

  * Customer
  * Publication Date (default to current; blank = all)
  * Missing Fields (multi-select list of all Ad Sizes; default to blank = all; selecting one or more specific fields would reduce the results to only ads lacking the selected field(s), but would still show all missing fields for the displayed ads)
  * Publication (only for Full Admins; list of publications; default to blank = all)



  


Grouping/Sorting: 

  * Group by Publication Date if all; no grouping if only one Publication Date is selected
  * Sort by Customer, then by Ad Title



  


Development Specification

Tim Reitz 01/07/2021: Keep this as basic as we can.
