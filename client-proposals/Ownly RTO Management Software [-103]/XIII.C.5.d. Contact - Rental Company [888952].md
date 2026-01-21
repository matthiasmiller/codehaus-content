13.3.5.4. Contact - Rental Company

Accessed via: Settings | Configuration | Configure Rental Companies

  


Custom Section that is only visible for Rental Company-type Contact Records.

  


Fields:

  * Short Code (text; required)
  * Damage Waiver Abbreviation (list of Damage Waiver Abbreviations; required) 
  * Term Months (RG of a single number field: "# Months")
    * Warning on save if there are no Term Months specified: "No Term Months are specified."
    * Warning on save if the Term Months are not divisible by 12: "Rental term length is not divisible by 12."
    * Error on save if there is a Contract Definition for the Rental Company that offers a Term that is NOT in the Term Months RG: "The following Term Months are specified on Contract Definitions for this Rental Company: <Term Months>"



  


  * Due Date Method (list; required)
    * Fixed
    * Floating
  * Monthly Fixed Day of Month (number, 1-31; visible for Fixed)
  * Semimonthly Fixed Day of Month (number, 1-31; visible for Fixed)
  * Weekly/Biweekly Fixed Day of Week (list of weekdays; visible for Fixed)
  * Late Fee Duplicate Prevention (list; required; visible for Floating)
    * When Fee Assessed
    * When Payment Due
    * In the field description say, "This setting prevents more than one fee being assessed for the calendar month/week/2-week period based on either the date the fee was assessed or the payment was due."



  


  * Depreciation Schedules section (custom)
    * RG
      * Columns
        * Method (drop-list of Depreciation Methods; required)
        * Useful Life (drop-list of Fixed Length, Contract Length; required; Contract Length is only available for Straight Line depreciation)
        * Length (Years) (only editable and required if Useful Life is "Fixed Length")
      * Buttons to add/remove rows: "✚" / "🞭"
      * Validate that there is at least 1 Book depreciation method



  


NOTE:

  * If a state limits the convenience fee by 1%, you cannot charge more than $10 for a $1000 payment. Thus, the total payment would be $1010.



  


Other Notes: 

  * Unless otherwise noted, all fields default to blank and all checkboxes default to not checked.



  


Matthias Miller 07/30/2025: TODO_PERMISSIONS:

  * Who can create/edit Rental Companies?
    * Administrator-level permission


