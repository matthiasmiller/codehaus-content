11.9.1. Distributions - Distribution Summary Section

Distribution Summary section:

  * School (drop-list of active school contacts)
  * Year (number)
  * The following label is displayed in red text if one or more Family Applications represented in the Families embedded spreadsheet has the "Requires Documentation" checkbox checked: "One or more Family Applications are lacking income details - see below." 
    * Probably located to the right of Year. 
  * Date Entered (date; required; defaults to the current date)
  * Paperwork (drop-list)
    * List items:
      * "School Managed"
      * "PASS Managed"
  * Legacy School-Managed (checkbox; auto-set and read-only; visible and checked if "Paperwork = "School Managed" and the "Year" is "2024" or prior)
  * All For Tuition (read-only; checkbox; lookup from the school application that matches on School and Year)
  * Fix Paperwork (button; visible if Paperwork does not match Paperwork on the matching school application)
    * When clicked, sets Paperwork to the value from the matching school application)
    * A red warning label is displayed next to the Fix Paperwork button as long as the button is visible.
  * Fix Students (button; visible if the number of students does not match the number of students on family applications for the school and year, and no check information is entered)
    * When clicked; fills the scholarship funds RG with a row for each student.
    * A red warning label is displayed next to the button as long as the button is visible.
  * Table of:

  
| Pre-K| K-12| OSTC| Non-EITC| Total  
---|---|---|---|---|---  
Starting Balance| expr| expr| expr| expr| expr  
Minimum Distribution| expr| expr| expr| expr| expr  
Funds to Allocate| field| field| field| field| expr  
  
  


  


Validation:

  * Error: if the school is the scholarship organization and Paperwork is not blank.



_TR Austin Priest 10/10/2024: I don't understand what this point means?

TODO_NM: Tim Reitz 02/24/2025: Could you take a look at this? Similar to the question in another section about a school being a scholarship organization. 

  * Error: if Year is not a valid year.
    * Error Message: "Please enter a valid year."
  * Warning on save: if the sum of Pre-K, K-12, OSTC, and Non-EITC funds distributed is less than the funds balance from previous contributions for the Pre-K, K-12, or OSTC fund.
    * Warning Message: "The <Fund Name> fund has <remaining amount> remaining from prior year contributions, but this distribution is only using <used amount>."
  * Warning on save: if All for Tuition is checked and any School Discretionary Portion funds are entered for any of the funds.
    * Warning Message: "If the application is marked 'All for Tuition', the School Discretionary Portion should be 0.00 for <Fund Name>. (Field: DistDiscSchoolPortion<Fund Name>)"
  * Warning on save: if the sum of any fund column in the Scholarship Funds RG is not equal to the Funds to Allocate number for that fund column in the table.
    * Warning Message: "Scholarship to Allocate for <Fund Name> should be equal to sum of <Fund Name> amount(s) in <Paperwork Type> Scholarship Funds.
  * Warning on save: if Total for # of Families is not equal to the number of families in the Scholarship Funds RG.
    * Warning Message: "The number of families who were awarded scholarship does not match the number of families receiving funds."
  * Warning on save: if Check Amount is not blank or the distribution is PASS Managed and Print Award Review Form Today is checked, and School Discretionary Portion for any fund exceeds the maximum discretionary amount for that fund.
    * Warning Message: "The <Fund Name> discretionary amount is <Total Amount>, but it should not exceed <Max Discretionary Amount>"
  * Error: if Funds to Allocate exceeds Starting Balance for any fund.
    * Error Message: "Funds to Allocate should not exceed Starting Balance for <Fund Name>. (Field: <Fund Name> Funds to Allocate)



  


  


Additional Behaviors:

  * When School is modified, Funds to Allocate is set for all funds, based upon the starting contribution balance for the fund.
  * When year is modified:
    * Paperwork is set to Paperwork from the School Application for the school and year.
    * # of Families for Pre-K, K-12, and OSTC is set based upon family applications for the school and year.
    * # of Families for Non-EITC is set to zero.



  


Additional Notes:

  * The following fields are editable if Check Date, Check Number, and Check Amount are all blank:
    * School
    * Year
    * Date Entered
    * Paperwork
    * The Pre-K, K-12, OSTC, and Non-EITC columns for the Funds to Allocate row in the table.
  * In the table: expressions (expr) are auto-calculated and non-editable. Fields are editable as noted above.


