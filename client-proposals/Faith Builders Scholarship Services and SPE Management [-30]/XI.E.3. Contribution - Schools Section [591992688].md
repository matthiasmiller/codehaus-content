11.5.3. Contribution - Schools Section

Schools:

Embedded spreadsheet (RG):

Columns:

  * School (drop-list of active schools)
  * View (link to the selected school)
  * School Year (number; required)
  * Gross Amount (number; two decimals; required)
  * School Portion (read-only; 95% of the Gross Amount)
  * Admin Fee (read-only; 5% of the Gross Amount)



  


Validation:

  * Error on change: if duplicate schools are entered.
    * Error Message: "Duplicate schools are not allowed."
  * Error: if School Year is not a valid year.
    * Error Message: "Please enter a valid year."
  * Warning on save: if a school in the RG has already received a distribution for the school year.



_TR Austin Priest 10/04/2024: I am unable to bring about this validation. Am I missing something, is there a bug, or is the spec wrong?

TODO_NM: Tim Reitz 02/24/2025: Could you take a look at this? 

  * Warning on save: if School Year is not the same or next year as the School Year from the Contribution section.
    * Warning Message: "School Year should be <ContributionYear> or <ContributionYear+1>. (Field: School Year; Row: BB School #0925)"



  


Additional Behaviors:

  * When School is modified: School Year is set to the Default School Year for the contribution.


