11.11.1. Member Application - Member Application Details Section

  


Requirements

Member Application Details:

  


TODO_NM: Tim Reitz 09/17/2024: Should we display the Member Application ID on the detail screen?

  


  * Member (required; drop-list of active contacts marked Eligible for SPE)
  * Application Type (required; drop-list)



List items:

  * Prefilled by SPE
  * Completed by Member


  * Application Date (required; defaults to the current date)
  * Tax Year (auto-calculated; read-only; tax year of application date until admitted; year of admittance date after admitted)
  * Year # (required; drop-list)



List items:

  * Year 1 of 2
  * Year 2 of 2


  * Total Amount
  * Renew (checkbox; defaults to checked)
  * Inactive (checkbox)
    * (unlabeled date field; visible when Inactive is checked; uneditable)



  


Additional behaviors:

  * When Application Type or Application Date are modified:
    * If there is a "Year 1 of 2" member application and no "Year 2 of 2" application for the previous year and the selected member, Year # is set to  "Year 2 of 2".
    * If there was no "Year 1 of 2" member application for the previous year and the selected member, Year # is set to "Year 1 of 2".
  * When Inactive is checked:
    * The date field that becomes visible is set to the current date.
    * Renew is unchecked.



  


Validation:

  * Error on save: if Total Amount is not equal to the sum of the Amount column in the School Designations RG.
    * Error Message: "School designation total amount should equal the applications total amount. (Field: Total Amount)"
  * Error: if Inactive is checked and Admittance Status is "Admitted".
    * Error Message: "The member application cannot be marked as inactive when check status is not shredded. (Field: Inactive)"
  * Error on save: if Inactive is checked, Check Status is not blank, and Check Status is not set to "Shredded".
    * Error Message: "The member application cannot be marked as inactive when check status is not shredded. (Field: Inactive)"
  * Warning on save if Renew is not checked for an admitted year 1 of 2 application: "Renew is not checked for an admitted year 1 of 2 member application."
    * Warning Message: "Renew is not checked for an admitted year 1 of 2 member application."



  


Development Specification

TODO_NM: Use Ifs in SPEMemberAppCalculatedDefaultYearNum and add comments.
