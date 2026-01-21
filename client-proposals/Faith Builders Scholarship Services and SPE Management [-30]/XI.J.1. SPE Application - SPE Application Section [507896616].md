11.10.1. SPE Application - SPE Application Section

  


Requirements

SPE Application: 

  * Name (auto-generated and read-only)
  * SPE (required; list of SPEs; links to the SPE; editable if Application Status is not "Approved")
  * Year # (required; drop-list; editable if Application Status is not "Approved")
  * List items:
    * Year 1 of 2 (Initial)
    * Year 1 of 2 (Renewal)
    * Year 2 of 2
  * Application Date (required; drop-list; defaults to "May 15"):
    * May 15
    * July 1
  * Application Year (required; editable if Application Status is not "Approved")
  * Application Amount (required)
  * Application Number
  * Application Status (automatic and read-only):
    * If an approval date is specified, "Approved".
    * If Approval Date is blank, "Pending" until June 30 of the year following the application year
    * Approval Date is blank and the current date is later than June 30 of the year following the application year, "Denied".
  * Approval Date
  * Approved Amount (required if approval date is specified; may be less than the application amount)
  * Tax Year (required)
  * Receipt Submitted Due Date
  * Receipt Submitted Actual Date 
  * SO Disbursement Due Date
  * Stage Acknowledgment Letter Date
  * SPE's Business Application (drop-list of business applications for the business contact linked to the SPE; links to the Business Application)



  


Additional Behaviors:

  * On save: Name is set to <SPE> \- <Application Year>, <Year #> \- <Application Amount> \- <Application Number>.
  * If the record has not been saved and Year # is modified, Application Date is set to "July 1" if Year # is "Year 1 of 2 (Initial)". If the Year # is set to a different value, Application Date is set to "May 15".
  * When Approval Date is modified:
    * If Approval Date is not blank, Tax Year is set to the year of the Approval Date.
    * Receipt Submitted Due Date is set to the Approval Date + # of Days Until SPE Receipt Due from AppHosting.zone settings.
    * SO Disbursement Due Date is set to the Approval Date + # of Days until SO Disbursement Due from AppHosting.zone settings.



  


Validation:

  * Error on save: if a "Year 2 of 2" application already exists for this SPE for the entered Tax Year.
    * Error Message: "A 'Year 2 of 2' SPE application already exists for <SPE> for <Year>. Multiple 'Year 2 of 2' SPE applications cannot be created for the SPE for one year.
  * Error: if Application Year is not a valid year.
    * Error Message: "Please enter a valid year."
  * Warning on save: if Application Number is blank.
    * Warning Message: "Missing application number. (Field: Application Number)"
  * Warning on save: if the Application Number begins with "TEMP" and the record is not being saved for the first time.
    * Warning Message: "SPE application has a temporary application number assigned and it needs to be updated. (Field: Application Number)"
  * Warning: if Approved Amount is greater than Application Amount.
    * Warning Message: "Approved amount exceeds the application amount. (Field: Approved Amount)"
  * Error: if Tax Year is not a valid year.
    * Error Message: "Please enter a valid year."
  * Warning on save: if Application Status is "Approved", the Receipt Submitted Due Date is blank or in the past, and the Receipt Submitted Actual Date is blank.
    * Warning Message: "Receipt submitted date is missing. (Field: Receipt Submitted Actual Date)"



  


Development Specification

TODO_NM: Use ListFilter for the HelperList on SPEAppSPE.
