11.3.2. Business Application - Status Section

Status section:

  * Received Application from Business (date; optional; 
    * warning on the field if Received Application from Business is after the final filing schedule date for the application filing schedule (either June 30 or July 1). - "The application was received after the final date for this filing schedule.")
  * Compliance Filed (date; optional)
  * Submitted Application to State (date; optional;
    * warning on the field if Submitted Application to State is after the final filing schedule date for the application filing schedule (either June 30 or July 1) - "The application was submitted after the final date for this filing schedule."
    * warning on save if State Application Number is not blank and Submitted Application to State is blank. - "If the State Application Number is specified, the Submitted Application to State date must be specified as well.")
  * State Application Number (number; editable if Received Application from Business is not blank; required if Submitted Application to State is not blank - "State Application Number" is a required field.)
  * State Fiscal Year (read-only; defaults to the value of the "Year" field in the Business Application schedule)
    * TODO_TR Austin Priest 02/28/2025: I don't understand where this macro is getting it's value. What is meant by ""Year" field in the Business Application schedule"
  * Override Status (checkbox; makes Status list editable)
  * Status (drop-list of "Pending", "Approved", and "Denied"; required if Override Status is checked)



  


Additional behaviors:

  * If Received Application from Business is cleared, Submitted Application to State is automatically cleared.



  


Other Notes:

  * Unless the "Override Status" box is checked, a status message is displayed underneath the status.
    * If the status is "Pending" and the Submitted Application to State date is empty, a message is displayed in black text: "This application is pending because the application was not submitted from May 15 through July 31."
    * If the status is "Pending" and the above date is not empty, a message is displayed in black text: "This application is pending because no contributions have been postmarked since August 1, <Year>."
    * If the status is "Approved", a message is displayed in green text: "This application was automatically approved because one or more contributions were postmarked between August 1, <Year> through May 1, <Year + 1>."
    * If the status is "Denied", a message is displayed in red text: "This application was automatically denied because no contributions were postmarked from August 1, <Year> through May 1, <Year + 1>."


