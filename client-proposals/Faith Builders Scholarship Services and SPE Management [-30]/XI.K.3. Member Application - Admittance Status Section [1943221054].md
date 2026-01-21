11.11.3. Member Application - Admittance Status Section

  


Requirements

Admittance Status:

  * Admittance Status (automatic and read-only)
    * Inactive (if the application is marked inactive)
    * Pending Accepted by SPE (if the Application Type is Completed by Member, Accepted by SPE is checked, and SPE Application is blank)
    * Waiting for Payment (if the Application Type is Completed by Member, Accepted by SPE is checked, and SPE Application is not blank)
    * Admitted (if the Application Type is Completed by Member, Accepted by SPE is checked, and payment has been received)
    * Pending (if none of the other conditions are met)
  * Admitted Date (visible if Admitted; auto-calculated and read-only; latest date of Accepted by SPE date and check dates)
  * Accepted by SPE (checkbox)
    * (unlabeled date; visible if Accepted By SPE; defaults to the current date when Accepted by SPE is set)
  * Payment Due Date (visible and required if Accepted by SPE)
  * SPE Application (drop-list of approved SPE Applications for the year of admittance; visible and required if accepted by SPE)
  * SPE (uneditable; auto-set; link to SPE record from linked SPE Application)



  


Additional behaviors:

  * When Accepted by SPE is set:
    * The accepted date is set to the current date.
    * Payment Due Date is set to acceptance date  \+ # of Days Until Member Payment Due from AppHosting.zone settings.
  * When acceptance date is modified, Payment Due Date is set to acceptance date + # of Days Until Member Payment Due from AppHosting.zone settings.
  * When SPE Application is modified, SPE is set.



  


Validation:

  * Warning on save: if there is more than one member application for the same member, tax year, and year number.
    * Warning Message: "Member has more than one application for the same tax year and year number."
  * Error on save: if Application Type is "Prefilled by SPE" and Accepted By SPE is checked.
    * Error Message: "Prefilled by SPE member applications cannot be marked as accepted. (Field: Accepted By SPE)"
  * Error on save: if Year # does not match the Year # from the SPE Application.
    * Error Message: "Year # does not match. Only an approved '<SPEMemberAppYearNumber>' SPE application can be selected. (Field: SPE Application)"
  * Error on save: if the SPE Application does not have enough available funds for the member application.
    * Error Message: "The selected SPE application does not have enough available funds for this member application. (Field: SPE Application)"



  


Development Specification

TODO_NM:

OnChange on SPEMemberAppAcceptedBySPE should be modified to use a Condition:

OnChange:Condition:DetailNewValue; 

SPEMemberAppPaymentDueDate =

SPEMemberAppAcceptanceDate +

NAToZero( LookupAppHostingSettings( NumDaysUntilMemberPaymentDue))

  


Label capitalization: Accepted by SPE
