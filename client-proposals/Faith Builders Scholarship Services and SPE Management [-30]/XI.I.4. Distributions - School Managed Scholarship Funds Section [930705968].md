11.9.4. Distributions - School Managed Scholarship Funds Section

  


Requirements

School Managed Scholarship Funds section  (visible only for Distributions with the "Legacy School-managed Distribution" checkbox checked):

  * Embedded spreadsheet (RG):



Columns:

  * Family (plain text)
  * Household Income (number; no decimals)
  * Household Size (number; no decimals)
  * County (drop-list of PA counties)
  * Pre-K # (number; no decimals)
  * Pre-K $ (number; no decimals)
  * K-8 # (number; no decimals)
  * K-8 $ (number; no decimals)
  * 9-12 # (number; no decimals)
  * 9-12 $ (number; no decimals)
  * EITC Award $ (read-only; sum of previous $ fields)
  * OSTC K-8 # (number; no decimals)
  * OSTC K-8 $ (number; no decimals)
  * OSTC 9-12 # (number; no decimals)
  * OSTC 9-12 $ (number; no decimals)
  * OSTC Award $ (read-only; sum of OSTC $ fields)
  * Non-EITC # (number; no decimals)
  * Non-EITC $ (number; no decimals)



Buttons:

  * "+" \- insert row
  * "-" \- delete selected row



  


Validation:

  * Error on change: if duplicate families are entered.
    * Error Message: "Duplicate families are not allowed."
  * Warning on save: if the dollar column is blank and number of students column is not zero for any fund.
    * Warning Message: "<Column Name> cannot be blank if <Column Name> is not zero. (Field: <Column Name>; Row: <Row Name>)"



  


Additional Notes:

  * N/A



  


Development Specification

TODO_NM: "School-Managed Scholarship Funds" label, School Managed should not be hyphenated.
