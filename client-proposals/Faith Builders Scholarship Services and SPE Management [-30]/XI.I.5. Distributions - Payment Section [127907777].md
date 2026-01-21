11.9.5. Distributions - Payment Section

Payment section:

  * Table of:

  
| Pre-K| K-12| OSTC| Non-EITC| Total  
---|---|---|---|---|---  
School Discretionary Portion|   
|   
|   
|   
|   
  
School Scholarship Portion|   
|   
|   
|   
|   
  
School Check|   
|   
|   
|   
|   
  
FBSS Application Fees|   
|   
|   
|   
|   
  
Ending Balance|   
|   
|   
|   
|   
  
  
  


TODO_DOC: TODO_BR/TODO_TR/TODO_VA/TODO_NM: Niccolas Miller 08/15/2025:

  * Now checks RG instead of non-RG fields.
  * Document cached fields for Fund Discretionary Portion (set when check is Finalized; if one check, School Discretionary Portion for fund; if more than one check, School Discretionary Portion for fund - prior check amounts):
    * DistCheckDiscSchoolPreKPortion
    * DistCheckDiscSchoolK12Portion
    * DistCheckDiscSchoolOSTCPortion
    * DistCheckDiscSchoolNonEITCPortion



  


  * Check Date (date; editable if all of the Family Applications represented in the Families embedded spreadsheet have the "Requires Documentation" checkbox not checked)
  * Check Number (number; no decimals; editable if all of the Family Applications represented in the Families embedded spreadsheet have the "Requires Documentation" checkbox not checked)
  * Check Amount (number; two decimals; editable if all of the Family Applications represented in the Families embedded spreadsheet have the "Requires Documentation" checkbox not checked)



  


Validate:

  * Error: if Check Amount is not equal to all funds for the school.



  


Additional Notes:

  * All cells in the table are uneditable expressions.


