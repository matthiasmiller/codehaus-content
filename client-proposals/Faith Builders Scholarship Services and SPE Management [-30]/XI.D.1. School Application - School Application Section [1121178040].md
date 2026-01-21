11.4.1. School Application - School Application Section

  


Requirements

School Application:

  * ID (auto-set and uneditable; <school contact ID number>-<Year>)
  * School (drop-list of active school type contacts; required)
  * Year (number; required)
  * All For Tuition (checkbox)
  * Paperwork (drop-list; required)
    * List items:
      * School Managed
      * PASS Managed 
  * School Type (drop-list; required)
    * List items:
      * September School
      * November School
  * Qualifies for OSTC (checkbox)
  * Custom Income Limits (checkbox)
  * Custom Base Salary (number; visible if Custom Income Limits is checked); required for non-draft applications when visible)
  * Custom Per Dependent Amount (number; visible if Custom Income Limits is checked; required for non-draft applications when visible)
  * Target Funds (number)
  * Family Application Deadline (date)
  * Number of Students (number)
  * Received Confirmation from School (date)
  * Temporarily Allow Editing (checkbox; visible for non-draft applications)



  


Additional Behaviors:

  * Temporarily Allow Editing is always unchecked on Save.



  


Validation:

  * Error on save: if there is already a school application for the school and application year.
    * Error Message: "A school application already exists for this year."
  * Error: if the selected school is the scholarship organization for the system Config_ScholarshipOrgSchool system switch, set to Faith Builders Training Institute).



_TR Austin Priest 10/04/2024: I do not understand the above validation. You can't set a scholarship org on the school field.

TODO_NM: Tim Reitz 02/24/2025: Could you take a look at this? Is this for School Managed schools or something like that? 

  * Error: if Year is not a valid year.
    * Error Message: "Please enter a valid year."
  * Error: if the Paperwork on the distribution for the school and application year does not match Paperwork on the application.
    * Error Message: "The school applied to be School Managed, but it has a distribution that is PASS Managed. (Field: Paperwork)"
  * Error: if Custom Income Limits is checked and no Custom Base Salary is entered.
    * Error Message: "You should specify custom base salary if custom income limits are enabled. (Field: Custom Base Salary)"
  * Warning on save: if Custom Base Salary is less than the government base income limit from AppHosting.zone settings for the application year.
    * Warning Message: "The school's base salary is less than the government's base salary. Is this what you intended? (Field: Custom Base Salary)"
  * Error: if Custom Income Limits is checked and Custom Per Dependent Amount is blank.
    * Error Message: "You should specify custom per dependent amount if custom income limits are enabled. (Field: Custom Per Dependent Amount)"
  * Warning on save: if Custom Per Dependent Amount is less than the government per dependent amount from AppHosting.zone settings for application year.
    * Warning Message: "The school's per dependent amount is less than the government's per dependent. Is this what you intended? (Field: Custom Per Dependent Amount)"
  * Warning: if there is a distribution for the school and application year and Temporarily Allow Editing is checked.
    * Warning Message: "Changing the school application settings could affect existing distributions. (Field: Temporarily Allow Editing)"



  


Additional Notes:

  * School Applications are considered to be draft application if Received Confirmation from School is blank and there are no distributions for the school and application year.
  * For draft application, "(Draft)" is added to the section label.
  * The following fields are only editable for draft applications or if Temporarily Allow Editing is checked:
    * School
    * Year
    * All For Tuition
    * Paperwork
    * School Type
    * Qualifies for OSTC
    * Custom Income Limits



  


Development Specification

TODO_NM: SchoolAppTargetFunds should not have decimals.
