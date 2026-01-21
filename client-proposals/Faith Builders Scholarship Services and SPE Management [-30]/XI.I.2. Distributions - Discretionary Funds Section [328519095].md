11.9.2. Distributions - Discretionary Funds Section

Discretionary Funds section:

  * Table of:

  
| Pre-K| K-12| OSTC| Non-EITC| Total  
---|---|---|---|---|---  
Max. Discretionary Amount| expr| expr| expr| expr| expr  
# of Families| field| field| field| field| expr  
Application Fees| expr| expr| expr| expr| expr  
School Discretionary Portion| expr(editable)| expr(editable)| expr(editable)| expr(editable)| expr  
  
  


Validation:

  * Error: if # of Families is negative for any fund.
    * Error Message: "Number of Families cannot be negative for <Fund Name>."
  * Error: if School Discretionary Portion is negative for any fund.
    * Error Message: "School Discretionary Portion cannot be negative for <Fund Name>."
  * Warning on save: if All for Tuition is checked and School Discretionary Portion is not 0.00 for all funds.
    * Warning Message: "If the application is marked 'All for Tuition', the School Discretionary Portion should be 0.00 for <Fund Name>. (Field: DistDiscSchoolPortion<Fund Name>)"



  


Additional Notes:

  * If the school is PASS managed and is flagged for "All for Tuition", the discretionary fund only contains the application fees.
  * Application fees are taken from OSTC if any child is OSTC. Otherwise, they are taken from the respective EITC fund.
  * If Paperwork is School Managed, the # of Families row is blank.
  * In the table: 
    * Expressions (expr) are auto-calculated and non-editable unless otherwise noted. 
    * Fields and editable expressions are editable if Paperwork is PASS Managed and Check Date, Check Number, and Check Amount are all blank.


