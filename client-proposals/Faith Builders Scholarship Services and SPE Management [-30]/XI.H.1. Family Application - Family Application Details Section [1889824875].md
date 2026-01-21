11.8.1. Family Application - Family Application Details Section

Family Application Details section:

  * ID (auto-set and read-only)
  * Requires Documentation (checkbox + read-only date; with the following details: 
    * checkbox defaults to not checked; 
    * if checked, the date sets to the current date and the record's normal validation that requires "Income" is suppressed, displaying a warning instead - see additional details below; 
    * automatically unchecks when an Income is entered; 
    * when unchecked, the date clears and the "Income" validation returns to normal) 
    * Probably located to the right of the ID. 
  * Family (drop-list of active families; required)
  * School Year (number; required)
  * Adults (number; required)
  * Dependents (number; required)
  * Income (number; required if the "Requires Documentation" checkbox is not checked; if the "Requires Documentation" checkbox is checked, entering a non-zero value here automatically unchecks the checkbox) 
  * The following label is displayed below Income if it is not blank:
    * In red text, if the income is greater than the government base limit or any school's custom income limit on the school application for the current year: "This family does not meet the income eligibility requirements for all schools."
    * In green text, if the income is less than the income limits for the current year: "This family meets the income eligibility requirements for all schools."
  * The following label is displayed in red text below "Income" if it is blank: "This Family Application is lacking income details." 



  


Validations:

  * Error: if School year is not a valid year. 
  * Warning: If the "Requires Documentation" checkbox is checked: "This Family Application is lacking income details." 



  


Additional behaviors:

  * If Family is changed and School Year is blank, School Year is set to the current default school year from AppHosting.zone settings.


